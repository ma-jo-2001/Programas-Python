# p069-arriba-abajo.py 
# Imprime numeros de 1 a n o de n a 1 segun lo decidas

print("\033[2J\033[H", end="")
print("Imprimir numeros de 1 a n o de n a 1 segun lo decidas\n")
print("[1] Voy de 1 a n")
print("[2] Voy de n a 1")
op = int(input("Elige ?"))

if op == 1:
    print("\nVamos hacia arriba de 1 a n")
    n = int(input("Hasta donde ?"))
    for x in range(1, n + 1):
        print(f"{x}", end="")
elif op == 2:
    print("\nVamos hacia abajo de n a 1")
    n = int(input("Desde donde ?"))
    for x in range(n, 0, -1):
        print(f"{x}", end="")
else:
    print("\nOpcion erronea")

print("\n Proceso terminado", x)