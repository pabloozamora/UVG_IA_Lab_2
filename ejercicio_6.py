'''
Inteligencia Artificial - Sección 20
Laboratorio #2

Diego Andrés Morales Aquino - 21762
Erick Stiv Junior Guerra - 21781
Pablo Andrés Zamora Vásquez - 21780
'''

import matplotlib.pyplot as plt
from random import random, randint
import numpy as np

nodes = ['A','B','C','D','E','F','G','H','I','J']
p_val = 0.9
m = 4
n = 1000

resultsA = []
resultsB = []

def transition_table(p):
    '''
        Crea la matriz de transición en base a un valor de p.
    '''
    return [
            [p,(1-p)/2,(1-p)/2,0,0,0,0,0,0,0],
            [0,p,0,(1-p),0,0,0,0,0,0],
            [0,0,p,(1-p),0,0,0,0,0,0],
            [0,0,0,p,(1-p)/2,0,0,(1-p)/2,0,0],
            [0,0,0,0,p,(1-p)/3,0,0,(1-p)/3,(1-p)/3],
            [0,0,0,0,0,p,(1-p),0,0,0],
            [0,0,0,0,0,0,p,0,(1-p),0],
            [0,0,0,0,0,0,0,p,0,(1-p)],
            [0,0,0,0,0,0,0,0,p,(1-p)],
            [0,0,0,0,0,0,0,0,0,p],
        ]
    
def markov(p,limit=float('inf'), obj='J'):
    '''
        Realiza la simulación del grafo.
    '''
    steps = 0
    transitions = transition_table(p)
    S = 'A'
    
    while(steps < limit and S != obj):
        steps += 1
        rand = random()
        if rand < p:
            continue
        options = [(index, value) for index,value in enumerate(transitions[nodes.index(S)])
                   if value > 0]
        
        selected = options[randint(1,len(options)-1)][0]
        
        S = nodes[selected]
    return (steps, S)

# Número de pasos
for i in range(n):
    steps, _ = markov(p_val, obj='J')
    resultsA.append(steps)
    
# Última posición alcanzada
for i in range(n):
    _, last = markov(p_val, limit=m)
    resultsB.append(last)
    
# Distribución del número de pasos necesarios.
plt.hist(resultsA, bins=max(resultsA)-min(resultsA)+1, color='skyblue', edgecolor='black', alpha=0.7, density=True)
plt.xlabel('Pasos')
plt.ylabel('Frecuencia')
plt.title(f'Número de pasos necesarios ({n} ensayos)')
plt.show()

# Distribución de posiciones en los nodos después de M movimientos.
counts = {letter: resultsB.count(letter) for letter in nodes}
frequencies = []

for letter in nodes:
    frequencies.extend([letter] * counts[letter])


plt.hist(frequencies, bins=np.arange(len(nodes)+1)-0.5, color='pink', edgecolor='black', alpha=0.7, density=True)
plt.xlabel('Nodo alcanzado')
plt.ylabel('Frecuencia')
plt.title(f'Posición después de {m} movimientos ({n} ensayos)')
plt.show()