# p099-filtrar-pares.py
# Filtra los numeros para una lista de numeros introducidos usando compresion de listas 

print("\033c", end="")
print("\033[1;34m" + "Filtra numeros pares" + "\033[0m")

cant = int(input("Ingresa la cantidad de numeros a introducir: "))
numeros = []

# Se introducen los numeros en la lista
for i in range (cant):
    num = int(input(f"Ingresa el numero {i + 1}: "))
    numeros.append(num)

# Se filtran los numeros pares e impares usando compresion de listas 
pares = [x for x in numeros if x % 2 == 0] # Par
impares = [x for x in numeros if x % 2 != 0] # Impar

print("Los numeros introducidos son:", numeros)
print(f"Los numeros pares son: {pares} - Cantidad: {len(pares)}")
print(f"Los numeros impares son: {impares} - Cantidad: {len(impares)}")