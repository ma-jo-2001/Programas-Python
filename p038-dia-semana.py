# p038-dia-semana.py
# Dias de la semana 

print("\033[2J\033[H", end="")
print("Ingresa un numero del 1 al 7 donde 1 es domingo y 7 sabado\n")

numero = int(input())

if (numero == 1):
    print("Domingo")
elif (numero == 2):
        print("Lunes")
elif (numero == 3):
      print("Martes")
elif(numero == 4):
      print("Miercoles")
elif(numero == 5):
      print("Jueves")
elif(numero == 6):
      print("Viernes")
elif(numero == 7):
      print("Sabado")
else:
      print("ERROR. Dia invalido")

print("\nEl programa termino")