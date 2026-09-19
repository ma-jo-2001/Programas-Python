# p083-rombo-caracter.py
# Dibuja un rombo con el caracter elegido por el usuario

print("\033[2J\033[H", end="")
print(f"Dibuja un rombo con el caracter elegido por el usuario\n")

altura = int(input("Dame un número impar para la altura: "))
while altura % 2 == 0:
    print("El número debe ser impar.")
    altura = int(input("Dame un número impar para la altura: "))

simbolo = input("¿Qué caracter quieres usar? ")

# Parte superior del rombo
for ancho in range(1, altura + 1, 2):
    espacios = (altura - ancho) // 2
    print(" " * espacios + simbolo * ancho)

# Parte inferior del rombo
for ancho in range(altura - 2, 0, -2):
    espacios = (altura - ancho) // 2
    print(" " * espacios + simbolo * ancho)

print("\nPrograma terminado")