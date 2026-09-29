# p086-acceder-lista.py
# Acceder a elementos de una lista

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\033[H\033[J')

print('Acceder a los elementos de una lista\n')

print('\nLongitud y contenido de las mediciones:')
print(f'Longitud: {len(nums)}')
print(f'Contenido   : {nums}')

print('\nPor índice positivo:')
print(f"elementos en el indice 0 y 8: {nums[0]} - {nums[8]}")

print('\nPor índice negativo:')
print(f"elementos en el indice -8 y -1: {nums[-8]} - {nums[-1]}")

print("\nPor rango")
print("\nDe 2 al 6 {sin incluir el 6}:")
print(f"Elementos: {nums[2:6]}")

print("\nPor saltos:")
print(f"Elementos con saltos de 2:{nums[::2]}")
print(f"Elementos con saltos de 3:{nums[::3]}")
