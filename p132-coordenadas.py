# p132-coordenadas.py
# Registro de coordenadas georaficas usando tuplas 

# Definicion de las tuplas para las coordenadas de dos ciudades
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

# Imprime los datos de las coordenadas de Zacatecas
print("Coordenadas de Zacatecas:")
print("Tipo:", type(zacatecas))
print("Ciudad: ", zacatecas[0])
print("Latitud: ", zacatecas[1])
print("Longitud: ", zacatecas[2])

# Imrime los datos de las coordenadas de Guadalupe 
ciudad, latitud, longitud = guadalupe 
print("Coordenadas de Guadalupe:")
print("Tipo:", type(guadalupe))
print("Ciudad: ", guadalupe[0])
print("Latitud: ", guadalupe[1])
print("Longitud: ", guadalupe[2])

# Itera sobre las tuplas de coordenadas y las imprime 
for lugar in [zacatecas, guadalupe]:
    print("\nCoordenadas de", lugar[0])
    print("Latitud:", lugar[1])
    print("Longitud:", lugar[2])

# Desempaquetado ignora el primer elemento (nombre de la ciudad) y obtiene las coordenadas    
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Calculo del punto medio entre las dos coordenadas
centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print("Punto medio", centro)

# Verificar pertenencia 
print("Zacatecas pertenece a la tupla:", "Zacatecas" in zacatecas)

# Crear otra tupla con datos extra 
ampliada = zacatecas + ("Mexico",)

print("Tupla original: ", zacatecas)
print("Tupla ampliada: ", ampliada)