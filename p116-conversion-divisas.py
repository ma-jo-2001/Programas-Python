# p116-conversion-divisas.py
#Implementar un conversor de divisas a pesos mexicanos (MXN).
# Definir un diccionario conversiones con las fases de
# Cambio (e), EUR, USD, GBP, JPY, MXN.

# Borrar la consola 
print("\033c", end="")

# Definir el diccionario de conversiones 
conversiones = {
    "USD": 18.50, # 1 USD = 18.50 MXN
    "EUR": 20.00, # 1 EUR = 20.00 MXN 
    "GBP": 23.00, # 1 GBP = 23.00 MXN
    "JYP": 0.14,  # 1 JYP = 0.14 MXN
    "CAD": 14.00  # 1 CAD = 14.00 MXN
}

# Mostrar Opciones: Iterar sobre las llaves del diccionario para mostrar al usuario todas las monedas disponibles.

print("Opciones de divisas:")
for divisa in conversiones:
    print(f"- {divisa}")

# Solicitar al usuario que ingrese la cantidad y la divisa de origen y valida divisa valida 
cantidad = float(input("Ingresa la cantidad a convertir: "))
while True: 
    divisa_origen = input("Ingrese la divisa de origen (USD, EUR, GBP, JYP, CAD):").upper()
    if divisa_origen in conversiones:
        break
    else:
        print("Divisa de origen no valida. Intenete de nuevo.")

# Mostrar el resultado de la conversion a pesos mexicanos (MXN)
pesos_mxn = cantidad * conversiones[divisa_origen]
print("Resultado de la conversion:")
print(f"{cantidad} {divisa_origen} son {pesos_mxn:.2f} pesos mexicanos(MXN).")
