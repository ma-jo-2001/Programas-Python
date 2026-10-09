# p105-listas-multiplica.py
# Programa para multiplicar numeros de listas

print('\033[H\033[J')

listaA = []
listaB = []

listaA = list(map(int, input('Introduzca 5 numeros para la lista A: ').split()))

while len(listaA) != 5:
    print('Debe introducir exactamente 5 numeros.')
    listaA = list(map(int, input('Introduzca 5 numeros para la lista A: ').split()))

listaB = list(map(int, input('Introduzca 5 numeros para la lista B: ').split()))

while len(listaB) != 5:
    print('Debe introducir exactamente 5 numeros.')
    listaB = list(map(int, input('Introduzca 5 números para la lista B: ').split()))

listaC = [listaA[i] * listaB[i] for i in range(5)]

print('\n--- Resultados ---')
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
print(f'Lista C (A * B): {listaC}')

print("\nPrograma terminado")