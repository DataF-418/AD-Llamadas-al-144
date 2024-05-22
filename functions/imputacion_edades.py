def imputacion_edad(df):
    if df['edad_victima'].isnull().any():
        null_count = df['edad_victima'].isnull().sum()
        print(f"Se encontraron {null_count} valores nulos en la columna 'edad_victima'.")
        # Llenar los valores nulos con -1 y convertir el tipo de dato a entero
        df['edad_victima'] = df['edad_victima'].fillna(-1).astype(int)
        print("Valores nulos se imputaron con -1 y tipo de dato convertido a entero.")
    else:
        print("No se encontraron valores nulos en la columna 'edad_victima'. No se realizaron cambios.")
    
    return df


