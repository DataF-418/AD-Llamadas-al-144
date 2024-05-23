import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import plotly.express as px
from sklearn.model_selection import train_test_split

## Recurso
df_final = pd.read_csv('df_final.csv')

## I. ANALISIS UNIVARIADO

## 1. DISTRIBUCIÓN DE LA EDAD DE LAS VICTIMAS
    ## Edad- Total, relativo
edad_info = df_final['edad_victima'].describe()
print (edad_info)

 #VALORES ATÍPICOS
"Se registra un solo valor con 127. Decido eliminarlo de forma manual, este se encontraba en el df_2021"
    ## Edad- total sin -1
df_final_filtrado = df_final[df_final['edad_victima'] != -1]
edad_info_final = df_final_filtrado['edad_victima'].describe()
print('Las valores descriptivos reales sobre las edades son:', edad_info_final)

    ## PORCENTAJE DE VALORES IMPUTADOS (-1)- EDAD

num_valores_menos_1 = df_final[df_final['edad_victima'] == -1]['edad_victima'].count()
porcentaje_menos_1 = (num_valores_menos_1 / len(df_final['edad_victima'])) * 100
print("El {:.2f}% del total original corresponde a -1 en la columna 'edad_victima'.".format(porcentaje_menos_1))

## Histograma para visualizar la dispersión de la edad de las personas en situación de violencia.

plt.figure(figsize=(10,6))
sns.histplot(df_final_filtrado['edad_victima'], bins=20, kde=True, color='skyblue')

plt.axvline(edad_info_final['mean'], color='red', linestyle='dashed', linewidth=1, label='Media')
plt.axvline(edad_info_final['50%'], color='green', linestyle='dashed', linewidth=1, label='Mediana')

plt.xlabel('Edad de la víctima')
plt.ylabel('Frecuencia')
plt.title('Distribución de la Edad de las Personas en Situaciones de Violencia')
plt.legend()

plt.grid(True)
plt.show()

## 2. DISTRIBUCIÓN POR GÉNERO DE LAS VÍCTIMAS
    ## FRECUENCIA DE VÍCTIMAS POR GÉNERO
plt.figure(figsize=(10, 6))
sns.countplot(x='genero_victima', data=df_final, hue='genero_victima', palette='viridis', dodge=False)
plt.xlabel('Género de la víctima')
plt.ylabel('Frecuencia')
plt.title('Distribución de Género de las Víctimas')
plt.legend([],[], frameon=False)  # Para evitar la duplicación de leyenda
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.show()

    ## COMPARACIÓN DE LAS DISTRIB. DE EDAD POR GÉNERO. (VICTIMAS)
plt.figure(figsize=(12, 8))
sns.boxplot(x='genero_victima', y='edad_victima', data=df_final_filtrado, hue='genero_victima', palette='viridis')
plt.xlabel('Género de la víctima')
plt.ylabel('Edad de la víctima')
plt.title('Distribución de Edad por Género de las Víctimas')
plt.legend([],[], frameon=False)  # Para evitar la duplicación de leyenda
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()

## 3. TIPOS DE VIOLENCIA
tipos_de_violencia = [
    'tipo_de_violencia_fisica',
    'tipo_de_violencia_psicologica',
    'tipo_de_violencia_sexual',
    'tipo_de_violencia_economica_y_patrimonial',
    'tipo_de_violencia_simbolica',
    'tipo_de_violencia_domestica'
]

for tipo in tipos_de_violencia:
    df_final[tipo] = df_final[tipo].apply(lambda x: 1 if x.lower() == 'si' else 0)
violencia_counts = df_final[tipos_de_violencia].sum()
prorcentajes_violencia = (violencia_counts / violencia_counts.sum()) * 100
    # GRAFICO DE TORTA- DISTRIBUCIÓN DE LOS TIPOS DE VIOLENCIA %
