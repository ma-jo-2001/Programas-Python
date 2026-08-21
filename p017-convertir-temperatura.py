# p017-convertir-temperatura.py
# convertir la tenperatura de grados Celsius a grados Fahrenheit 

import math as mt
print("\033[H\033[J", end="")
print("Convertir la tempertura de grados Celcius a grados Fahrenheit")

# Formula farenheit = (celcius × 9/5) + 32
celcius = float(input("Ingresa la temperatura en grados Celcius"))
fahrenheit = (celcius * 9/5) + 32

print(f"\nLa temperatura de {celcius:.2f} grados Celcius, equivale a {fahrenheit:.2f} grados Fahrenheit")

      