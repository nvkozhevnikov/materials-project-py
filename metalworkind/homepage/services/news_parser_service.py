import requests
from bs4 import BeautifulSoup
import random

import proxy_pool
import news_sources

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

def get_data(url):
    user = get_headers_proxy()
    try:
        request = requests.get(url, headers=user['headers'],
                         proxies=user['proxy_dict'], verify=False, timeout=5)
    except:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
        request = requests.get(url, headers=headers, verify=False, timeout=5)

    if request.status_code == 200:
        return request.text

def prepare_data(data):
    soup = BeautifulSoup(data, "html.parser")
    title = soup.find('p', attrs={'class': 'press-center-banner__title'}).get_text()
    link = soup.find('a', attrs={'class': 'press-center-banner__link'}).get('href')
    date = soup.find('p', attrs={'class': 'press-center-banner__date'}).get_text()
    print(date)





if __name__ == '__main__':
    sources = news_sources.NEWS_SOURCES
    for source, value in sources.items():
        prepare_data(get_data(value['url']))