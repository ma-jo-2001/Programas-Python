# p090-iterar-lista.py
# Iterar por los elementos de una lista

print('\033[H\033[J')

print('Iterar sonre una lista: {nums}| Longitud: {len(nums)} \n')

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print(f'Números a procesar: {nums} - {len(nums)}\n')

# Interar por elemento
print('Iteración por elemento:')
for n in nums:
    print(n, end=' ')

# Interar por indice
print('\n\nIteración por indice de cada elemento:')
for i in range(len(nums)):
    print(f"Indice {i}: {nums[i]}")

# Interar por elemento de suma 2 
print('\n\n Iteración por elemento para sumar 2')
for n in nums:  
    print(n + 2, end=' ')

# Interar por elemento sumando 10
print('\n\n4. Iteración por índice para sumar 10')
for i in range(len(nums)):
    print(nums[i]+10, end=' ')

# Interar por enumerate 
print('\n\n5. Iteración con enumerate')
for i, n in enumerate(nums):
    print(i,'\t', n,)

#Elevar al cuadrado cada elemento y guardar el resultado en la lista original
original = nums.copy()
print("\nElevar al cuadrado cada elemento:")
print(f"Lista original: {original}")
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print(f"lista con los elementos al cuadrado: {nums}")