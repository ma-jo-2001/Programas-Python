# p095-registro-estudiantes.py
"""""Planteamiento del problema: Registro de estudiantes para evento
• Se está organizando un evento y necesitas registrar a los asistentes.
• El programa debe permitir al usuario introducir el nombre y la edad de cada
persona.
• El registro termina cuando se introduce un * como nombre.
• Al finalizar, el sistema debe mostrar dos informes:
• una lista de todos los asistentes que son mayores de edad (18 años o más).
• y el nombre y la edad de la persona con mayor edad para entregarle un reconocimiento."""

print("\033c", end="") # Esto limpia la consola en sistemas compatibles 
nombres = []
edades = []
# Bucle para registrar asistentes, se detiene cuando se introduce "*" como nombre
while True:
    nombre = input("Ingrese el nombre del asistente (o "*" para terminar):")
    if nombre == "*":
        break
    try: # Validar que la edad sea un numero entero positivo 
        edad = int(input(f"Ingrese la edad de {nombre}:"))
        if edad < 0 :
            print("Edad invalida. Debe ser un numero positivo.")
            continue # si la edad es negativa, se solicita nuevamente el nombre y la edad 
        nombres.append(nombre)
        edades.append(edad)
    except ValueError: # Captura el error si la entrada no es un numero entero 
        print("Entrada invalida. Por favor, ingrese un numero entero en la edad.")

if nombres:
    # Filtrar asistentes mayores de edad 
    for i in range(len(edades)):
        if edades [i] >= 18:
            print(f"{nombres[i]} es mayor de edad con {edades[i]} años.")
    # Encontrar la persona con mayor edad 
    max_edad = max(edades)
    indice_max_edad =edades.index(max_edad)
    print(f"La persona con mayor edad es {nombres[indice_max_edad]} con {edades[indice_max_edad]} años.")