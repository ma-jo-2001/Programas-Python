# p003-area-triangulo.py
# Calcular el area de un triangulo 

print("\033[2J\033[H", end="")

print("Calcula el area de un triangulo \n")

print("Dame la base y la altura del triangulo separadas por <enter>")
base, altura = int(input()), int(input())

area = (base * altura )/ 2

print(f"el triangulo de base {base} y altura {altura}, tiene un area de {area:.2f} ")
