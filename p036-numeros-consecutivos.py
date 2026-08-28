# p036-numeros-consecutivos.py
# Recibe tres numeros enteros y determina si son consecutivos

print("\033[2J\033[H", end="")
print("Recibe tres numeros enteros y determina si son consecutivos\n")

n1, n2, n3 = input().split()

n1, n2, n3 = int(n1), int(n2), int(n3)

if (
    (n2 == n1 + 1 and n3 == n2 + 1) or  # Orden: n1, n2, n3 (ej: 1, 2, 3)
    (n3 == n1 + 1 and n2 == n3 + 1) or  # Orden: n1, n3, n2 (ej: 1, 3, 2)
    (n1 == n2 + 1 and n3 == n1 + 1) or  # Orden: n2, n1, n3 (ej: 2, 1, 3)
    (n3 == n2 + 1 and n1 == n3 + 1) or  # Orden: n2, n3, n1 (ej: 3, 1, 2)
    (n1 == n3 + 1 and n2 == n1 + 1) or  # Orden: n3, n1, n2 (ej: 2, 3, 1)
    (n2 == n3 + 1 and n1 == n2 + 1)     # Orden: n3, n2, n1 (ej: 3, 2, 1)
):
    print("Los numeros son consecutivos")
else:
    print("Los numeros NO son consecutivos.")

print("\nEl programa finalizo")