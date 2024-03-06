from pyrogram import Client, filters
import requests
import time

target_chat_id = -1001901252477

@Client.on_message(filters.command("url"))
def analyze_url_and_forward(_, message):
    try:
        command_parts = message.text.split('/url ', 1)
        if len(command_parts) < 2:
            message.reply_text('**NO URL FOUND SORRY BOZO**.')
            return

        raw_urls = command_parts[1].split('\n')
        urls = [url.strip() for url in raw_urls if url.strip()]

        if not urls:
            message.reply_text('**NO URL FOUND SORRY BOZO Send 1 valid URL**.')
            return

        if len(urls) > 50:
            message.reply_text('**LIMIT IS 50 URL PER CHECK**')
            return

        checking_msg = message.reply_text('**YOUR SITES BEING CHECKED. PLEASE WAIT NEGA!**')

        for url in urls:
            result = analyze_site(url)

            formatted_result = format_result(result)
            result_message = f"{formatted_result}"

            message.reply_text(result_message)
            time.sleep(0.5)  # Introduce a 0.5-second delay after sending each result

            if result['payment_gateways']:
                forward_url_to_chat(result_message, target_chat_id, message._client)

        checking_msg.delete()

    except Exception as e:
        message.reply_text(f"Error: {str(e)}")

def forward_url_to_chat(result_message, target_chat, bot):
    try:
        # Forward the formatted result message to the specified chat
        bot.send_message(chat_id=target_chat, text=result_message,disable_web_page_preview=True)
    except Exception as e:
        print(f"Error forwarding message to chat: {str(e)}")


def format_result(result):
    formatted_result = (
        f"<b>𝐇𝐞𝐫𝐞𝐬 𝐘𝐨𝐮𝐫 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐒𝐢𝐭𝐞𝐬 𝐈𝐧𝐟𝐨 ✅ {result['url']}</b>\n"
        f"<b>𝐆𝐚𝐭𝐞𝐬</b> <code>{', '.join(result['payment_gateways']) if result['payment_gateways'] else 'None'}</code>\n"
        f"<b>𝐂𝐚𝐩𝐭𝐜𝐡𝐚</b> <code>{result['captcha']}</code>\n"
        f"<b>𝐂𝐥𝐨𝐮𝐝𝐟𝐥𝐚𝐫𝐞</b> <code>{result['cloudflare']}</code>\n"
        f"<b>𝐆𝐫𝐚𝐩𝐡𝐐𝐋</b> <code>{result['graphql']}</code>\n"
        f"<b>𝐒𝐢𝐭𝐞 𝐂𝐨𝐫𝐞</b> <code>{result['platform']}</code>\n"
        f"<b>𝐄𝐫𝐫 𝐋𝐨𝐠𝐬</b> <code>{result['error']}</code>\n"
        f"<b>𝐒𝐢𝐭𝐞 𝐒𝐭𝐚𝐭𝐮𝐬</b> <code>{result['http_status']}</code>\n"
        f"<i>𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲- @NoMoreBins </i>\n"
    )

    return formatted_result

def analyze_site(url):
    result = {'url': url, 'payment_gateways': [], 'captcha': False, 'cloudflare': False,
              'graphql': False, 'platform': None, 'http_status': None, 'error': None}

    try:
        response = requests.get(url, timeout=10)
        html=response.text
        headers = response.headers
        cookies = response.cookies
        content_type = headers.get('Content-Type', '')

        # Payment Gateway checks
        result['payment_gateways'] = check_for_payment_gateway(headers, content_type, cookies, html)

        # Cloudflare detection
        result['cloudflare'] = check_for_cloudflare(response.text)

        # CAPTCHA detection
        result['captcha'] = check_for_captcha(response.text)

        # Additional checks based on content type, cookies, etc.
        result['content_type'] = content_type
        result['cookies'] = cookies.get_dict()

        # GraphQL detection
        result['graphql'] = check_for_graphql(response.text)

        # Platform detection
        result['platform'] = check_for_platform(response.text)

        # HTTP status code
        result['http_status'] = response.status_code

    except requests.Timeout:
        result['error'] = 'Timeout error. Unable to fetch the page within the specified time.'
    except Exception as e:
        result['error'] = str(e)

    return result

