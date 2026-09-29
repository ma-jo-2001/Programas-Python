# p089-eliminar-lista.py
# Eliminar elementos de una lista

print('\033[H\033[J')
print('Eliminar elementos de una lista:\n')

nums = [1, 3, 5, 7, 9, 11, 13, 15, 19]

print("\nLongitud y contenido de la lista de numeros:")
print(f'Contenido: {nums} - Longitud{len(nums)}\n')

print(f'Eliminar el 5 de la lista:')
nums.remove(5)
print(f'Contenido actualizado : {nums} | Longitud {len(nums)}\n')

print(f"Eliminar el elemento en la posición 3") 
del nums[3]
print(f"Contenido actualizado: {nums} | Longitud: {len(nums)}")

print("\nElimine el elemento en posicion de 8 usando pop()")
num = nums.pop(5)
print(f"Contenido actualizao: {nums} | Longitud: {len(nums)}")
print(f"Elemento elimindo: {num}")

print("\nElimine el elemento usando pop() sin parametros")
num = nums.pop()
print(f"elemento eliminado: {nums} | Contenido actualizado: (nums) | Longitud: {len(nums)} ")

print("\nElimine el elemento usando clear")
nums.clear()
print(f"Contenido actualizado: {nums} | Longitud {len(nums)}")