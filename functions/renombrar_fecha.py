#F. para renombrar las columnas Fechas.
def renombrar_fecha(df):
    df.rename(columns={'Fecha': 'fecha'}, inplace=True)
