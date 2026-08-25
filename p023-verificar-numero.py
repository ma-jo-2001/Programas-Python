# p023-verificar-numero.py
# Verificar si el numero entro es positivo, negativo o cero

print("\033[2J\033[H", end="")
print("Verificar si el numero entro es positivo, negativo o cero\n")

numero = int(input("Dame un numero entero"))

if numero > 0:
    print("El numero es positivo 👆")

else:
    if numero < 0:
        print("El numero es negativo 👇")
    else:
        print("El numero es cero 🤷‍♀️")

print("\nAqui termina la decision")
 
