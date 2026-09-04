# p062-conversion-temperaturas.py
# Programa que muestra la conversión a Fahrenheit para cada grado

print("\033[2J\033[H", end="")
print("Conversión de temperaturas de Celsius a Fahrenheit\n")

while True:
    temp_inicial = int(input("Introduce la temperatura inicial en °C: "))
    temp_final = int(input("Introduce la temperatura final en °C: "))

    celsius = temp_inicial

    while celsius <= temp_final:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        celsius += 1

    if input("\n¿Desea continuar (S/N)? ").upper() == 'N':
        break

print("\nPrograma Terminado.")