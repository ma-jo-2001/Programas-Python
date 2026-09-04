# p063-numero-mayor.py
# Programa que muestra una serie de numeros hasta que el usuario ingrese un 0

while True:
    print("\033[2J\033[H", end="")
    print("Introduce números (0 para terminar):")
    mayor = 0
    a = 0   # 0 = aún no hay numero, 1 = ya hay un numero

    while True:
        numero = int(input("> "))
        if numero == 0:
            break
        else:
            if a == 0:   # primer numero
                mayor = numero
                a = 1
            elif numero > mayor:
                mayor = numero

    print("--------------------")
    if a == 1:
        print(f"El numero mayor fue: {mayor}")
    else:
        print("No se introdujeron numeros.")

    if input("\n¿Desea continuar (S/N)? ").upper() == 'N':
        break

print("\nPrograma Terminado.")