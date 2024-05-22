def comparar_columnas_df(dataframes):
    # Obtener las columnas de cada DataFrame
    columnas_por_df = {nombre: df.columns.tolist() for nombre, df in dataframes.items()}

    # Comparar las columnas de cada DataFrame con las columnas de los otros DataFrames
    for nombre_df, columnas_df in columnas_por_df.items():
        print(f"- Columnas del DataFrame '{nombre_df}':")
        for otro_nombre_df, otro_columnas_df in columnas_por_df.items():
            if nombre_df != otro_nombre_df:
                diferencias = set(columnas_df) - set(otro_columnas_df)
                if diferencias:
                    print(f"- Columnas que están en '{nombre_df}' pero no en '{otro_nombre_df}': {diferencias}")
        print()