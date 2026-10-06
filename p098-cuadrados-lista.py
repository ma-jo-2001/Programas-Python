# p098-cuadrados-lista.py
# Genera cuadrados usando conversion de listas 


print("\033c", end="")
print("\033[1;32m" + "Genera cuadrados usando conversion de listas" + "\033[0m")
print("Cuadrados de 1 a n usando compresion de listas")
n = int(input("Ingresa el valor de n:"))

numeros = list(range(1, n + 1))
cuadros = [x ** 2 for x in numeros] #Compresion de listas para calcular los cuadrados

print("Los numeros del 1 al", n, "son:", numeros)
print("Los cuadros del 1 al", n, "son:", cuadros)