# p015-hipotenusa-triangulo.py
#Calcular la longitud de la hipotenusa de un triangulo rectangulo 

import math as mt
print("\033[H\033[J", end="")
print("Calcular la longitud de la hipotenusa de un triangulo rectangulo\n")

# Hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

# Pedir la hipotenusa al usuario

Lado1 = float(input("Ingresa la longitud del primer cateto: ")) 
Lado2 = float(input("Ingresa la longitud del segundo cateto:"))

# Calcular la hipotenusa con la formula (hipotenusa = √a**2 + b**2)

hipotenusa = mt.sqrt(Lado1**2 + Lado2**2)

# Mostrar el resultado al usuario 
print("La longitud de la hipotenusa es:", hipotenusa)