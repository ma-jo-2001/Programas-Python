# p001-hola-mundo.py
# Lee datos y envia un saludo 

print("Leyendo datos y enviando un saludo")

# Leer datos 
print("\033[2J\033[H", end="") # Borrar la pantalla de la terminal

nombre = input("Dame tu nombre ? ")
edad = int(input("Dame la edad ? "))
peso = float(input("Dame el peso ? "))

print(f"{nombre}, bienvenido a python, tu edad {edad}, tu peso es {peso}")

print(nombre + "bienvenido a python, tu edad es " + str(edad), "tu peso es " + str(peso))
