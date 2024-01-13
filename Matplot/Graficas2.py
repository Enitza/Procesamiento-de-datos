import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Ejercicio 1
archivo = pd.read_csv('notas_estudiantes.csv')
df = pd.DataFrame(archivo)

#Ejercicio 2
plt.figure(figsize=(10, 6))
sns.boxplot(x='materia', y='nota', data=df)
plt.xlabel('Notas')
plt.title('Distribución de Notas de los Estudiantes')
plt.yticks([])  

plt.show()

#Ejercicio 3
aprobados = df[df['aprobado'] == 'Si'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

labels = ['Aprobados', 'No Aprobados']
sizes = [aprobados, no_aprobados]
colors = ['lightgreen', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Proporción de Estudiantes Aprobados y No Aprobados')

plt.show()
