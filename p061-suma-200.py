# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor que 200

print("\033[2J\033[H", end="")
print("Leer números y sumarlos hasta que el total acumulado sea mayor que 200\n")

while True:
    suma = 0
    conteo = 0

    while suma < 200:
        print(f"Suma actual: {suma}. ", end="")
        numero = int(input("Introduce un numero: "))
        suma += numero
        conteo += 1

    print("---")
    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de numeros introducidos: {conteo}")

    opcion = input("\n¿Desea continuar (S/N)? ").upper() == 'N'

    if opcion != "S":
        break

print("\nPrograma Terminado.")