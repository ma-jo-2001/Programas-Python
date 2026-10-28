# p134-coordenadas-
# Representa las coordenadas geograficas de dos ciudades usando tuplas

# Crear las tuplas de las ciudades
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")

# Acceso por índices positivos y negativos
print("\nAcceso por índices (Zacatecas):")
print(f"Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}")
print(f"Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}")

# Desempaquetar cada tupla
nombre_z, lat_z, lon_z = zacatecas
nombre_g, lat_g, lon_g = guadalupe

print(f"\n{nombre_z}: ({lat_z}, {lon_z})")
print(f"{nombre_g}: ({lat_g}, {lon_g})")

# Recorrer ambas ubicaciones y usar slicing
for ubicacion in (zacatecas, guadalupe):
    nombre = ubicacion[0]
    coordenadas = ubicacion[1:3]
    print(f"Ubicación: {nombre}, Coordenadas: {coordenadas}")

# Calcular el punto medio aproximado
lat_media = (lat_z + lat_g) / 2
lon_media = (lon_z + lon_g) / 2
print(f"\nPunto medio aproximado: ({lat_media}, {lon_media})")

# Crear una nueva tupla con el código, sin modificar la original
zacatecas_codigo = zacatecas + ("ZAC",)
print(f"\nNueva tupla Zacatecas: {zacatecas_codigo}")
print(f"Original sin cambios: {zacatecas}")

# Verificar si "Zacatecas" pertenece a la tupla
print(f"\n'Zacatecas' pertenece a la tupla: {'Zacatecas' in zacatecas}")

# Nota: Intentar modificar un elemento directamente arroja TypeError (las tuplas son inmutables).
# Ejemplo: zacatecas[0] = "Otra ciudad"  # TypeError: 'tuple' object does not support item assignment