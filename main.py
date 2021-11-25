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
        page = scraper.get(url, headers=headers, timeout=4)
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
    len_metadescription = scrapingUrl.lenMetadescripcion(soup)
    robots_directivas = scrapingUrl.robotsDirectivas(soup)
    puerto = scrapingUrl.puerto(soup)
    lenguaje = scrapingUrl.lenguaje(soup)
    canonical = scrapingUrl.canonical(soup)
    text_length = scrapingUrl.lenParrafo(soup)
    links_internos = scrapingUrl.linksInternos(soup)
    links_externos = scrapingUrl.linksExternos(soup)
    lenImagenes = scrapingUrl.imgenes(soup)
    size_pagina = scrapingUrl.sizePaginaWeb(url)
    text_radio = textoRadio(soup)
    wordCount = scrapingUrl.wordCount(soup)
    etiquetas = scrapingUrl.etiquetaEncabezado(soup)
    len_h_uno = scrapingUrl.lenHeadingUno(soup)
    len_h_dos = scrapingUrl.lenHeadingDos(soup)
    len_h_tres = scrapingUrl.lenHeadingTres(soup)
    len_h_cuatro = scrapingUrl.lenHeadingCuatro(soup)
    len_h_cinco = scrapingUrl.lenHeadingCinco(soup)
    len_h_seis = scrapingUrl.lenHeadingSies(soup)
    len_metatitulo = scrapingUrl.len_metatitulo(soup)

    data = {
        # 'metadescription': metadescription,
        # # 'robots_directivas': robots_directivas,
        # 'lenguaje': lenguaje,
        # 'canonical': canonical,
        # # 'etiquetas': etiquetas,
        'url': url,
        'url_len': len(url),
        'wourd count': wordCount,
        'puerto': puerto,
        'text_length': text_length,
        'links_internos': links_internos,
        'links_externos': links_externos,
        'size_pagina': size_pagina,
        'lenImagenes': lenImagenes,
        'text_radio': text_radio,
        'len_h_uno': len_h_uno,
        'len_h_dos': len_h_dos,
        'len_h_tres': len_h_tres,
        'len_h_cuatro': len_h_cuatro,
        'len_h_cinco': len_h_cinco,
        'len_h_seis': len_h_seis,
        'len_metadescription': len_metadescription,
        'len_metatitulo': len_metatitulo,
        'Categoria': '1'}
    df = pd.DataFrame(data=data, index=[0])
    # print(df)
    # print(data)
    return df


def leerExcel(nombreHoja):
    direccion = 'url_data_clean.xlsx'
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
    data = {}
    df = pd.DataFrame(data=data, index=[0])
    for iter in dfseoAlto.index:
        # url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"
        url = dfseoAlto['SEO_ALTO'][iter]
        print(url)
        soup = soupUrl(url)
        data = {
        # 'metadescription': metadescription,
        # # 'robots_directivas': robots_directivas,
        # 'lenguaje': lenguaje,
        # 'canonical': canonical,
        # # 'etiquetas': etiquetas,
        'url': 0,
        'url_len': 0,
        'wourd count': 0,
        'puerto': 0,
        'text_length': 0,
        'links_internos': 0,
        'links_externos': 0,
        'size_pagina': 0,
        'lenImagenes': 0,
        'text_radio': 0,
        'len_h_uno': 0,
        'len_h_dos': 0,
        'len_h_tres': 0,
        'len_h_cuatro': 0,
        'len_h_cinco': 0,
        'len_h_seis': 0,
        'len_metadescription': 0,
        'len_metatitulo': 0,
        'Categoria': '1'}
        df = pd.DataFrame(data=data, index=[0])
        df2 = agruparParametros(url, soup)
        df.append(df2)
        print(df)
    return df


data = obtenerParametrosUrls()
print(data)
# dfseoAlto = pd.DataFrame(data=data, index=[0])
with pd.ExcelWriter('matriz_seo_alto.xlsx') as writer:
    data.to_excel(writer, sheet_name='SEO_ALTO')