plt.figure(figsize=(10, 8))
plt.pie(prorcentajes_violencia, labels=prorcentajes_violencia.index.str.replace('_', ' ').str.title(), autopct='%1.1f%%', colors=plt.cm.viridis(np.linspace(0, 1, len(prorcentajes_violencia))))
plt.title('Gráfico de Torta - Distribución de los Tipos de Violencia (%)')
plt.axis('equal')  # Para asegurar que el gráfico de torta sea circular
plt.show()

## 4 FRECUENCIA DE LAS MODALIDADES DE VIOLENCIA
modalidades_violencia = [
    'modalidad_de_violencia_institucional',
    'modalidad_de_violencia_laboral',
    'modalidad_violencia_contra_libertad_reproductiva',
    'modalidad_de_violencia_obstetrica',
    'modalidad_de_violencia_mediatica',
    'modalidad_de_violencia_otras'
]
for tipo in modalidades_violencia:
    df_final[tipo] = df_final[tipo].apply(lambda x: 1 if x.lower() == 'si' else 0)
violencia_mod_counts = df_final[modalidades_violencia].sum()
porcentajes_mod_violencia = (violencia_mod_counts / violencia_mod_counts.sum()) * 100

# GRAFICO DE TORTA- FREC. DE CADA MODALIDAD. %
plt.figure(figsize=(10, 8))
plt.pie(porcentajes_mod_violencia, labels=porcentajes_mod_violencia.index.str.replace('_', ' ').str.title(), autopct='%1.1f%%', colors=plt.cm.viridis(np.linspace(0, 1, len(porcentajes_mod_violencia))))
plt.title('Gráfico de Torta - Distribución de las Modalidades de Violencia (%)')
plt.axis('equal')  # Para asegurar que el gráfico de torta sea circular
plt.show()

## 5. DISTRICUBIÓN GEOGRÁFICA
    ## GRÁFICO DE BARRAS- DISTRIBUCIÓN DE INCIDENTES POR PROV.
plt.figure(figsize=(12, 6))
sns.countplot(x='prov_res_victima', data=df_final, color='skyblue')
plt.xlabel('Provincia')
plt.ylabel('Cantidad de Incidentes')
plt.title('Distribución de Incidentes por Provincia')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()

## 6. FRECUENCIA DE LOS AGRESORES POR SU GÉNERO
    ## GRÁFICO DE BARRAS- FRECUENCIA DE LOS AGRESORES POR GÉNERO.
plt.figure(figsize=(8, 6))
sns.countplot(x='genero_agresor', data=df_final, color='skyblue')
plt.xlabel('Género del Agresor')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de los Agresores por Género')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()

## 7. FRECUENCIA DE LOS DIF. VÍNCULOS CON EL AGRESOR.
    ## GRÁFICO DE TORTA- FRECUENCIA DE LOS DIF. VÍNCULOS CON EL AGRESOR.

vinculos_agresor = df_final['vinculo_con_agresor'].value_counts()

# Crear el gráfico de torta
vinculos_agresor = df_final['vinculo_con_agresor'].value_counts()
plt.figure(figsize=(10, 8))
pie = plt.pie(vinculos_agresor, labels=vinculos_agresor.index, autopct='%1.1f%%', colors=plt.cm.viridis(np.linspace(0, 1, len(vinculos_agresor))))
plt.title('Distribución de los Diferentes Vínculos con el Agresor')
plt.legend(vinculos_agresor.index, title="Vínculo con el Agresor", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.axis('equal')
plt.show()


## II. ANALISIS BIVARIADO.

## EDAD DE LA VÍCTIMA Y GÉNERO DEL AGRESOR.
    ## GRÁFICO BOXPLOTS- COMPARACIÓN DE LA DIST. DE EDADES SEGÚN GÉNERO DEL AGRE.
## EDAD DE LA VÍCTIMA Y VÍNCULO CON EL AGRESOR
    ## GPRAFICO BLOXPLOTS- COMP. DE LA DISTR. DE LAS EDADES  DE LAS VÍCTIMAS SEGÚN VINCULO CON EL AGRESOR.


