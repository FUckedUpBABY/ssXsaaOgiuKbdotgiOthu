from FUNC.usersdb_func import *
import stripe

def ccn_charge(fullcc):
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
        stripe.api_key = sk
        splitter = fullcc.split("|")
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = splitter[3]
        while True:
            try:
                result1 = stripe.PaymentMethod.create(
                  type="card",
                  card={
                    "number": f"{cc}",
                    "exp_month": f"{mes}",
                    "exp_year": f"{ano}",
                  },
                )
                break
            except Exception as e:
                result1 = str(e)
                if "Request rate limit exceeded." in result1:
                    continue
                elif "Your card number is incorrect." in result1:
                    return result1
                    break
                elif "Invalid API Key provided" in result1 or "testmode_charges_only" in result1 or "api_key_expired" in result1:
                    return result1
                else:
                    break
        try:
            id = result1.id
        except:
            return result1
        
        while True:
            try:
                result2 = stripe.PaymentIntent.create(
            amount=60,
            currency="usd",
            payment_method_types=["card"],
            payment_method=f"{id}",
            confirm="true",
            off_session="true",
          )
                result2 = "succeeded"
                break
            except Exception as e:
                result2 = str(e)
                if "Request rate limit exceeded." in result2:
                    continue
                else:   
                    break
        return result2
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def massccncharge(fullcc, user_id):
    try:
        result = ccn_charge(fullcc)
        if '"seller_message": "Payment complete."' in result or "succeeded" in result:
            status = "Live 🟢"
            response = "Charged 0.50$ 🔥"
            

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
            response = "Card Declined 🚫"
            with open("result_logs.txt", "a") as f:
                mtcresp = f"{result}\n"
                f.write(mtcresp)
            refundcredit(user_id)
        return (f"<code>{fullcc}</code>\n<b>𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ {response}</b>\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def masstxtccn(fullcc, user_id):
    try:
        result = ccn_charge(fullcc)
        if '"seller_message": "Payment complete."' in result or "succeeded" in result:
            status = "Live 🟢"
            response = "Charged 0.50$ 🔥"
            hits = "HITS"
            

        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"
            hits = "CVV"
            

        elif "incorrect_cvc" in result or "security code is incorrect." in result or "Your card's security code is incorrect." in result or "Your card's security code is invalid." in result or "invalid_cvc" in result:
            status = "Live 🟡"
            response = "CCN Live ❎"
            hits = "CCN"
            

        elif "transaction_not_allowed" in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits = "CVV"
            

        elif '"cvc_check": "pass"' in result:
            status = "Live 🟢"
            response = "CVV LIVE ❎"
            hits = "CVV"
            

        elif "three_d_secure_redirect" in result or "card_error_authentication_required" in result:
            status = "Live 🟡"
            response = "3D Secure Redirected ❎"
            hits = "CVV"
            

        elif "stripe_3ds2_fingerprint" in result:
            status = "Live 🟡"
            response = "3D Secured ❎"
            hits = "CVV"
            

        elif "Your card does not support this type of purchase." in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits = "CVV"
            

        elif "generic_decline" in result or "You have exceeded the maximum number of declines on this card in the last 24 hour period." in result or "card_decline_rate_limit_exceeded" in result:
            status = "Dead 🔴"
            response = "𝐃𝐄𝐀𝐃 𝐂𝐀𝐑𝐃 𝐍𝐈𝐆𝐆𝐀! 💔❌"
            hits = "NO"

        elif "do_not_honor" in result:
            status = "Dead 🔴"
            response = "𝐃𝐈𝐃 𝐍𝐎𝐓 𝐇𝐎𝐍𝐎𝐑 𝐘𝐎𝐔 𝐀𝐒 𝐀 𝐂𝐀𝐑𝐃𝐄𝐑 𝐋𝐌𝐀𝐎💔❌"
            hits = "NO"

        elif "fraudulent" in result:
            status = "Dead 🔴"
            response = "Fraudulent 🚫"
            hits = "NO"

        elif "stolen_card" in result:
            status = "Dead 🔴"
            response = "Stolen Card 🚫"
            hits = "NO"

        elif "lost_card" in result:
            status = "Dead 🔴"
            response = "Lost Card 🚫"
            hits = "NO"

        elif "pickup_card" in result:
            status = "Dead 🔴"
            response = "Pickup Card 🚫"
            hits = "NO"

        elif "incorrect_number" in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card has expired." in result or "expired_card" in result:
            status = "Dead 🔴"
            response = "Expired Card 🚫"
            hits = "NO"

        elif "intent_confirmation_challenge" in result:
            status = "Dead 🔴"
            response = "Captcha 😥"
            hits = "NO"

        elif "Your card number is incorrect." in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card's expiration year is invalid." in result or "Your card\'s expiration year is invalid." in result:
            status = "Dead 🔴"
            response = "Expiration Year Invalid 🚫"
            hits = "NO"

        elif "Your card's expiration month is invalid." in result or "invalid_expiry_month" in result:
            status = "Dead 🔴"
            response = "Expiration Month Invalid 🚫"
            hits = "NO"

        elif "card is not supported." in result:
            status = "Dead 🔴"
            response = "Card Not Supported 🚫"
            hits = "NO"

        elif "invalid_account" in result:
            status = "Dead 🔴"
            response = "Dead Card 🚫"
            hits = "NO"

        elif "Invalid API Key provided" in result or "testmode_charges_only" in result or "api_key_expired" in result:
            status = "Dead 🔴"
            response = "SK DEAD 🚫"
            hits = "NO"
            refundcredit(user_id)

        elif "Your card was declined." in result or "card was declined" in result:
            status = "Dead 🔴"
            response = "𝐃𝐄𝐀𝐃 𝐂𝐀𝐑𝐃 𝐍𝐈𝐆𝐆𝐀! 💔❌"
            hits = "NO"

        else:
            status = "Dead 🔴"
            response = result
            hits = "NO"
            with open("result_logs.txt", "a") as f:
                mtcresp = f"{result}\n"
                f.write(mtcresp)
            refundcredit(user_id)
        return response, hits,fullcc
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
