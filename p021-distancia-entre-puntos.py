# p021-distancia-entre-puntos.py
# Calcula la distancia entre dos puntos en un plano cartesiano 

import math as mt
print("\033[H\033[J", end="")
print("Calcular la distancia entre dos puntos en un plano cartesiano\n " )

# Formula distancia = √((x2 - x1)**2 + (y2 - y1)**2)

# Punto A (x1,y1)

x1 = float(input("Ingresa la cordenada x1 del punto A:"))
y1 = float(input("Ingresa la cordenada y1 del punto A:"))

# Punto B (x2,y2)

x2 = float(input("Ingresa la cordenada x2 del punto B:"))
y2 = float(input("Ingresa la cordenada y2 del punto B:"))

# Calcula la distancia 

distancia = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los puntos A y B es:", distancia)