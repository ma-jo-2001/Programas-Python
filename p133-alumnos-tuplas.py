# p133-alumnos-tuplas.py
# Registro de alumnos usano una tupla de tuplas 

# Creamos una tupla donde cada elemento es otra tupla que contiene los datos de cada estudiante
alumnos = (
    ("Ana", "ISC", 9, 10, 9),
    ("Luis", "ISC", 8, 9, 10),
    ("Maria", "ISC", 10, 8, 9)
)

# Imprime el total de calumnos
print("Registro de alumnos:")
print("Total de alumnos:", len(alumnos))

# Itera sobre la tupla de alumnos y calcula el promedio de califcaciones 
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre} - {carrera} - {calificaciones} : {promedio:,2f}")

# Imprime los datos del primer alumno usando indices
primer_alumno = alumnos[0]
print("\nDatos del primer alumno:")
print("Nombre:", primer_alumno[0])
print("Carrera:", primer_alumno[1])
print("Calificaciones:", primer_alumno[2])

# Creamos la tupla de promedios usando compresion de tuplas
promedios = tuple(
    (nombre, sum(notas) / len(notas)) for nombre, _, notas in alumnos
)

print("\nPromedios de los alumnos:", promedios)

# Crear tupla con nombres de los alumnos
# Usando compresion de lsitas
nombres = tuple(nombre for nombre, _, _ in alumnos)
print("\nNombres de los alumnos:", nombres)