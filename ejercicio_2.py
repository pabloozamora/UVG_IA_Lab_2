'''
Inteligencia Artificial - Sección 20
Laboratorio #2

Diego Andrés Morales Aquino - 21762
Erick Stiv Junior Guerra - 21781
Pablo Andrés Zamora Vásquez - 21780
'''

import random
import matplotlib.pyplot as plt

def lanzar_dado():
    return random.randint(1, 6) # Únicamente retornar un valor aleaotrio entre 1 y 6

def simular_experimentos(N):
    sumas = [lanzar_dado() + lanzar_dado() for _ in range(N)] # Simular N experimentos de lanzar dos dados y calcula el promedio de las sumas
    return sum(sumas) / N

def repetir_simulacion_y_graficar(M, N):
    promedios = [simular_experimentos(N) for _ in range(M)] # Repetir la simulación de N experimentos M veces y graficar los promedios obtenidos
    
    plt.hist(promedios, bins=15, edgecolor='black', alpha=0.75)
    plt.title(f'Distribución de los promedios de {M} repeticiones (N={N})')
    plt.xlabel('Promedio de la suma de dos dados')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

valores_M = [5, 10, 50, 100, 200]
N = 10000  # Número de lanzamientos en cada simulación
for M in valores_M:
    repetir_simulacion_y_graficar(M, N)
