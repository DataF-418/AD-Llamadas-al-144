def imputacion_objets(df):
    for columna in df.columns:
        if df[columna].dtype == 'O' and df[columna].isnull().any():
            # Imprimir la cantidad de valores nulos encontrados y de qué columna
            null_count = df[columna].isnull().sum()
            print(f"Se encontraron {null_count} valores nulos en la columna '{columna}'.")
            
            # Imputar los valores faltantes con "no especificado"
            df.fillna({columna: 'no especificado'}, inplace=True)

