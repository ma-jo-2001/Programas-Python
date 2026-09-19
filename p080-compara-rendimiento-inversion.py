# p080-compara-rendimiento-inversion.py
# # Comparar el rendimiento de dos fondos de inversión

print("\033[2J\033[H", end="")
print(f"Calcula el rendimiento de fondos de inversion\n")

print('Fondo de Inversión A')
capital_inicial_A = float(input('Monto inicial: '))
tasa_anual_A = float(input('Tasa de interés anual (%): '))

print('\nFondo de Inversión B')
capital_inicial_B = float(input('Monto inicial: '))
tasa_anual_B = float(input('Tasa de interés anual (%): '))

años_proyeccion = int(input('\nAños a proyectar: '))

print('\n   Comparación de rendimientos anuales    ')
print('Año |  Fondo A   |  Fondo B')
print('------------------')

valor_A = capital_inicial_A
valor_B = capital_inicial_B

for año in range(1, años_proyeccion + 1):
    valor_A = valor_A * (1 + tasa_anual_A / 100)
    valor_B = valor_B * (1 + tasa_anual_B / 100)
    print(f"{año:2d}  |  ${valor_A:8.2f}  |  ${valor_B:8.2f}")

print('\nResultado final:')

if valor_A > valor_B:
    print(f'El Fondo A (${valor_A:.2f}) superó al Fondo B (${valor_B:.2f}).')
elif valor_B > valor_A:
    print(f'El Fondo B (${valor_B:.2f}) superó al Fondo A (${valor_A:.2f}).')
else:
    print(f'Ambos fondos terminaron con el mismo valor: ${valor_A:.2f}.')

print("\nPrograma terminado")