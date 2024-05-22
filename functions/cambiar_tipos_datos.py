def cambiar_tipo_datos(df, columna, tipo):
    df[columna] = df[columna].astype(tipo)
