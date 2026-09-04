# p058-impares-ascendente.py
# Imprime numeros impares y suma total en un rango ascendente de 1 hasta n

print("\033[2J\033[H", end="")
print("Imprime numeros impares y suma total\n")

while True:
    n = int(input("Ingresa un numero limite:"))

    i = 1
    suma = 0
    impares = []

    while i <= n:
        if i % 2 != 0: #Si es impar 
            print(i)
            suma += i
            impares.append(str(i))
        else:
            suma = suma
            i += 1
    print(f"\nNumeros impares: {", ".join(impares)}")
    print(f"Suma total de los numeros impares: {suma}\n")

    opcion = input("Deseas continuar (S/N)?").strip().upper()
    if opcion != "S":
        break

print("\nPrograma Terminado.")