from metalworkind.celery import app
from .services.sendinblue_service import subscribe_doi, send_transactional_email
from .services.cbr_exchange_rate_service import get_usd_rate
from .services.get_metal_prices_service import get_metal_prices
from .services.news_parser_service import get_news


@app.task
def subscribe_doi_sendinblue(email):
    subscribe_doi(email)

@app.task
def send_transaction_email_sendinblue(data):
    send_transactional_email(data)

@app.task
def download_currency_rate():
    get_usd_rate()

@app.task
def download_metal_prices():
    get_metal_prices()

@app.task
def parse_news():
    get_news()



