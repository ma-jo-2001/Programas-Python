# p118-lote-autos.py
# Crear una lista de diccionario para almacenar los datos de varios autos

autos = [ 
    {"marca": "Toyota", "Modelo": " Camry", "Año": 2020, "precio": 25000},
    {"marca": "Honda", "Modelo": "Civic", "Año": 2019, "precio": 22000},
    {"marca": "Ford", "Modelo": "Focus", "Año": 2021, "precio": 23000}
]

autos.append({"marca":"Chevrolet", "modelo": "Malibu", "año": 2022, "precio": 27000})

# Borrar pantalla de la consola 
print("\033c", end="")

# Mostrar los datos de cada auto en la lista
print(f"\nTodos los autos: {autos} - {len(autos)} elementos")
print("\nDatos de cada auto:")
for auto in autos:
    print(auto)
    print()

# Mostrar los datos en forma de tabla 
print("\nDatos de los autos en forma de tabla:")
for k in autos[0].keys():
    print(f"{k:<10}")
print()
for auto in autos: 
    for v in auto.values():
        print(f"{v:<10}", end="")
    print()

# Mostrar los datos en forma de registro 
print("\nDatos de los autos en forma de registro:")
for auto in autos:
    for k, v in auto.items():
        print(f"{k}: {v}:")
    print()