# p042-precio-entrada-cine.py
# Determina el precio de una entrada segun la edad del cliente

print("\033[2J\033[H", end="")
print("Taquilla de cine\n")

edad = int(input("Ingresa su edad:"))

if edad < 5:
    precio = 0
    categoria = "Menores de 5 años"
elif 5 <= edad <= 12:
    precio = 5
    categoria = "Niño (5 a 12 años)"
elif 13 <= edad <= 64:
    precio = 10
    categoria = "Adulto (13 a 64 años)"
else:  # 65 años o más
    precio = 7
    categoria = "Tercera edad (65 años o más)"

print("\n--- Ticket de Entrada ---")
print(f"Categoría: {categoria}")
if precio == 0:
    print("Precio: ¡Entras gratis!")
else:
    print(f"Precio a pagar: ${precio}")

print("\nPrograma terminado")