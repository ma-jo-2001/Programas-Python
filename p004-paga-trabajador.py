# p004-paga-trabajador.py
# Calcular la paga de un trabajador 

print("\033[2J\033[H", end="")
print("Calculando la paga de un trbajador \n")

# Entrada 
nombre = input("Dame tu nombre ? ")
horas = int(input("Horas ? "))
paga = float(input("Paga ? "))

# Proceso 
tasa = 0.03
pagabruta = horas * paga 
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto 

# salida 
print("resumen de pagos \n")
print(f"El trabajador {nombre}, trabajo {horas} horas, a una paga de {paga} pesos")
print(f"Paga Bruta : {pagabruta:>10,.2f}")
print(f"impuesto : {impuesto:>10.2f}")
print(f"Paga Neta : {paganeta:>10,.2f}")