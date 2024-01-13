import requests
import pandas as pd
import numpy as np

##Parte 4
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

def descarga_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('datos.csv', 'w', encoding='utf-8') as archivo_csv:
            archivo_csv.write(response.text)

##Parte 5
df = pd.read_csv('datos.csv')
df = pd.DataFrame(df)

def limpieza(df):
    #Verificar que no existan valores faltantes
    df = df.dropna()

    #Verificar que no existan filas repetidas
    df = df.drop_duplicates()

    #Verificar si existen valores atípicos y eliminarlos
    columnas = ['creatinine_phosphokinase', 'platelets', 'serum_sodium']
    for columna in columnas:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1

        # Definir los límites para detectar valores atípicos
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_cleaned = df[(df[columna] >= lower_bound) & (df[columna] <= upper_bound)]


    #Categorizar por edades
    rangos = [0, 12, 19, 39, 59, float('inf')]
    etiquetas = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']

    categorias = pd.cut(df_cleaned['age'],bins=np.array(rangos),labels=etiquetas)
    df_cleaned = df_cleaned.copy()
    df_cleaned['Categoria edad'] = categorias
    df_cleaned.to_csv('datos_filtrados.csv', index=False)
