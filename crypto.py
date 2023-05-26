



import requests
from twilio.rest import Client

# CoinMarketCap API configuration
api_key = '2b95e3ba-d844-4326-b8ef-b54bf119409e'
headers = {
    'X-CMC_PRO_API_KEY': api_key,
    'Accepts': 'application/json'
}
params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Twilio configuration
twilio_account_sid = 'AC83df95c39a64cdf47f6a4cfa10fafa04'
twilio_auth_token = 'f3c3539c6422e7494c1e520c703e9c73'
twilio_phone_number = '+13158894983'
recipient_phone_number = '+38349569393'

# Send SMS function using Twilio
def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

# Retrieve cryptocurrency data from CoinMarketCap API
response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    sms_message = ""
    for currency in data['data']:
        name = currency['name']
        price = currency['quote']['USD']['price']
        sms_message += f"Name: {name}, Price: {price}\n"
    
    send_sms(sms_message)
    print("SMS sent successfully!")
else:
    print('Error:', response.status_code)
    print(response.json())
