import requests
from urllib.request import urlopen


class ScrapingUrl:
    def metatitulo(self, soup):
        try:
            metatitle = (soup.find('title')).get_text()
            return metatitle
        except:
            metatitle = 0
            return metatitle

    def len_metatitulo(self, soup):
        try:
            metatitle = (soup.find('title')).get_text()
            return len(metatitle)
        except:
            metatitle = 0
            return metatitle

    def metadescripcion(self, soup):
        try:
            metadescription = soup.find('meta', attrs={'name': 'description'})["content"]
            return metadescription
        except:
            metadescription = 0
            return metadescription

    def lenMetadescripcion(self, soup):
        try:
            metadescription = soup.find('meta', attrs={'name': 'description'})["content"]
            return len(metadescription)
        except:
            metadescription = 0
            return metadescription

    def robotsDirectivas(self, soup):
        robots_dir = 0
        try:
            robots_directives = soup.find('meta', attrs={'name': 'robots'})["content"].split(",")
            if robots_directives:
                robots_dir = 1
            return robots_dir
        except:
            return robots_dir

    def puerto(self, soup):
        try:
            viewport = soup.find('meta', attrs={'name': 'viewport'})["content"]
            return viewport
        except:
            viewport = 0
            return viewport

    def lenguaje(self, soup):
        try:
            html_language = soup.find('html')["lang"]
            return html_language
        except:
            html_language = 0
            return html_language

    def canonical(self, soup):
        try:
            canonical = soup.find('link', attrs={'rel': 'canonical'})["href"]
            return canonical
        except:
            canonical = 0
            return canonical

    def lenParrafo(self, soup):
        try:
            paragraph = [a.get_text() for a in soup.find_all('p')]
            # print(paragraph)
            # Text length
            text_length = sum([len(a) for a in paragraph])
            return text_length
        except:
            text_length = 0
            return text_length

    def lenHeadingUno(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h1')]
            # headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # # Cleaning the headers list to get the tag and the text as different elements in a list
            # list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return len(h1)
        except:
            h1 = 0
            return h1

    def lenHeadingDos(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h2')]
            # headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # # Cleaning the headers list to get the tag and the text as different elements in a list
            # list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return len(h1)
        except:
            h1 = 0
            return h1

    def lenHeadingTres(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h3')]
            # headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # # Cleaning the headers list to get the tag and the text as different elements in a list
            # list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return len(h1)
        except:
            h1 = 0
            return h1

    def lenHeadingCuatro(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h4')]
            # headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # # Cleaning the headers list to get the tag and the text as different elements in a list
            # list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return len(h1)
        except:
            h1 = 0
            return h1

    def lenHeadingCinco(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h5')]
            # headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # # Cleaning the headers list to get the tag and the text as different elements in a list
            # list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return len(h1)
        except:
            h1 = 0
            return h1

    def lenHeadingSies(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h6')]
            # headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # # Cleaning the headers list to get the tag and the text as different elements in a list
            # list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return len(h1)
        except:
            h1 = 0
            return h1

    def linksInternos(self, soup):
        try:
            internal_links = [
                [a.get_text(), a["href"], "nofollow"] if "nofollow" in str(a) else [a.get_text(), a["href"], "follow"]
                for a in soup.find_all('a', href=True) if "<your_domain>" in a["href"] or a["href"].startswith("/")]
            number_internal_links = len(internal_links)
            return number_internal_links
        except:
            internal_links = 0
            return internal_links

    def linksExternos(self, soup):
        try:
            external_links = [
                [a.get_text(), a["href"], "nofollow"] if "nofollow" in str(a) else [a.get_text(), a["href"], "follow"]
                for a in soup.find_all('a', href=True) if
                "<your_domain>" not in a["href"] and not a["href"].startswith("/")]
            # To get the number of links
            number_external_links = len(external_links)
            return number_external_links
        except:
            number_external_links = 0
            return number_external_links

    def sizePaginaWeb(self, url):
        try:
            r = urlopen(url)
            sizePage = len(r.read())
            return sizePage
        except:
            sizePage = 0
            return sizePage

    def tiempoCacheNavegador(self, url):
        res = requests.head(url)
        # print(res.headers)
        print(res.headers['Cache-Control'])

    def lenUrl(self, url):
        lenUrl = len(url)
        print(lenUrl)

    def etiquetaEncabezado(self, soup):
        try:
            h1 = [a.get_text() for a in soup.find_all('h1')]
            headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            # Cleaning the headers list to get the tag and the text as different elements in a list
            list_headers = [[str(x)[1:3], x.get_text()] for x in headers]
            return list_headers
        except:
            list_headers = 0
            return list_headers

    def imgenes(self, soup):
        try:
            images = [[a["src"], a["alt"]] if "alt" in str(a) else [a["src"], ""] for a in soup.find_all('img')]
            return len(images)
        except:
            images = 0
            return images

    def wordCount(self, soup):
        try:
            wordCount = soup.find('body').get_text().split()
            return len(wordCount)
        except:
            wordCount = 0
            return wordCount

    # def concatenar_lista(self, lista, caracter):
    #     if isinstance(lista, list):
    #         if isinstance(caracter, str):
    #             return caracter.join(map(str, lista))
    #         raise TypeError('El parámetro caracter debe ser una cadena de caracteres (str).')
    #     raise TypeError('El parámetro lista debe ser una lista.')
    #
    # def textoRadio(self, soup):
    #     try:
    #         body = ScrapingUrl.concatenar_lista(soup.body.get_text().split(), ' ')
    #         bodyCount = len(body)
    #         # print('Text Ratio')
    #         # tomar todos lo valores en el html incluido tags
    #         html = (soup.html.encode('UTF-8'))
    #         textRatio = "{0:.2f}".format((bodyCount / len(html)) * 100)
    #         print(textRatio)
    #         return textRatio
    #     except:
    #         textRatio = 0
    #         return textRatio
