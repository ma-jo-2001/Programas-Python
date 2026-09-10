# p068-conteo-descendente-for-v2.py
#  Imprime numeros de n a 1 en intervalos de m usando for 

print("\033[2J\033[H", end="")
print("Imprimir los numeros del n al 1 en intervalos de m usando for\n")

n = int(input("Desde donde ?"))
m = int(input("Intervalo ?"))

for i in range(n, 0, -m):
    print(i)

print("\n Proceso terminado", i)