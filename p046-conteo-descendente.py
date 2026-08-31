# p046-conteo-descendente.py
# Imprimir los numeros de 100 a 1

print("\033[2J\033[H", end="")
print("Imprimir los numeros de 100 a 1\n")

c = 100

while c >= 1:
    print(f"{c}", end="")
    c-=1

print("\n Proceso terminado", c)