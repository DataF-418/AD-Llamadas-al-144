import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import plotly.express as px
from sklearn.model_selection import train_test_split

df_final = pd.read_csv('df_final.csv')

## Análisis descriptivo

## EDAD

    ## Edad- Total, relativo
edad_info = df_final['edad_victima'].describe()
print (edad_info)


"""
Se registra un solo valor con 127. Decido eliminarlo.

df_final = df_final[df_final['edad_victima'] != 127]

    ## Edad- total sin -1
"""

df_final_filtrado = df_final[df_final['edad_victima'] != -1]

edad_info_final = df_final_filtrado['edad_victima'].describe()
print('Las valores descriptivos sobre las edades son:', edad_info_final)

## PORCENTAJE DE VALORES IMPUTADOS (-1)- EDAD

num_valores_menos_1 = df_final[df_final['edad_victima'] == -1]['edad_victima'].count()
porcentaje_menos_1 = (num_valores_menos_1 / len(df_final['edad_victima'])) * 100
print("El {:.2f}% del total original corresponde a -1 en la columna 'edad_victima'.".format(porcentaje_menos_1))

## Histograma para visualizar la dispersión de la edad de las personas en situación de violencia.

plt.figure(figsize=(8,6))
plt.hist(df_final_filtrado['edad_victima'], bins=20, color='skyblue', edgecolor='black')

plt.xlabel('Edad de la víctima')
plt.ylabel('Frecuencia')
plt.title('Distribución de la Edad de las Personas en Situaciones de Violencia')

plt.xticks(np.arange(0, max(df_final_filtrado['edad_victima']), step=10))

# Agregar líneas verticales para la media y la mediana
plt.axvline(edad_info_final['mean'], color='red', linestyle='dashed', linewidth=1, label='Media')
plt.axvline(edad_info_final['50%'], color='green', linestyle='dashed', linewidth=1, label='Mediana')

plt.legend()

# Mostrar el histograma
plt.grid(True)
plt.show()
