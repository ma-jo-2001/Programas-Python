# p059-pares-descendente.py
#  Imprimir numeros pares y suma total en un rango descendente de 100 - n

while True:
    print("\033[2J\033[H", end="")
    n=int(input("Ingresa un numero limite (menor o igual a 100):"))

    i = 100
    suma = 0 
    contador = 0
    print("\nNumeros pares:", end="")

    while i >= n:
        if i % 2 == 0:
            print(i, end="")
            suma += i
            contador += 1

            if i - 2 >= n:
                print(", ", end="")

        i -= 1

    print(f"\nSuma total de los numeros pares: {suma}")

    opcion = input("Deseas continuar (S/N)?").strip().upper()
    if opcion != "S":
        break

print("\nPrograma Terminado.")