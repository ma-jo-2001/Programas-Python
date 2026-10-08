# p113-calificaciones-estudiante.py
# procesar calificaciones de un estudiante con un diccionario 

# Borrar la consola
print("\033c", end="")

# Crear dos listas, una de materias otra de calificaciones 
materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
calificaciones = [8.5, 9.0, 7.0, 6.5, 9.5]

# Crear un diccionario para almacenar las calificaciones del estudiante
calificaciones_estudiante = dict(zip(materias, calificaciones))
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Mostrar las calificaciones del estudiante 
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Agregar dos nuevas calificaciones al estudiante 
calificaciones_estudiante["Educacion fisica"] = 10.0
calificaciones_estudiante["Arte"] = 9.0

# Actualizar 3 calificaciones del estudiante
calificaciones_estudiante["Matematicas"] = 9.0 
calificaciones_estudiante["Fisica"] = 8.5
calificaciones_estudiante["Historia"] = 7.0

print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Elimina 2 calificaciones del estudiante usando pop 
calificaciones_estudiante.pop("Quimica")
calificaciones_estudiante.pop("Lengua")
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Mostrar el par llave-valor de las calificaciones del estudiante, y promedio de calificaciones 
print("Las llaves y valores son:")
total = 0
for materia, calificacion in calificaciones_estudiante.items():
    print(f" - {materias}: {calificaciones}")
    total += calificacion 
promedio = total / len(calificaciones_estudiante)
print(f"Promedio de calificaciones: {promedio:.2f}")