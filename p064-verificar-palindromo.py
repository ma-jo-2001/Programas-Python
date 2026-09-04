# p064-verificar-palindromo.py
# Solicita un numero entero y determina si es un palindromo

print("\033[2J\033[H", end="")
print("Verificar si un numero es palindromo\n")

while True:
    numero = input("Introduce un numero para verificar si es palindromo: ")

    n_invertido = ""
    n_recorrido = ""
    i = 0

    while n_recorrido != numero:
        caracter = numero[i]
        n_recorrido += caracter
        n_invertido = caracter + n_invertido
        i += 1

    if numero == n_invertido:
        print(f"El numero {numero} es un palindromo.")
    else:
        print(f"El numero {numero} no es un palindromo.")

    if input("\n¿Desea continuar (S/N)? ").upper() == 'N':
        break

print("\nPrograma Terminado.")