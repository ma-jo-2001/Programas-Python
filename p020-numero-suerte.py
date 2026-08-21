# p020-numero-suerte.py
# Programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos

print("\033[H\033[J", end="")
print("Calcular el numero de la suerte\n " )

# Solicitar el año de nacimiento 
ano_nacimiento = input("Ingresa el año de nacimiento (4 digitos)")

suma = 0

print("Digitos individuales")

for digito in ano_nacimiento:
    print(digito)
    suma += int(digito)

print("La suma de los digitos es:", suma)