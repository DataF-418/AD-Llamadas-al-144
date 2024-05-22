#Función de exploración de datos.
from tabulate import tabulate

def explorar_datos(df):
    print("Información del DataFrame:")
    print(tabulate(df.info()))