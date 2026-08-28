# p043-calculadora-anio-bisiesto.py
# Determina si el año es bisiesto

print("\033[2J\033[H", end="")
print("Verificador de años bisiestos\n")

an = int(input("Ingresa un año"))

# Es divisible por 4, pero no es divisible por 100.
# Es divisible por 400.

if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print(f"El año {an} es bisiesto ")
else:
    print(f"El año {an} no es bisiesto ")

print("\nPrograma terminado")