# p107-listas-aleatorios-suma.py
# Programa para generar dos listas aleatorias y una con la suma solo si ambos numeros son impares

print('\033[H\033[J')

import random

listaA = []
listaB = []
listaSuma = []

for i in range(10):
    listaA.append(random.randint(1, 100))
    listaB.append(random.randint(1, 100))
    
for i in range(10):
    if listaA[i] % 2 != 0 and listaB[i] % 2 != 0:
        listaSuma.append(listaA[i] + listaB[i])
    else:
        listaSuma.append(0)

print('--- Listas Generadas ---')
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')

print('\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---')
print(f'Lista C: {listaSuma}')

print("\nPrograma terminado")