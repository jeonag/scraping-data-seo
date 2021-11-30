import requests
from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd

# palabrasClaves = 'laptops quayaquil'

palabrasClaves = [
    "Quito", "Guayaquil", "Cuenca", "Guaranda", "Tulcán", "Riobamba", "Latacunga", "Esmeraldas", "Galapagos",
    # "Ibarra", "Loja", "Babahoyo", "Portoviejo", "Macas", "Tena",
    # "Orellana", "Puyo", "Santo Domingo", "Loja", "Ambato", "Zamora",

    # "Machala", "Manta", "Protoviejo", "Otavalo", "Cayambe", "Salinas", "Machachi", "Atacames", "Patate",
    # "Guano", "Tabacundo", "Pelileo", "Atuntaqui", "Pedernales", "Azogues", "Santa Elena", "Chone"

]

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 "
        "Safari/537.36 Edge/18.19582 "
}


def obtenerSerpAlto(palabrasClaves, headers):
    params = {'q': palabrasClaves}

    html = requests.get('https://www.google.com/search', headers=headers, params=params).text
    soup = BeautifulSoup(html, 'lxml')
    url = []
    # container with all needed data
    for result in soup.select('.tF2Cxc'):
        link = result.select_one('.yuRUbf a')['href']
        url.append(link)
    print(url)
    return url


def obtenerSerpBajo(palabrasClaves, headers):
    scraper = cloudscraper.create_scraper()

    params = {
        'q': palabrasClaves,
        'hl': ['en', 'es'],
        'num': '32'
    }

    html = scraper.get('https://www.google.com/search', headers=headers, params=params).text
    soup = BeautifulSoup(html, 'lxml')
    url = []
    # container with all needed data
    for result in soup.select('.tF2Cxc'):
        link = result.select_one('.yuRUbf a')['href']
        url.append(link)
        # print(f'{link}')
    return url


# interseccion = set(serpAlto).intersection(serpBajo)
# listaInterseccion = list(interseccion)

listSerpAlto = []
listSerpBajo = []
for k in palabrasClaves:
    query = "laptops " + k
    serpAlto = obtenerSerpAlto(query, headers)
    serpBajo = obtenerSerpBajo(query, headers)
    lSerpBajo = list(set(serpBajo) - set(serpAlto))
    totalSerpAlto = 10 + len(serpAlto)
    lSerpBajo = lSerpBajo[0:totalSerpAlto]
    for i in lSerpBajo:
        listSerpBajo.append(i)
    for j in serpAlto:
        listSerpAlto.append(j)

df1 = pd.DataFrame(listSerpAlto, columns=['SEO_Alto'])
df2 = pd.DataFrame(listSerpBajo, columns=['SEO_Bajo'])

with pd.ExcelWriter('datos_serp_3.xlsx') as writer:
    df1.to_excel(writer, sheet_name='SEO_ALTO')
    df2.to_excel(writer, sheet_name='SEO_BAJO')
