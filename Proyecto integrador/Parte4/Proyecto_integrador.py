import requests

##Parte 4
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

def descarga_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('datos.csv', 'w', encoding='utf-8') as archivo_csv:
            archivo_csv.write(response.text)

descarga_datos(url)

