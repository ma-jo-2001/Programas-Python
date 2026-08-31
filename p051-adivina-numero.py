# p051-adivina-numero.py
# Permite adivinar un numero generado al azar entre 1 y 50

import random

print("\033[2J\033[H", end="")
print("Adivina el numero\n")
print("He pensado un numero entre 1 y 50, adivina cual es")

ns = random.randint(1,50)
ci = 0

while True: 
    intento = int(input("cual es ?"))
    ci += 1 
    if intento < ns : 
        print("Demasiado bajo intenta con un numero mas alto")
    elif intento > ns:
        print("Demasiado alto intenta con un numero mas bajo")
    else:
        print(f"Felicidades Adivinaste el numero en {ci} intentos")
        print("El numero era :", ns)

print("\n Terminamos Gracias")
