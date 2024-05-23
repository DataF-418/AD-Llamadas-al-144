import unicodedata

def limpiar_valores(columna):
    return columna.apply(lambda x: unicodedata.normalize('NFKD', str(x).lower()).encode('ASCII', 'ignore').decode('utf-8'))

def mostrar_variaciones(df):
    valores_unicos = {}
    for columna in df.columns:
        valores_limpios = limpiar_valores(df[columna])
        valores_unicos[columna] = valores_limpios.value_counts()
    for columna, conteo_valores in valores_unicos.items():
        print(f"Valores únicos y su frecuencia en la columna '{columna}':")
        print(conteo_valores)
        print()