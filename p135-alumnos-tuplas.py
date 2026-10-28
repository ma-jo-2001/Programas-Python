# p135-alumnos-tuplas.py
# Representa los datos de alumnos usando tuplas 

# Registro escolar como tupla de alumnos
alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10))
)

# Crear y mostrar la tupla externa
print(f"Registros de alumnos: {alumnos}")
print(f"Total de alumnos: {len(alumnos)}")

# Recorrer mediante desempaquetado y mostrar promedio
print()
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

# Construir pares (nombre, promedio)
pares = tuple(
    (nombre, sum(calificaciones) / len(calificaciones))
    for nombre, carrera, calificaciones in alumnos
)
print(f"\nPares (nombre, promedio): {pares}")

# Identificar el alumno con el promedio más alto
mejor = max(pares, key=lambda par: par[1])
print(f"Alumno con mejor promedio: {mejor[0]} con {mejor[1]}")

# Consultar calificaciones con índices de tuplas anidadas
print()
for i in range(len(alumnos)):
    nombre = alumnos[i][0]
    calificaciones = alumnos[i][2]
    print(
        f"{nombre} -> Conteo de 10s: {calificaciones.count(10)}, "
        f"Índice de primera calificación: {calificaciones.index(10)}"
    )

# Ordenar por promedio de menor a mayor
ordenados = tuple(sorted(pares, key=lambda par: par[1]))
print(f"\nOrdenados por promedio: {ordenados}")

# Formar una nueva tupla con Eva, sin modificar la original
eva = ("Eva", "ISC", (9, 9, 10))
alumnos_con_eva = alumnos + (eva,)

print(f"\nTupla original intacta: {alumnos}")
print(f"Nueva tupla con Eva: {alumnos_con_eva}")