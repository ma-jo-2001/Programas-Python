# p126-procesar-diccionario.py
# Procesar un diccionario generado a partir de dos listas

print('\033[H\033[J')
print('Procesar un diccionario (Nomina de empleados)\n')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print(f'Diccionario nomina:\n{nomina} - len: {len(nomina)}\n')

print('--- Llaves del diccionario ---')
for llave in nomina.keys():
    print(llave)
print()

print('--- Valores del diccionario ---')
for valor in nomina.values():
    print(valor)
print()

print('--- Iterar por llaves accediendo al valor ---')
for nombre in nomina:
    print(f'{nombre:<10} : {nomina[nombre]:>10.2f}')
print()

print('--- Llave y valor (usando items()) ---')
for nombre, sueldo in nomina.items():
    print(f'{nombre:<10} : {sueldo:>10.2f}')
print()

suma = sum(nomina.values())
promedio = suma / len(nomina)

print('-' * 50)
print(f'Suma : {suma:,.2f}, Promedio {promedio:,.2f}')
print('-' * 50)
