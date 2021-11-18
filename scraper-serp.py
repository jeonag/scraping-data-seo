import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {'q': 'laptops quayaquil'}

html = requests.get('https://www.google.com/search', headers=headers, params=params).text
soup = BeautifulSoup(html, 'lxml')

# container with all needed data
for result in soup.select('.tF2Cxc'):
    link = result.select_one('.yuRUbf a')['href']
    print(link)

# 'https://www.google.com/search?q=laptops+guayaquil&client=opera&hs=p8P&biw=1920&bih=970&sxsrf=AOaemvJKe-rS9u3JYh_0yABniUMXAjEDWw%3A1636684300413&ei=DNKNYdDMGNzOwbkPnPCI6AM&oq=laptops&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIECCMQJzIECCMQJzIFCAAQgAQyCggAEIAEEIcCEBQyCAgAEIAEELEDMggIABCABBDJAzIFCAAQkgMyBQgAEIAEMgUIABCABDoHCCMQsAMQJzoHCAAQRxCwAzoGCCMQJxATOggILhCABBCxAzoLCAAQgAQQsQMQgwE6BQguEIAEOg4ILhCABBCxAxDHARDRAzoECAAQQzoECC4QQzoKCC4QxwEQ0QMQQzoKCC4QsQMQgwEQQzoHCAAQsQMQQzoKCAAQsQMQgwEQQ0oECEEYAFDLB1jaDWC1FGgCcAJ4AIABvQGIAdkIkgEDMC43mAEAoAEByAEKwAEB&sclient=gws-wiz'
# 'https://www.google.com/search?q=laptops+guayaquil&client=opera&hs=Gok&sxsrf=AOaemvIYEBUhw54f2gqnXsCPwN6BLFsaQg:1636684308647&ei=FNKNYbLYJt2rwbkP8JSi2AQ&start=10&sa=N&ved=2ahUKEwiyss2W5JH0AhXdVTABHXCKCEsQ8tMDegQIARA7&biw=1920&bih=970&dpr=1'
# 'https://www.google.com/search?q=laptops+guayaquil&client=opera&sxsrf=AOaemvLI-iG26_oaADjWtt9cS9yn4CUnDQ:1636689084616&ei=vOSNYe3_JNqHwbkPgv6GkAU&start=20&sa=N&ved=2ahUKEwjtzfv79ZH0AhXaQzABHQK_AVI4ChDy0wN6BAgBED4&biw=1920&bih=970&dpr=1'
