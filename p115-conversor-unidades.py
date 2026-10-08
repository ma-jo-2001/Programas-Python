# p115-conversor-unidades.py
# Crear un conversor de undades de longitud 
# Definir un diccionario conversiones que almacene los
# factores para convertir "km", "m", "cm", y "mm" a metros.

# Borrar consola 
print("\033c", end="")

# Definir el diccionario de conversion 
conversiones = {
    "km": 1000.0, # 1 km = 1000 m
    "m": 1.0,     # 1 m = 1 m
    "cm": 0.01,   # 1 cm = 0.01 m
    "mm": 0.01,   # 1 mm = 0.01 m
}

# Solicitar al usuario que ingrese la cantidad y la unidad de origen y valida unidad valida 
cantidad = float(input("Ingrese la cantidad a convertir:"))
while True:
    unidad_origen = input("Ingrese la unidad de origen (km, m, cm, mm):").lower()
    break
print("Unidad de origen no valida. Intente nuevamente")

# Mostrar el resultado de la conversion en metros
metros = cantidad * conversiones[unidad_origen]
print(f"{cantidad} {unidad_origen} son {metros:.4f} metros.")