# p018-area-volumen-cilindro.py
# Calcula el area y el volumen de un cilindro a partir de su radio y altura 

import math as mt
print("\033[H\033[J", end="")
print("Calcular el area y el volumen de un cilindro\n " )

# Formula Area = 2 π (R + h)
# Volumen = π * R**2 * h

radio = float(input("Ingresa el radio del circulo (R)"))
altura = float(input("Ingresa la altura del cilindro (h)"))

area = 2 * mt.pi * (radio + altura)
volumen = mt.pi * (radio ** 2) * altura

print("El area del cilindro es:", area)
print("El volumen del cilindro es:", volumen)