# p092-procesar-calificaciones.py
# Procesa n calificaciones entre 1 y 10 en una lista hasta introducir 999
# Al fianl muestra: la lista, suma, promedio, la mas alta y las mas baja.
# cuantos alumnos mayores al promedio
# Valida que no introduzca letras en lugar de numeros 

calificaciones = []
suma = 0
# Borrar la consola para que se vea mas limpio 
print("\033c", end="")
while True:
    try:
        calificacion = float(input("Ingrese una calificacion entre 1 y 10 (o 999 para terminar):"))
        if calificacion == 999:
            break
        elif 1 <= calificacion <= 10:
            calificaciones.append(calificacion)
            suma += calificacion
        else:
            print("Calificacion invalida. Debe estar entre 1 y 10.")
    except ValueError:
        print("Entrada invalida. Por favor, ingrese un numero.")

if calificaciones:
    promedio = suma / len(calificaciones)
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)
    alumnos_mayores_promedio = sum(1 for cal in calificaciones if cal >promedio)

    print("\nResultados:")
    print(f"Lita de calificaciones:{calificaciones}")
    print(f"Suma de calificaciones: {suma}")
    print(f"Promedio de calificaciones: {promedio}")
    print(f"Calificacion mas alta: {calificacion_mas_alta}")
    print(f"Calificacion mas baja: {calificacion_mas_baja}")
    print(f"Numero de alumnos con calificacion mayor al promedio: {alumnos_mayores_promedio}")