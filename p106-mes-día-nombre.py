# p106-mes-día-nombre.py
# Programa para leer mes del 1 al 12 muestra su nombre y la cantidad de dias que tiene

print('\033[H\033[J')

nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes_num = int(input('Introduzca un numero de mes (1-12): '))

if 1 <= mes_num <= 12:
    print('\n--- Resultados ---')
    print(f'Mes: {nombres_meses[mes_num - 1]}')
    print(f'Dias: {dias_mes[mes_num - 1]}')
else:
    print('Error: el numero debe estar entre 1 y 12.')

print("\nPrograma terminado")