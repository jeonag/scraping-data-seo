import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()


headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    'q': 'laptops quito',
    'hl': ['en', 'es'],
    'num': '32'
}

html = scraper.get('https://www.google.com/search', headers=headers, params=params).text
soup = BeautifulSoup(html, 'lxml')

# container with all needed data
for result in soup.select('.tF2Cxc'):
    title = result.select_one('.DKV0Md').text
    link = result.select_one('.yuRUbf a')['href']
    displayed_link = result.select_one('.TbwUpd.NJjxre').text
    try:
        snippet = result.select_one('#rso .lyLwlc').text
    except:
        snippet = None

    # print(f'{title}\n{link}\n{displayed_link}\n{snippet}\n')
    print(f'{link}')
    print('---------------')
