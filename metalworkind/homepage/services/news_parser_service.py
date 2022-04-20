import requests
from bs4 import BeautifulSoup
import random
import re
from datetime import datetime
from homepage.models import News

from config import news_sources, proxy_pool


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
    else:
        return None

def prepare_data(html, source, value):
    soup = BeautifulSoup(html, "html.parser")

    if value.get('title').get('sclass'):
        print('erher')
        title = soup.find(value['title']['tag'], attrs={'class': value['title']['class']}).find(value['title']['stag'], attrs={'class': value['title']['sclass']}).get_text().strip()

    else:
        title = soup.find(value['title']['tag'], attrs={'class': value['title']['class']}).get_text().strip()

    if value.get('link').get('sclass'):

        link = soup.find(value['link']['tag'], attrs={'class': value['link']['class']}).find(value['link']['stag'], attrs={'class': value['link']['sclass']}).get('href').strip()
    else:
        link = soup.find(value['link']['tag'], attrs={'class': value['link']['class']}).find('a').get('href').strip()

    if value.get('date').get('stag'):
        date = soup.find(value['date']['tag'], attrs={'class': value['date']['class']}).find('p').get_text().strip()
    else:
        date = soup.find(value['date']['tag'], attrs={'class': value['date']['class']}).get_text().strip()

    data = {
        'title': title,
        'url': modification_url(link, value['url']),
        'published_date': datetime.strptime(modification_date(date), '%Y/%m/%d'),
        'source': source
    }
    print(data)

    return data

def modification_url(link, uri):
    if 'http' in link:
        return link
    else:
        split_uri = uri.split('/')
        url = split_uri[0] + '//' + split_uri[2]
        return url + link

def modification_date(date):
    _month_list = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12',
    }

    def split_date(date, sep):
        split = date.split(sep)
        if len(split[0]) == 4:
            splited_date = {
                'year': split[0].strip(),
                'month': split[1].strip(),
                'day': split[2].strip()
            }
        else:
            splited_date = {
                'day': split[0].strip(),
                'month': split[1].strip(),
                'year': split[2].strip()
            }
        return splited_date

    def check_year(year):
        if len(year) == 4:
            return 'four'
        elif len(year) == 2:
            return 'two'
        else:
            return 'bad'

    def new_date_generate(year, month, day):
        new_date = year + '/' + month + '/' + day
        return new_date

    if re.findall(r'[а-яА-Я]+', date):
        splited_date = split_date(date, ' ')
        replace_month = _month_list[splited_date['month']]
        if check_year(splited_date['year']) == 'four':
            return new_date_generate(splited_date['year'], replace_month, splited_date['day'])
        elif check_year(splited_date['year']) == 'two':
            return new_date_generate('20' + splited_date['year'], replace_month, splited_date['day'])
        else:
            year = re.findall(r'[\d]+', splited_date['year'])[0]
            if len(year) == 4:
                return new_date_generate(year, replace_month, splited_date['day'])
            elif len(year) == 2:
                return new_date_generate('20' + year, replace_month, splited_date['day'])
            else:
                return new_date_generate(str(datetime.now().year), replace_month, splited_date['day'])

    elif re.findall(r'[\.\/]+', date):
        date = date.replace('/', '.')
        splited_date = split_date(date, '.')
        if check_year(splited_date['year']) == 'four':
            return new_date_generate(splited_date['year'], splited_date['month'], splited_date['day'])
        elif check_year(splited_date['year']) == 'two':
            return new_date_generate('20' + splited_date['year'], splited_date['month'], splited_date['day'])
        else:
            year = re.findall(r'[\d]+', splited_date['year'])[0]
            if len(year) == 4:
                return new_date_generate(year, splited_date['month'], splited_date['day'])
            elif len(year) == 2:
                return new_date_generate('20' + year, splited_date['month'], splited_date['day'])
            else:
                return new_date_generate(str(datetime.now().year), splited_date['month'], splited_date['day'])

def write_metal_prices_to_db(payload):
    return News.objects.get_or_create(**payload)

def get_news():
    sources = news_sources.NEWS_SOURCES
    for source, value in sources.items():
        try:
            html = get_data(value['url'])
            if html:
                news = prepare_data(html, source, value)
                write_metal_prices_to_db(news)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    get_news()