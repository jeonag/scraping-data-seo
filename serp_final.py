try:
    from googlesearch import search
    import pandas as pd
except ImportError:
    print("No module named 'google' found")

# to search
provincias = [
    # "Quito",
    # "Guayaquil",
    # "Cuenca",
    # "Guaranda",
    # "Tulcán",
    # "Riobamba",
    # "Latacunga",
    "Machala"
    # "Esmeraldas",
    # "Galapagos",

    # "Ibarra",
    # "Loja",
    # "Babahoyo",
    # "Portoviejo",
    # "Macas",
    # "Tena",
    # "Orellana",
    # "Puyo",
    # "Santo Domingo",
    # "Loja",
    # "Ambato",
    # "Zamora"
]

# Documentation https://www.geeksforgeeks.org/performing-google-search-using-python-code/
contSeoAlto = 0
constSeoBajo = 0
listSeoAlto = []
listSeoBajo = []
aux = " "

for k in provincias:
    query = "laptops " + k
    for j in search(query, tld="com", num=60, stop=60, pause=20):
        if j.split('/')[2] == aux:
            continue
        aux = j.split('/')[2]
        if contSeoAlto < 10:
            listSeoAlto.append(j)
            contSeoAlto = contSeoAlto + 1
            continue
        if constSeoBajo < 20:
            listSeoBajo.append(j)
            constSeoBajo = constSeoBajo + 1
        else:
            contSeoAlto = 0
            constSeoBajo = 0
            break

df1 = pd.DataFrame(listSeoAlto, columns=['SEO_Alto'])
df2 = pd.DataFrame(listSeoBajo, columns=['SEO_Bajo'])

with pd.ExcelWriter('datos_machala.xlsx') as writer:
    df1.to_excel(writer, sheet_name='SEO_ALTO')
    df2.to_excel(writer, sheet_name='SEO_BAJO')
