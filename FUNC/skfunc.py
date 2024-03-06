def getskinfo(sk):
    import stripe
    stripe.api_key = sk
    all = stripe.radar.ValueList.list()
    useripdb = ""
    cardbindb = ""
    cardcountrydb = ""
    ipcountrydb = ""
    usersipresp = """Users IP Blacklisted: (0)
N/A"""
    cardbinresp = """Card Bin Blacklisted: (0)
N/A"""
    cardcountryresp = """Card Country Blacklisted: (0)
N/A"""
    ipcountryresp = """Country's IP Blacklisted: (0)
N/A"""
    for i in all:
        module = i["alias"]
        if module == "client_ip_address_blocklist":
            totalip = i["list_items"]["total_count"]
            if totalip != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    useripdb += each + "\n"
                usersipresp = f"""Users IP Blacklisted: ({totalip})
{useripdb}"""
            else:
                usersipresp = f"""Users IP Blacklisted: ({totalip})
N/A"""
        elif module == "card_bin_blocklist":
            totalbin = i["list_items"]["total_count"]
            if totalbin != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    cardbindb += each + "\n"
                cardbinresp = f"""Card Bin Blacklisted: ({totalbin})
{cardbindb}"""
            else:
                cardbinresp = f"""Card Bin Blacklisted: ({totalbin})
N/A"""
        elif module == "card_country_blocklist":
            totalcountry = i["list_items"]["total_count"]
            if totalcountry != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    cardcountrydb += each + "\n"
                cardcountryresp = f"""Card Country Blacklisted: ({totalcountry})
{cardcountrydb}"""
            else:
                cardcountryresp = f"""Card Country Blacklisted: ({totalcountry})
N/A"""

        elif module == "client_ip_country_blocklist":
            ipcountry = i["list_items"]["total_count"]
            if ipcountry != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    ipcountrydb += each + "\n"
                ipcountryresp = f"""Country's IP Blacklisted: ({ipcountry})
{ipcountrydb}"""
            else:
                ipcountryresp = f"""Country's IP Blacklisted: ({ipcountry})
N/A"""
        else:
            pass
    return usersipresp, cardbinresp, cardcountryresp, ipcountryresp


def getbalance(sk):
    import stripe
    stripe.api_key = sk
    fetch = stripe.Balance.retrieve()
    get = fetch["available"][0]
    currency = fetch["available"][0]["currency"]
    balance = fetch["available"][0]["amount"]
    cards = fetch["available"][0]["source_types"]["card"]
    return currency, balance, cards

def skmass(sk):
    try:
        import requests
        r = requests.Session()
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
        data1 = "type=card&card[number]=5326102318247350&card[exp_month]=03&card[exp_year]=26&card[cvc]=627"
        result = r.post(url1, data=data1, headers=headers1)
        try:
            id = result.json()["id"]
            result = "LIVE"
        except:
            result = result.text
        if result == "LIVE":
            response = "✅ 𝗟𝗜𝗩𝗘 𝗞𝗘𝗬"
        elif "rate limit" in result:
            response = "♻️ 𝗥𝗔𝗧𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗"
        elif "Invalid API Key" in result:
            response = "𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐊𝐄𝐘 𝐌𝐅! 𝐁𝐎𝐙𝐎 𝐑𝐔𝐍!"
        elif "𝐊𝐄𝐘 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐒𝐇𝐈𝐓! 𝐁𝐎𝐙𝐎 𝐑𝐔𝐍! provided" in result:
            response = "𝐊𝐄𝐘 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐒𝐇𝐈𝐓! 𝐁𝐎𝐙𝐎 𝐑𝐔𝐍! ❌"
        elif "Your account cannot currently make live charges." in result:
            response = "𝐓𝐄𝐒𝐓𝐌𝐎𝐃𝐄 𝐊𝐄𝐘 𝐒𝐇𝐈𝐓! 𝐁𝐎𝐙𝐎 𝐑𝐔𝐍! ❌"
        else:
            response = "f{result} ❌"
        return (f"<code>{sk}</code>\n<b>𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ {response}</b>\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")