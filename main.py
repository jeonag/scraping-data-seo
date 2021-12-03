import requests
from bs4 import BeautifulSoup
from scraping_url import ScrapingUrl
import cloudscraper
import pandas as pd

scrapingUrl = ScrapingUrl()


# url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"

def soupUrl(url):
    scraper = cloudscraper.create_scraper()

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }
    proxies = {
        'http': 'http://10.10.1.10:3128'
    }
    try:
        page = scraper.get(url, headers=headers, timeout=10)
        print(page.ok)
        if not page.ok:
            return
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
    lenguaje = scrapingUrl.lenguaje(soup)
    canonical = scrapingUrl.canonical(soup)
    len_metadescription = scrapingUrl.lenMetadescripcion(soup)
    robots_directivas = scrapingUrl.robotsDirectivas(soup)
    puerto = scrapingUrl.puerto(soup)
    text_length = scrapingUrl.lenParrafo(soup)
    links_internos = scrapingUrl.linksInternos(soup)
    links_externos = scrapingUrl.linksExternos(soup)
    lenImagenes = scrapingUrl.imgenes(soup)
    size_pagina = scrapingUrl.sizePaginaWeb(url)
    text_radio = textoRadio(soup)
    loadTime = scrapingUrl.loadTime(url)
    wordCount = scrapingUrl.wordCount(soup)
    etiquetas = scrapingUrl.etiquetaEncabezado(soup)
    len_h_uno = scrapingUrl.lenHeadingUno(soup)
    len_h_dos = scrapingUrl.lenHeadingDos(soup)
    len_h_tres = scrapingUrl.lenHeadingTres(soup)
    len_h_cuatro = scrapingUrl.lenHeadingCuatro(soup)
    len_h_cinco = scrapingUrl.lenHeadingCinco(soup)
    len_h_seis = scrapingUrl.lenHeadingSies(soup)
    len_metatitulo = scrapingUrl.len_metatitulo(soup)

    ldata = [url,
             len(url),
             wordCount,
             puerto,
             text_length,
             links_internos,
             links_externos,
             size_pagina,
             lenImagenes,
             text_radio,
             loadTime,
             len_h_uno,
             len_h_dos,
             len_h_tres,
             len_h_cuatro,
             len_h_cinco,
             len_h_seis,
             len_metadescription,
             len_metatitulo,
             robots_directivas,
             '2']
    return ldata


def leerExcel(nombreHoja):
    direccion = 'serp_clean.xlsx'
    # Crea un dataframe del excel
    data_seo = pd.read_excel(direccion, sheet_name=nombreHoja)

    feature_names = [nombreHoja]
    matriz_datos = data_seo.to_numpy()
    df = pd.DataFrame(matriz_datos, columns=feature_names)
    return df


def obtenerParametrosUrls():
    nombreHoja = 'SEO_BAJO'
    # dfseoBajo = leerExcel(nombreHoja)
    # nombreHoja = 'SEO_ALTO'
    dfseoAlto = leerExcel(nombreHoja)
    ldata = []
    for iter in dfseoAlto.index:
        url = dfseoAlto['SEO_BAJO'][iter]
        # url = dfseoAlto['SEO_ALTO'][iter]
        print(url)
        soup = soupUrl(url)
        if soup is None:
            continue
        df2 = agruparParametros(url, soup)
        ldata.append(df2)
        # print(ldata)
    return ldata


data = obtenerParametrosUrls()
print(data)
columnas = ['url', 'url_len', 'wourd count', 'puerto', 'text_length', 'links_internos', 'links_externos', 'size_pagina',
            'lenImagenes', 'text_radio', 'Load Time', 'len_h_uno', 'len_h_dos', 'len_h_tres', 'len_h_cuatro',
            'len_h_cinco', 'len_h_seis', 'len_metadescription', 'len_metatitulo', 'robots_directives', 'Categoria']
dfseoAlto = pd.DataFrame(data=data, columns=columnas)
with pd.ExcelWriter('matriz_seo_bajo1.xlsx') as writer:
    dfseoAlto.to_excel(writer, sheet_name='SEO_BAJO')
