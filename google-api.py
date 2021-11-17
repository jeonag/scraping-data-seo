import http.client

conn = http.client.HTTPSConnection("https://computron.com.ec/")

headers = {
    'x-user-agent': "desktop",
    'x-proxy-location': "US",
    'x-rapidapi-host': "google-search3.p.rapidapi.com",
    'x-rapidapi-key': "0125d8e61fmsh787095a7af7cc32p1e22a3jsnfca4b82bd929"
}

conn.request("GET", "/api/v1/search/q=elon+musk&num=100", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
