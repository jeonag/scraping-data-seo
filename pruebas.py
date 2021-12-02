# import cloudscraper
# from bs4 import BeautifulSoup
#
# scraper = cloudscraper.create_scraper()
# url = "https://www.officedepot.com.mx/"
#
# html = scraper.get(url)
# print(html.ok)
# #     retun;
# soup = BeautifulSoup(html.text)
#
# # viewport = soup.find('meta', attrs={'name': 'viewport'})["content"]
#
# try:
#     html_language = soup.find('html')["lang"]
#     if html_language:
#         print(html_language)
# except:
#     print("0")

from urllib.parse import urlparse, parse_qs

URL = 'https://computacion.mercadolibre.com.ec/vendo-cyber-y-venta-compus-y-laptops-en-otavalo'
parsed_url = urlparse(URL)
print(parse_qs(parsed_url.query))


from newspaper import Article
import requests
from bs4 import BeautifulSoup
from readability.readability import Document as Paper
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re