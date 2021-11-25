import requests
from bs4 import BeautifulSoup
from scraping_url import ScrapingUrl
import cloudscraper
import pandas as pd

scrapingUrl = ScrapingUrl()

def soupUrl(url):
    scraper = cloudscraper.create_scraper()

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }
    proxies = {
        'http': 'http://10.10.1.10:3128'
    }
    # url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"
    try:
        page = scraper.get(url, headers=headers, proxies=proxies, timeout=2)
        print(page.ok)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        soup = 0
        print(e)
        return soup



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


def agruparParametros(url, soup):
    # url = url
    # soup = soupUrl()
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
    lenImagenes = scrapingUrl.imgenes(soup)
    size_pagina = scrapingUrl.sizePaginaWeb(url)
    text_radio = textoRadio(soup)
    wordCount = scrapingUrl.wordCount(soup)

    print(metatitulo)

    # data = {'metatitulo': metatitulo,
    #         'wourd count': wordCount,
    #         # 'metadescription': metadescription,
    #         # # 'robots_directivas': robots_directivas,
    #         # 'puerto': puerto,
    #         # 'lenguaje': lenguaje,
    #         # 'canonical': canonical,
    #         # 'text_length': text_length,
    #         # 'links_internos': links_internos,
    #         # 'links_externos': links_externos,
    #         # # 'etiquetas': etiquetas,
    #         # 'size_pagina': size_pagina,
    #         # 'lenImagenes': lenImagenes,
    #         # 'text_radio': text_radio,
    #         'Categoria': ''}
    # df = pd.DataFrame(data=data, index=[0])
    # print(df)


def leerExcel(nombreHoja):
    direccion = 'url-seo.xlsx'
    # Crea un dataframe del excel
    data_seo = pd.read_excel(direccion, sheet_name=nombreHoja)

    feature_names = [nombreHoja]
    matriz_datos = data_seo.to_numpy()
    df = pd.DataFrame(matriz_datos, columns=feature_names)
    return df


def obtenerParametrosUrls():
    # nombreHoja = 'SEO_BAJO'
    # dfseoBajo = limpiarDatos(nombreHoja)
    nombreHoja = 'SEO_ALTO'
    dfseoAlto = leerExcel(nombreHoja)

    for iter in dfseoAlto.index:
        # url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"
        url = dfseoAlto['SEO_ALTO'][iter]
        print(url)
        soup = soupUrl(url)
        agruparParametros(url, soup)


obtenerParametrosUrls()

# url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"
# soup = soupUrl(url)
# etiquetas = scrapingUrl.etiquetaEncabezado(soup)
# print(etiquetas)
# robots_directivas = scrapingUrl.robotsDirectivas(soup)
# print(robots_directivas)




# import cloudscraper
# from bs4 import BeautifulSoup
#
# scraper = cloudscraper.create_scraper()
#
# url = "https://ec.eldirectorio.co/empresas/galapagos/laptops"
# html = scraper.get(url=url)
# soup = BeautifulSoup(html.text)
# wordCount = scrapingUrl.wordCount(soup)
#
# result = soup.find_all('a')
# a = list()
# for g in result:
#     for i in g.get_text().split():
#         a.append(i)
# wordCount = len(wordCount) + len(a)
# print(wordCount)
