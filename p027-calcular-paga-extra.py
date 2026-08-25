# p027-calcular-paga-extra.py
#Calcula la paga de un trabajador considerando horas extra

print("\033[2J\033[H", end="")
print("Calcula la paga de un trabajador considerando horas extra\n")

print("Dame tus datos")
nombre = input("Nombre :")
horas = int(input("Horas :"))
pago_hora = float(input("Pago x hora:"))

horas_extra = paga_extra = 0

if horas > 40:
    paga_normal = 40 * pago_hora
    horas_extra = horas - 40
    paga_extra = horas_extra * (pago_hora*2)
else:
    paga_normal = horas * pago_hora

total = paga_normal + paga_extra

print("Calculo de pagos")
print(f"El trabajador {nombre} trabajo {horas} horas a una paga de {pago_hora}")
print(f"Horas normal: {paga_normal}")
print(f"Horas extra: {horas_extra}")
print(f"Paga extra: {paga_extra}")
print(f"Total. : {total}")

print("\nPrograma finalizado")