# p002-area-circulo.py
# Calcula el area de un circulo 

import math # importa la libreria de constances y funciones matematicas 

print("\033[2J\033[H", end="") # Borrar la pantalla de la terminal
print("Calculando el area de un circulo \n")

radio = float(input("Dame el radio ?"))

area = math.pi * radio ** 2
area = math.pi * math.pow(radio, 2)

print(f"El circulo de radio {radio}, tiene un area de {area:.2f}")