'''
Inteligencia Artificial - Sección 20
Laboratorio #2

Diego Andrés Morales Aquino - 21762
Erick Stiv Junior Guerra - 21781
Pablo Andrés Zamora Vásquez - 21780
'''

import numpy as np
import matplotlib.pyplot as plt

def lanzar_dado():
    return np.random.randint(1, 7) # Únicamente retornar un valor aleaotrio entre 1 y 6

def realizar_experimento():
    count = 1
    while lanzar_dado() in {1, 6}: # Mientras se obtenga 1 o 6, continuar los lanzamientos
        count += 1
    return count

def simular_experimentos(N):
    resultados = [realizar_experimento() for _ in range(N)] # Almacenar el conteo de lanzamientos de cada experimento
    return resultados

def mostrar_histograma(resultados, N):
    max_lanzamientos = max(resultados)
    plt.hist(resultados, bins=np.arange(1.5, max_lanzamientos + 2), align='left', density=True, rwidth=0.8)
    plt.xticks(ticks=np.arange(1, max_lanzamientos + 1))  # Asegurar que las etiquetas sean para números enteros
    plt.title(f'Histograma de {N} lanzamientos')
    plt.xlabel('Número de lanzamientos')
    plt.ylabel('Frecuencia relativa')
    plt.grid(True)
    plt.show()

N_vals = [10, 100, 1000, 10000]
for N in N_vals:
    resultados = simular_experimentos(N)
    mostrar_histograma(resultados, N)
