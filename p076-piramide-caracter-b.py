# p076-piramide-caracter-b.py
# Imprime piramide de caracteres
print("\033[2J\033[H", end="")
print("Imprime piramide de caracteres\n")

altura = 5
c = "*"
espacios = caracteres = 0

for i in range(1, altura+1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(" ", end=" ")
    for j in range(caracteres):
        print(c, end=" ")
    print()

for i in range(altura - 1, 0, -1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(" ", end=" ")
    for j in range(caracteres):
        print(c, end=" ")
    print()