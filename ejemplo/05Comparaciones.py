import numpy as np
import matplotlib.pyplot as plt

#Creación de semilla aleatoria para "reproductividad"
np.random.seed(0)

#Busqueda de parámetros para una distribución media
media = 0

#Desviación estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#Número de muestras deseado para su análisis
n_muestras = 1000

#Generación de datos de las distribuciones normales
data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

#Configuración de la gráfica
plt.figure(figsize=(10,6))

#Carga de frecuencias a partir de una gráfica de histograma
plt.hist(data1, bins=30, color='blue', density=True, label='Desviación Estander 1', alpha=0.5)
plt.hist(data2, bins=30, color='red', density=True, label='Desviación Estander 2', alpha=0.5)
plt.hist(data3, bins=30, color='green', density=True, label='Desviación Estander 3', alpha=0.5)

#Graficación
plt.title('Comparación de Distribuciones Normales con una semilla en random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()


