# p081-plan-ahorro-depistos-mensuales.py
# Simular un plan de ahorro mensual

print("\033[2J\033[H", end="")
print(f"Simular un plan de ahorro mensual\n")

print('Monto inicial de ahorro:', end=' ')
capital_inicial = float(input())

print('Depósito mensual:', end=' ')
aporte_mensual = float(input())

print('Tasa de interés mensual (%):', end=' ')
tasa_mensual = float(input())

print('Número de meses a simular:', end=' ')
total_meses = int(input())

print('\n    Plan de ahorro detallado    ')

saldo_actual = capital_inicial

for mes in range(1, total_meses + 1):
    interes_generado = saldo_actual * (tasa_mensual / 100)
    saldo_final = saldo_actual + interes_generado + aporte_mensual
    print(f'Mes {mes}: Saldo Inicial: ${saldo_actual:7.2f} | Interés: ${interes_generado:5.2f} | Saldo Final: ${saldo_final:7.2f}')
    saldo_actual = saldo_final

print(f'\nAl final de {total_meses} meses, tendrás ${saldo_actual:.2f}')
print("\nPrograma terminado")

print("\033[2J\033[H", end="")
print(f"Calcula el rendimiento de fondos de inversion\n")