# p102-aplanar-matriz.py
# Aplana una matriz de 2 dimenciones a una lista de 1 dimension usando compresion de listas

print("\033c", end="")
print("\033[1;34m" + "Aplanar matriz" + "\033[0m")

matriz = [[1, 2, 3], [-4, 5, 6], [-7, 8, 9]]

# Se aplana la matriz unsando compresion de listas 
aplanada = [elemento for fila in matriz for elemento in fila]
positivos = [elemento for fila in matriz for elemento in fila if elemento > 0]
negativos = [elemento for fila in matriz for elemento in fila if elemento < 0]

print("Matriz original:", matriz)
print("Matriz aplanada:", aplanada)
print("Elementos positivos:", positivos)
print("Elementos negativos:", negativos)