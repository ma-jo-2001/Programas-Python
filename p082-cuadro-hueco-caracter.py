# p082-cuadro-hueco-caracter.py
# Dibujar un cuadrado hueco con el caracter indicado

print("\033[2J\033[H", end="")
print(f"Dibujar un cuadrado hueco con el caracter indicado\n")

tamaño_lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
simbolo = input("¿Qué caracter quieres usar? ")

for fila_actual in range(1, tamaño_lado + 1):
    for columna_actual in range(1, tamaño_lado + 1):
        if fila_actual == 1 or fila_actual == tamaño_lado or columna_actual == 1 or columna_actual == tamaño_lado:
            print(simbolo, end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nPrograma terminado")