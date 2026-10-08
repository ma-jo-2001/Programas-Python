# p114-nombres-edades.py
# Censo de nombres y edades en un diccionario, hasta <enter> vacio 

# Borrar la consola
print("\033c", end="")

# Crear un diccionario para almacenar los nombres y edades 
censo = {}

# solicitar al usuario que ingrese nombres y edades hasta que ingrese un nombre vacio 
while True:
    nombre = input("Ingrese un nombre (o presione <enter> para salir):")
    if nombre == "":
        break
    censo[nombre] = int(input(f"Ingrese la edad de {nombre}:"))

# Mostrar el censo de nombres y edades 
print(f"Censo de nombres y edades: {censo} - {len(censo)} elementos")

#Resumen del censo 
print("Resumen del censo:")
for nombre, edad in censo.items():
    print(f"- {nombre}: {edad} años")

print()

suma_edades = sum(censo.values()) # sumar todas las edades 
promedio_edades = suma_edades / len(censo) if censo else 0 # promedio de edades, evitando desviacion por cero }
print(f"Suma de edades: {suma_edades} años")
print(f"Promedio de edades: {promedio_edades:.2f} años")