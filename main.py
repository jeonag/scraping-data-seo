import requests
from bs4 import BeautifulSoup
from scraping_url import ScrapingUrl

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

# Parametros SEO
metatitulo = scrapingUrl.metatitulo(soup)
metadescription = scrapingUrl.metadescripcion(soup)
robots_directivas = scrapingUrl.robotsDirectivas(soup)
puerto = scrapingUrl.puerto(soup)
lenguaje = scrapingUrl.lenguaje(soup)
canonical = scrapingUrl.canonical(soup)
text_length = scrapingUrl.lenParrafo(soup)
links_internos = scrapingUrl.linksInternos(soup)
links_externos = scrapingUrl.linksExternos(soup)
etiquetas = scrapingUrl.etiquetaEncabezado(soup)
imagenes = scrapingUrl.imgenes(soup)
size_pagina = scrapingUrl.sizePaginaWeb(url)


def concatenar_lista(lista, caracter):
    if isinstance(lista, list):
        if isinstance(caracter, str):
            return caracter.join(map(str, lista))
        raise TypeError('El parámetro caracter debe ser una cadena de caracteres (str).')
    raise TypeError('El parámetro lista debe ser una lista.')


def textoRadio(soup):
    try:
        body = concatenar_lista(soup.body.get_text().split(), ' ')
        bodyCount = len(body)
        # print('Text Ratio')
        # tomar todos lo valores en el html incluido tags
        html = (soup.html.encode('UTF-8'))
        textRatio = "{0:.2f}".format((bodyCount / len(html)) * 100)
        return textRatio
    except:
        textRatio = 0
        return textRatio


text_radio = textoRadio(soup)