def check_for_payment_gateway(headers, content_type, cookies, html):
    gateway_keywords = {
'mollie': ['mollie', 'api.mollie.com',          'mollie.com', 'mollie-payment', 'mollie-checkout', 'mollie-form', 'mollie-sdk', 'mollie-subscription', 'mollie-token', 'mollie-merchant', 'mollie-billing', 'mollie-gateway'],

'square': ['square', 'squareup.com', 'square-payment', 'square-checkout', 'square-form', 'square-sdk', 'square-subscription', 'square-token', 'square-merchant', 'square-billing', 'square-gateway','connect.squareup.com','connect.squareup.com/v2/analytics','connect.squareup.com/v2/analytics/verifications'],

'cybersource': ['cybersource', 'cybersource.com', 'cybersource-payment', 'cybersource-checkout', 'cybersource-form', 'cybersource-sdk', 'cybersource-subscription', 'cybersource-token', 'cybersource-merchant', 'cybersource-billing', 'cybersource-gateway'],

'2checkout': ['2checkout', '2checkout.com', '2checkout-payment', '2checkout-checkout', '2checkout-form', '2checkout-sdk', '2checkout-subscription', '2checkout-token', '2checkout-merchant', '2checkout-billing', '2checkout-gateway'],

'eway': ['eway', 'eway.com', 'eway-payment', 'eway-checkout', 'eway-form', 'eway-sdk', 'eway-subscription', 'eway-token', 'eway-merchant', 'eway-billing', 'eway-gateway'],

'stripe': ['stripe', 'checkout.stripe.com', 'js.stripe.com', 'stripe.com', 'stripe-elements', 'stripe-js-v3',
                   'stripe-button', 'stripe-payment', 'stripe-checkout', 'stripe-form', 'stripe-sdk', 'stripe-pay',
                   'stripe-card', 'stripe-subscription', 'stripe-checkout-button', 'stripe-elements', 'stripe-token'],
        'paypal': ['paypal', 'paypal.com', 'smart/buttons.js', 'checkout.js', 'paypal-checkout', 'paypal-button',
                   'paypal-payment', 'paypal-express', 'paypal-form', 'paypal-sdk', 'paypal-checkout-button',
                   'paypal-subscription', 'paypal-token', 'paypal-merchant', 'paypal-billing', 'paypal-braintree'],
        'braintree': ['https://js.braintreegateway.com/js/braintree-2.32.1.min.js','braintree', 'braintreegateway.com', 'braintree-api.com', 'data-braintree-name', 'braintree.js',
                      'braintree-payment', 'braintree-button', 'braintree-form', 'braintree-sdk', 'braintree-checkout',
                      'braintree-subscription', 'braintree-token', 'braintree-merchant', 'braintree-billing'],
        'worldpay': ['worldpay', 'worldpay.com', 'secure.worldpay.com', 'wp-e-commerce', 'worldpay-button',
                     'worldpay-payment', 'worldpay-express', 'worldpay-form', 'worldpay-sdk', 'worldpay-checkout',
                     'worldpay-subscription', 'worldpay-token', 'worldpay-merchant', 'worldpay-billing'],
        'authnet': ['authnet', 'authorize.net', 'authorizenet.com', 'accept-sdk', 'anet', 'authnet-button',
                    'authnet-payment', 'authnet-express', 'authnet-form', 'authnet-sdk', 'authnet-checkout',
                    'authnet-subscription', 'authnet-token', 'authnet-merchant', 'authnet-billing'],
        'recurly': ['recurly', 'recurly.com', 'recurly.js', 'recurly-integration', 'recurly-button', 'recurly-payment',
                    'recurly-checkout', 'recurly-form', 'recurly-sdk', 'recurly-express', 'recurly-subscription',
                    'recurly-token', 'recurly-merchant', 'recurly-billing'],
        'shopify': ['shopify', 'myshopify', 'shopify.com', 'checkout.shopify.com', 'shopify-checkout', 'shopify-payment-button',
                    'shopify-payment', 'shopify-checkout-button', 'shopify-express', 'shopify-form', 'shopify-sdk',
                    'shopify-subscription', 'shopify-token', 'shopify-merchant', 'shopify-billing'],
        'ayden': ['ayden', 'adyen', 'adyen.com', 'adyen-payment', 'adyen-express', 'adyen-form', 'adyen-sdk',
                  'adyen-checkout', 'adyen-subscription', 'adyen-token', 'adyen-merchant', 'adyen-billing'],
    }

    found_gateways = []

    for keyword, values in gateway_keywords.items():
        if (keyword in content_type.lower() or
                any(key.lower() in headers or key.lower() in html or keyword.lower() in str(cookies) for key in
                    values)):
            found_gateways.append(keyword.capitalize())

    return found_gateways

def check_for_cloudflare(response_text):
    cloudflare_markers = ['checking your browser', 'cf-ray', 'cloudflare']

    for marker in cloudflare_markers:
        if marker in response_text.lower():
            return True

    return False

def check_for_captcha(response_text):
    captcha_markers = ['recaptcha', 'g-recaptcha']

    for marker in captcha_markers:
        if marker in response_text.lower():
            return True

    return False

def check_for_graphql(response_text):
    graphql_markers = ['graphql', 'application/graphql']

    for marker in graphql_markers:
        if marker in response_text.lower():
            return True

    return False

def check_for_platform(response_text):
    platform_markers = {
        'woocommerce': ['woocommerce', 'wc-cart', 'wc-ajax'],
        'magento': ['magento', 'mageplaza'],
        'shopify': ['shopify', 'myshopify'],
        'prestashop': ['prestashop', 'addons.prestashop'],
        'opencart': ['opencart', 'route=common/home'],
        'bigcommerce': ['bigcommerce', 'stencil'],
        'wordpress': ['wordpress', 'wp-content'],
        'drupal': ['drupal', 'sites/all'],
        'joomla': ['joomla', 'index.php?option=com_']
    }


    for platform, markers in platform_markers.items():
        if any(marker in response_text.lower() for marker in markers):
            return platform.capitalize()

    return None
