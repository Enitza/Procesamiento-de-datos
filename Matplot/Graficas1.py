import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

##Ejercicio 1 dispersion
plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre las calificaciones de matematicas y ciencias')
plt.xlabel('Calificaciones de matematicas')
plt.ylabel('Calificaciones de ciencias')

plt.show()

#Ejercicio 2 barras de error
promedio_matematicas = np.mean(matematicas)
promedio_ciencias = np.mean(ciencias)
promedio_literatura = np.mean(literatura)

errores_promedio_matematicas = np.mean(errores_matematicas)
errores_promedio_ciencias = np.mean(errores_ciencias)
errores_promedio_literatura = np.mean(errores_literatura)

materias = ['Matemáticas', 'Ciencias', 'Literatura']
promedios = [promedio_matematicas, promedio_ciencias, promedio_literatura]
errores_promedios = [errores_promedio_matematicas, errores_promedio_ciencias, errores_promedio_literatura]

fig, ax = plt.subplots()

plt.errorbar(materias, promedios, yerr=errores_promedios, fmt='o', capsize=5)
#ax.bar(materias, promedios, yerr=errores_promedios, capsize=5, color=['blue', 'blue', 'blue'], alpha=0.7)
ax.set_xlabel('Materias')
ax.set_ylabel('Calificaciones Promedio')
ax.set_title('Calificaciones Promedio con Barras de Error')
ax.legend(['Calificaciones Promedio'])

plt.show()

#Ejercicio 3 histograma
plt.hist(matematicas, bins=10)

# Personalizar el histograma
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones de Matemáticas')

# Mostrar el histograma
plt.show()