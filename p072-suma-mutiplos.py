# p072-suma-mutiplos.py
# Imprime numeros de 1 a n, solo los multiplos de m

print("\033[2J\033[H", end="")
print("Imprimir los numeros del 1 a n, solo los multiplos de m\n")

m = int(input("Que multiplos quieres ?"))
n = int(input("Iniciando en 1 hasta donde ? "))

c = s = 0 

for i in range(1, n + 1):
    if i % m == 0:
        print(f"{i}", end="")
        c += 1
        s += 1

print(f"\n\nCuantos multiplos fueron {c}")
print(f"Suma de los multiplos de {m} = {c}")
