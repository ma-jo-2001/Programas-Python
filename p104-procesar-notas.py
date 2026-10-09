# p104-procesar-notas.py 
# Programa para leer calificaciones hasta que el usuario introduzca 0

print('\033[H\033[J')

lista_cal = []

while True:
    try:
        nota = float(input('Introduce una nota (0 para terminar): '))
        if nota < 0 or nota > 100:
            print('Error: la nota debe estar entre 0 y 100.')
            continue
        if nota == 0:
            break
        lista_cal.append(nota)
    except ValueError:
        print('Error: introduce un numero valido.')

if len(lista_cal) == 0:
    print('No se introdujeron notas.')
else:
    cant = len(lista_cal)
    s = sum(lista_cal)
    promedio = s / cant
    nota_max = max(lista_cal)
    nota_min = min(lista_cal)

    mn_promedio = [n for n in lista_cal if n < promedio]

    print("\n--- RESULTADOS ---")
    print(f'Cantidad de notas introducidas: {cant}')
    print(f'Lista de notas: {lista_cal}')
    print(f'Suma de las notas: {s:.2f}')
    print(f'Promedio de las notas: {promedio:.2f}')
    print(f'Nota máxima: {nota_max}')
    print(f'Nota mínima: {nota_min}')
    print(f'Notas menores al promedio ({len(mn_promedio)}): {mn_promedio}')

print("\nPrograma terminado")