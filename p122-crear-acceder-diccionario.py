# p122-crear-acceder-diccionario.py
# Crear un diccionario para representar los dias de la semana 

print('\033[H\033[J')
print('Accediendo a elementos de un diccionario\n')

# Crear el diccionario de días de la semana
dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miercoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sabado',
    7: 'Domingo'
}

# Mostrar el diccionario inicial
print(f'Diccionario inicial: \n{dias} - {len(dias)}\n')
print(dias)

# Acceder a elementos específicos
print("\nAccediendo a elementos:")
print("Llave 1 (con []):", dias[1])
print("Llave 7 (con []):", dias[7])
print("Llave 5 (con get()):", dias.get(5))
print("Llave 7 (con get()):", dias.get(7))

# Mostrar el diccionario final
print("\nDiccionario final:")
print(dias)