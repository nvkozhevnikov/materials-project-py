import requests
import xml.etree.ElementTree as et
import random
from datetime import date
from homepage.models import ExchangeRates, Currencies

import proxy_pool

def get_headers_proxy():
    users = proxy_pool.USER_AGENTS_PROXY_LIST
    user = random.choice(users)
    headers = {'user-agent': user['user-agent']}
    proxy_dict = {'http': user['http_proxy']}
    persona = {
        'headers': headers,
        'proxy_dict': proxy_dict
    }
    return persona

def get_usd_price():
    user = get_headers_proxy()
    url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={date.today().strftime('%d/%m/%Y')}"
    try:
        r = requests.get(url, headers=user['headers'],
                         proxies=user['proxy_dict'], timeout=5)
    except:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=5)

    if r.status_code == 200:
        p = et.fromstring(r.text)
        i = 0
        for x in p:
            if p[i].attrib['ID'] == 'R01235':
                for child in p[i]:
                    if child.tag == 'Value':
                        usd = child.text.strip()
            i += 1
        return usd

def write_exchange_rate(rate):
    rate = rate.replace(',', '.')
    currency = Currencies.objects.get(name='USD')
    return ExchangeRates.objects.create(price=rate, currency=currency)

def main():
    write_exchange_rate(get_usd_price())

if __name__ == '__main__':
    main()