# pip3 install request -> instala las dependencias para hacer peticiones

import requests
import re

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'

response = requests.get(url)



if response.status_code == 200:
    print('La petición fue exitosa')

    html = response.text
    #print(html)

    # regular expression para encontrar el precio
    price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
    match = re.search(price_pattern, html)

    if match:
        print(f"El título de la web es: {match.group(1)}")