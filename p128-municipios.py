# p128-municipios.py
# Gestion de un padron de municipal usando conjuntos

municipios = {"Zacatecas", "Fresnillo", "Jerez", "Guadalupe", "Sombrerete", "Fresnillo"}

# Borrar pantalla 
print('\033[H\033[J')

print("Padron de municipios")
print("--------------------")
print("Municipios registrados:")
print(type(municipios))
for municipio in municipios:
    print(municipio)
# Consultar si un municipio esta regitrado 
print("\nEsta Zacatecas dentro de los Municipios registrados?", "Zacatecas" in municipios)

# Altas al padron de municipios 
print("Agregando un municipio al padron ")
municipios.add("Calera")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# agregar varios municipios al padron 
print(f"Agregando varios municipios al padron ")
otros = {"Concepcion del Oro", "Jalpa", "Villanueva"}
municipios.update(otros)
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con remove 
print("\nEliminando un municipio del padron")
municipios.discard("Sombrerete")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con discard
print("\nEliminar un municipio del padron")
municipios.discard("Sombrerete")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con pop
print("\nEliminar un municipio del padron")
municipio_eliminado = municipios.pop("Fresnillo")
print(f"Municipio eliminado: {municipio_eliminado}")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar  todos los municipios del padron
print("\nEliminando todos los municipios del padron")
municipios.clear()
print(f"Municipios registrados: {municipios} - {len(municipios)}")