# p025-verificar-suma.py
# DAdos tres numeros enteros verifica si la suma de los tres numeros enteros es igual al tercero
# 10 + 20 == 30 (son iguales) 5 + 8 == 5 (son iguales)

print("\033[2J\033[H", end="")
print("Dados tres numeros enteros verifica si la suma de los tres numeros enteros es igual al tercero \n")

n1 = int(input("Numero 1 ?"))
n2 = int(input("Numero 2 ?"))
n3 = int(input("Numero 3 ?"))

if n1 + n2 == n3:
    print(f"SON IGUALES {n1} + {n2} = {n3}")
else:
    print(f"NO SON IGUALES {n1} + {n2} = {n3}")

print ("\nFin del programa")