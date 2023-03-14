import time
import requests
import selectorlib
import datetime
import streamlit
import plotly.express as px

URL = 'https://programmer100.pythonanywhere.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/39.0.2171.95 Safari/537.36'
}


def scraper(url):
    """Scrape URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def scrape_source(src):
    extractor = selectorlib.Extractor.from_yaml_file('target.yaml')
    value = extractor.extract(src)['temperature']
    return value


if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        scraped = scraper(URL)
        temperature = scrape_source(scraped)
        print(temperature)
        with open('temperatures.txt', 'a') as file:
            file.write(f'{now.strftime("%d-%m-%Y %H:%M:%S")}, {temperature}\n')
        time.sleep(2)
