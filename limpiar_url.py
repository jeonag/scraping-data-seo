import pandas as pd


def limpiarDatos(nombreHoja):
    direccion = 'datos_serp.xlsx'
    # Crea un dataframe del excel
    data_seo = pd.read_excel(direccion, sheet_name=nombreHoja)

    feature_names = [nombreHoja]
    matriz_datos = data_seo.to_numpy()
    df = pd.DataFrame(matriz_datos, columns=feature_names)
    # Eliminar registros repetidos y mantener el último
    # df.drop_duplicates(subset=feature_names, keep="last", inplace=True)
    # # Eliminar registros que coincidan con string de la lista
    buscarStrings = ['facebook', 'netflix', 'mercadolibre', 'olx', 'walmart', 'amazon', 'instagram', '.pdf', 'scribd',
                     'netflix', 'ebay', 'twitter', 'fiscalia', 'linkedin', 'prezi', 'pinteres',
                     'wikipedia', 'eluniverso', 'elcomercio', 'artefacta', '.ksp', 'lahora', 'news',
                     'docx', 'hotel', 'books', 'areasprotegidas', 'bestbuy', 'rtu', 'trabajo', '.gob', 'vymaps',
                     'municipiodeatacames', 'elcomercio', 'ubica.ec', 'clasificados', 'los40', '.edu', 'vistazo',
                     'iess', 'defensacivil', 'milanuncios', 'paginas-amarillas', 'infoanuncios', 'netlife', '.doplim',
                     'elpais', 'gallivantations', 'avianca', 'books.google', 'bbc', 'corporativo.tia',
                     'chrome', 'tetris', 'horarios', 'plusvalia', 'eldirectorio', 'puertolibreecuador', 'aliexpress',
                     'elpalaciodehierro', 'findsun', 'clasiec', 'yahoo','buscobus']
    pattern = '|'.join(buscarStrings)
    var = df[~df[nombreHoja].str.contains(pattern)]
    return var


nombreHoja = 'SEO_BAJO'
dfseoBajo = limpiarDatos(nombreHoja)
nombreHoja = 'SEO_ALTO'
dfseoAlto = limpiarDatos(nombreHoja)

# df1 = pd.DataFrame(var, columns=['SEO_Alto'])
# df2 = pd.DataFrame(var, columns=['SEO_Bajo'])

with pd.ExcelWriter('serp_clean2.xlsx') as writer:
    dfseoAlto.to_excel(writer, sheet_name='SEO_ALTO')
    dfseoBajo.to_excel(writer, sheet_name='SEO_BAJO')
