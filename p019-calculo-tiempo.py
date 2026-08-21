# p019-calculo-tiempo.py
# Calcula el tiempo en dias, minutos y segundos a partir de un tiempo en horas

import math as mt
print("\033[H\033[J", end="")
print("Calcular el tiempo en dias, minutos y segundos\n " )

# Días (considerando que 1 día tiene 24 horas)
# Minutos (considerando que 1 hora tiene 60 minutos)
# Segundos (considerando que 1 minuto tiene 60 segundos)

horas = int(input("Ingresa la cantidad de horas (numero entero)"))

dias = horas // 24
minutos = horas * 60
segundos = horas * 3600

print("Equibalencia del tiempo ingresado:")
print("Dias:", dias)
print("Minutos:", minutos)
print("Segundos:", segundos)

