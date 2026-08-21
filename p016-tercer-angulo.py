# p016-tercer-angulo.py
# Determina el tercer angulo de un triangulo 

# angulo3 = 180 – (angulo1 + angulo2)

print("\033[H\033[J", end="")
print("Calcular el tercer ángulo de un triángulo\n")

# Los dos angulos del triangulo 

angulo1 = float(input("Ingresa el primer angulo del triangulo (angulo1): "))
angulo2 = float(input("Ingresa el segundo angulo del triangulo (angulo 2): "))

angulo3 =180 - (angulo1 + angulo2)

print(f"El tercer angulo del triangulo es:", angulo3)