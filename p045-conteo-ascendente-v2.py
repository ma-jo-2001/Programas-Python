# p045-conteo-ascendente-v2.py
# Imprimir numeros de 1 a n usando while

print("\033[2J\033[H", end="")
print("Imprimir numeros de 1 a 100 usando while\n")

n = int(input("Hasta donde ?"))
m = int(input("Incrementos ?"))

c = 1 
while c <= 10:
    print(f"{c}", end="")
    c += m

print("\n Proceso terminado: {c}")
