import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scraping_url.scraping_url import ScrapingUrl

scrapingUrl = ScrapingUrl()

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}
proxies = {
    'http': 'http://10.10.1.10:3128'
}

url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"
page = requests.get(url, headers=headers, proxies=proxies)

soup = BeautifulSoup(page.text, 'html.parser')

scrapingUrl.metatitulo(soup)
