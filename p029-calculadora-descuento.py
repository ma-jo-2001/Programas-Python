# p029-calculadora-descuento.py
# Simular una calculadora de descuentos basada en el monto de compra

print("\033[2J\033[H", end="")
print("Simular una calculadora de descuento basada en el monto de compra\n")

compra = float(input("Total de comta ?"))
descuento = 0 
porcentaje = 0

if compra > 2000:
    porcentaje = 0.20
elif compra > 1000:
    porcentaje = 0.10
elif compra > 500:
    porcentaje = 0.05


descuento = compra * porcentaje
total = compra - descuento 

print("\nResumen de compra")
print(f"Total de compra : {compra:,.2f}")
print(f"Porcentaje de descuento : {porcentaje*100}%")
print(f"Descuento : {descuento:,.2f}")
print(f"Total a pagar : {total:,.2f}")