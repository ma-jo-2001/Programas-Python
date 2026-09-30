# p094-precio-acciones.py
# Analisis de precios de acciones diarias 
# Dame una lista de precios de cierre de una accion durante la semana.
# Encontrar el precio mas alto, el mas bajo, y el dia en que ocurrieron.

print("\033c", end="")
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
precios = [120.25, 152.30, 149.80, 151.00, 153.45, 154.10, 155.00]

precio_mas_alto = max(precios)
precio_mas_bajo = min(precios)
indice_mas_alto = precios.index(precio_mas_alto)
indice_mas_bajo = precios.index(precio_mas_bajo)

print("Analisis de precios de acciones:")
print(f"Precio mas alto: {precio_mas_alto} el dia {dias[indice_mas_alto]}")
print(f"Precio mas bajo: {precio_mas_bajo} el dia {dias[indice_mas_bajo]}")