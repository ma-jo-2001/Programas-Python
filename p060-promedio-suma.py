# p060-promedio-suma.py
# # Programa que muestra la cantidad de numeros, la suma y el promedio de la serie hasta introducir 0.

while True:
    print("\033[2J\033[H", end="")
    print("Introduce numeros separados por un enter (0 para terminar):")
    conteo = 0
    suma = 0

    while True:
        numero = int(input("> "))

        if numero == 0:
            break
        else:
            conteo += 1
            suma += numero

    print("--------------------")
    if conteo > 0:
        promedio = suma / conteo
        print(f"Se introdujeron {conteo} numeros.")
        print(f"La suma es: {suma}")
        print(f"El promedio es: {promedio}")
    else:
        print("No se introdujeron numeros.")

    opcion = input("\n¿Deseas continuar (S/N)? ").upper()
    if opcion != "S":
        break

print("\nPrograma Terminado.")