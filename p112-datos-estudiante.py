# p112-datos-estudiante.py
# Gestion de datos de un estudiante con un diccionario

# Borrar la consola
print("\033c", end="")

# Crear un diccionario para almacenar los datos del estudiante
estudiante = {
    "nombre": "Juan Perez",
    "edad": 20,
    "carrera": "Ingenieria de sistemas",
    "email": "juan.perez@universidad.edu.com"
}

print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Modificar un dato del estudiante 
estudiante["edad"] = 21
estudiante["email"] = "juanito@gmail.com"

print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Agregar un nuevo dato al estudiante 
estudiante["promedio"] = 8.5
print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Mostrar las llaves del diccionario 
print("Las llaves son:")
for value in estudiante.values():
    print(f"- {value}")

# Mostrar las llaves y valores del diccionario 
print("Las llaves y valoresson:")
for key, value in estudiante.items():
    print(f"- {key}: {value}")