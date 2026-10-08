# p117-punto-de-venta.py
# Crear un sistema simple de punto de venta (POS) para un puesto de comida

# Crear un sistema simple de punto de venta (POS) para un puesto de comida
comida = {
    "Hamburguesa": 5.0,
    "Papas fritas":2.5,
    "Refesco": 1.5, 
    "Pizza": 8.0,
}

# Mostrar Menu: Mostrar al usuario los productos disponibles y sus precios, interandose sobre el diccionario
print("\033c", end="")
print("Menu de productos:")
for producto, precio in comida.items():
    print(f"- {producto}: ${precio:.2f}")

# Tomar orden: Preguntar al usuario que desea ordenar en un bucle. 
orden = {}
while True:
    producto = input("Ingrese el producto que desea ordenar (o presione <enter> para salir):")
    if producto == "":
        break
    if producto in orden:
        orden[producto] += cantidad
    else:
        orden[producto] = cantidad
        continue
    cantidad = int(input(f"Ingrese la cantidad de {producto}:"))
    if producto in orden:
        orden[producto] += cantidad
    else:
        orden[producto] = cantidad

# Mostrar un recibo con el subtotal por producto y el total general de la compra.
total_general = 0
for producto, cantidad in orden.items():
    subtotal = comida[producto] * cantidad
    total_general += subtotal
    print(f"- {producto} x {cantidad}: ${subtotal:.2f}")
print(f"Total general: ${total_general:.2f}")