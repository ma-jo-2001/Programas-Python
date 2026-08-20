#p009-promedio-de-calificaciones.py
# Calcula el promedio de tres calificaciones ingresados por el usuario

print("\033[2J\033[H", end="")
print("Calculando el promedio de tres calificaciones\n")

# Entrada 
print("Dame tres calificaciones separadas por espacios\n")
cal1, cal2, cal3 = input().split()
#print(type(cal1), type(cal2), type(cal3))
cal1, cal2, cal3, =float(cal1), float(cal2), float(cal3)
#print(type(cal1), type(cal2), type(cal3))

# Proceso
suma = cal1 + cal2 +cal3 
promedio = suma / 3

# Salida 
print()
print(f"Las calificaciones son   : {cal1}, {cal2}, {cal3}")
print(f"La suma  es   : {suma:.2f}, \n y el promedio es {promedio:.2f}")
