# p103-resumen-ventas.py
# Transforma y filtra ventas con compresion de listas

print("\033c", end="")
print("\033[1;34m" + "Resumen de ventas" + "\033[0m")

ventas = [1000, 2000, 3000, 4000, 5000]

# Ventas mayores a 1000 aplica 10% de descuento, menores a 1000 aplica 5% de descuento 
ventas_descuento = [v * 0.9 if v >= 1000 else v * 0.95 for v in ventas]

# Saques ventas relevantes si son mayores a 1000
ventas_relevantes = [v for v in ventas if v >= 1000]

print("Ventas:", ventas)
print("Ventas con descuento:", ventas_descuento)
print("Ventas relevantes (mayores a 1000):", ventas_relevantes)