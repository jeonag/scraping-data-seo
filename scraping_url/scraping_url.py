import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}
proxies = {
    'http': 'http://10.10.1.10:3128'
}

url = "https://www.yataco.com.pe/cargador-laptop/ciu.php?ciu=ec-zam&key=Cargador-de-Laptop-Zamora"
page = requests.get(url, headers=headers, proxies=proxies)

soup = BeautifulSoup(page.text, 'html.parser')


class ScrapingUrl:
    def metatitulo(self, soup):
        try:
            metatitle = (soup.find('title')).get_text()
            print("METATITULO", metatitle)
            return metatitle
        except:
            metatitle = 0
            return metatitle

    def metadescripcion(self, soup):
        try:
            metadescription = soup.find('meta', attrs={'name': 'description'})["content"]
            print("METADESCRIPCION", metadescription)
        except:
            print("no metadescr")

    # h3 = soup.find_all('h3')  # It would return the content between the H1 tags.
    # print("ETIQUETA H3", h3)

    def robotsDirectivas(self, soup):
        try:
            robots_directives = soup.find('meta', attrs={'name': 'robots'})["content"].split(",")
            print("DIRECTIVAS ROBOTS", robots_directives)
        except:
            print("Error ")

    def puerto(self, soup):
        try:
            viewport = soup.find('meta', attrs={'name': 'viewport'})["content"]
            print("VIEWPORT", viewport)
        except:
            print("no puerto")

    def lenguaje(self, soup):
        try:
            html_language = soup.find('html')["lang"]
            print("LANGUAJE", html_language)
        except:
            print("no leng")

    def canonical(self, soup):
        try:
            canonical = soup.find('link', attrs={'rel': 'canonical'})["href"]
            print(canonical)
        except:
            print(" no canonical")

    def lenParrafo(self, soup):
        try:
            paragraph = [a.get_text() for a in soup.find_all('p')]
            # print(paragraph)
            # Text length
            text_length = sum([len(a) for a in paragraph])
            print(text_length)
        except:
            print("no parrafo ")

    def etiquetaEncabezado(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h1')]
            headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # Cleaning the headers list to get the tag and the text as different elements in a list
            list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            print(list_headers)
        except:
            print("no etiqeuta cabezadp")

    def imgenes(self, soup):
        images = [[a["src"], a["alt"]] if "alt" in str(a) else [a["src"], ""] for a in soup.find_all('img')]
        print(images)

    def linksInternos(self, soup):
        internal_links = [
            [a.get_text(), a["href"], "nofollow"] if "nofollow" in str(a) else [a.get_text(), a["href"], "follow"]
            for a in soup.find_all('a', href=True) if "<your_domain>" in a["href"] or a["href"].startswith("/")]
        number_internal_links = len(internal_links)
        print(number_internal_links)

    def linksExternos(self, soup):
        external_links = [
            [a.get_text(), a["href"], "nofollow"] if "nofollow" in str(a) else [a.get_text(), a["href"], "follow"]
            for a in soup.find_all('a', href=True) if
            "<your_domain>" not in a["href"] and not a["href"].startswith("/")]
        # To get the number of links
        number_external_links = len(external_links)
        print(number_external_links)

    def sizePaginaWeb(self, url):
        r = urlopen(url)
        sizePage = len(r.read())
        print(sizePage)

    def tiempoCacheNavegador(self, url):
        res = requests.head(url)
        # print(res.headers)
        print(res.headers['Cache-Control'])

    def lenUrl(self, url):
        lenUrl = len(url)
        print(lenUrl)

    def concatenar_lista(self, lista, caracter):
        if isinstance(lista, list):
            if isinstance(caracter, str):
                return caracter.join(map(str, lista))
            raise TypeError('El parámetro caracter debe ser una cadena de caracteres (str).')
        raise TypeError('El parámetro lista debe ser una lista.')

    # def textoRadio(self, soup):
    #     body = concatenar_lista(soup.body.get_text().split(), ' ')
    #     bodyCount = len(body)
    #     # print('Text Ratio')
    #     # tomar todos lo valores en el html incluido tags
    #     html = (soup.html.encode('UTF-8'))
    #     textRatio = "{0:.2f}".format((bodyCount / len(html)) * 100)
    #     print(textRatio)


# x = ScrapingUrl()
# x.metatitulo(soup)