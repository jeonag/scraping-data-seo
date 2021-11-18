import pandas as pd


def limpiarDatos(nombreHoja):
    direccion = 'output_1.xlsx'
    # Crea un dataframe del excel
    data_seo = pd.read_excel(direccion, sheet_name=nombreHoja)

    feature_names = [nombreHoja]
    matriz_datos = data_seo.to_numpy()
    df = pd.DataFrame(matriz_datos, columns=feature_names)
    # Eliminar registros repetidos y mantener el último
    df.drop_duplicates(subset=feature_names, keep="last", inplace=True)
    # Eliminar registros que coincidan con string de la lista
    buscarStrings = ['facebook', 'netflix', 'mercadolibre', 'olx', 'walmart', 'amazon', 'instagram', '.pdf', 'scribd',
                     'netflix', 'milanuncios', 'ebay', 'twitter', 'fiscalia', 'linkedin', 'prezi', 'pinteres',
                     'wikipedia', 'eluniverso', 'elcomercio']
    pattern = '|'.join(buscarStrings)
    var = df[~df[nombreHoja].str.contains(pattern)]
    print(var)
    return var


nombreHoja = 'SEO_BAJO'
dfseoBajo = limpiarDatos(nombreHoja)
nombreHoja = 'SEO_ALTO'
dfseoAlto = limpiarDatos(nombreHoja)

# df1 = pd.DataFrame(var, columns=['SEO_Alto'])
# df2 = pd.DataFrame(var, columns=['SEO_Bajo'])

with pd.ExcelWriter('url_data_clean.xlsx') as writer:
    dfseoAlto.to_excel(writer, sheet_name='SEO_ALTO')
    dfseoBajo.to_excel(writer, sheet_name='SEO_BAJO')
