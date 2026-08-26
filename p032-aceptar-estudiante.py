# p032-aceptar-estudiante.py
# Aseptar estudianes en base a edad y calificaciones  (Usando AND)
# Las condiciones edad >= 18 y c1 y c2 >= 8

print("\033[2J\033[H", end="")
print("Aseptar estudianes en base a edad y calificaciones (usando AND) \n")

nombre = input("Dame tu nombre ?")
edad = int(input("dame tu edad ?"))

if edad >= 18: 
    print("\nContinuamos con el proceso ..")
    print("Dame tus dos calificaciones separadas por Enter ?")
    c1 = float(input())
    c2 = float(input())
    if c1 >= 8 or c2 >= 8:
        print(f"{nombre} Bienvenido a la Universidad ")
    else: 
        print(f"\n{nombre}, no aceptamos calificaciones menores a 8 ..")
else:
    print(f"\n{nombre} , no aceptamos menorses de edad ..")

    print(" \n Proceso terminado")
