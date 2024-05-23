if __name__ == "__main__":
## Bibliotecas y modulos
    import pandas as pd
## Importar las funciones desde el módulo funciones.py
    from functions import explorar_datos, comparar_columnas_df, renombrar_fecha, seleccionar_columnas, cambiar_tipo_datos, imputacion_edad, imputacion_objets
    from functions.variaciones import mostrar_variaciones
## Importación de los dataset
    df_2020 = pd.read_csv('ds/linea144-2020.csv')
    df_2021 = pd.read_csv('ds/linea144-2021.csv')
    df_2022 = pd.read_csv('ds/linea144-enero-diciembre-2022.csv')
    df_2023 = pd.read_csv('ds/linea144-enero-junio-2023.csv')
## Exploración de datos
    # Periodo 2020
    explorar_datos(df_2020)
    # Periodo 2021
    explorar_datos(df_2021)
    # Periodo 2022
    explorar_datos(df_2022)
    # Periodo 2023
    explorar_datos(df_2023)

##COLUMNAS

## Verifico compatibilidad de df (columnas)
    # Diccionario 
    dataframes = {
        'df_2020': df_2020,
        'df_2021': df_2021,
        'df_2022': df_2022,
        'df_2023': df_2023
    }
    comparar_columnas_df(dataframes)
## Renombro- nombre de columna: Fecha.
    renombrar_fecha(df_2022)
    renombrar_fecha(df_2023)

## Datos seleccionados para su análisis
    columns_to_keep = ['fecha', 'prov_residencia_persona_en_situacion_violencia', 'genero_persona_en_situacion_de_violencia', 'edad_persona_en_situacion_de_violencia', 'pais_nacimiento_persona_en_situacion_de_violencia', 'tipo_de_violencia_fisica', 'tipo_de_violencia_psicologica', 'tipo_de_violencia_sexual', 'tipo_de_violencia_economica_y_patrimonial', 'tipo_de_violencia_simbolica', 'tipo_de_violencia_domestica', 'modalidad_de_violencia_institucional', 'modalidad_de_violencia_laboral', 'modalidad_violencia_contra_libertad_reproductiva', 'modalidad_de_violencia_obstetrica', 'modalidad_de_violencia_mediatica', 'modalidad_de_violencia_otras', 'vinculo_con_la_persona_agresora', 'genero_de_la_persona_agresora']
## Concatenación de los DataFrames
    df_final = pd.concat([seleccionar_columnas(df_2020, columns_to_keep), seleccionar_columnas(df_2021, columns_to_keep), seleccionar_columnas(df_2022, columns_to_keep), seleccionar_columnas(df_2023, columns_to_keep)], ignore_index=True)
## Renombrado de columnas para mejor manejo.
    df_final.rename(columns={
        "prov_residencia_persona_en_situacion_violencia": "prov_res_victima",
        "genero_persona_en_situacion_de_violencia": "genero_victima",
        "edad_persona_en_situacion_de_violencia": "edad_victima",
        "pais_nacimiento_persona_en_situacion_de_violencia": "origen_victima",
        "vinculo_con_la_persona_agresora": "vinculo_con_agresor",
        "genero_de_la_persona_agresora": "genero_agresor"
    }, inplace=True)
    print(df_final.head(10))

## MODIFICACION DE DATOS

##Tipo de datos: fecha--> datetime.
    cambiar_tipo_datos(df_final, 'fecha', 'datetime64[ns]')
## Decido imputar los datos faltantes en la columna edad de la víctima por el número -1
    imputacion_edad(df_final)
## Imputación valores faltantes de columnas: prov_res_victima, genero_victima, origen_victima, vinculo_con_agresor, genero_agresor
    imputacion_objets(df_final)
## Normalizo valores str
    mostrar_variaciones(df_final)