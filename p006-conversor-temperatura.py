# p006-conversor-temperatura.py
# Convertir una temperatura da en grados Celcius a grados Faranheit

print("\033[2J\033[H", end="")
print("Convertir una temperatura da en grados Celcius a grados Faranheit\n")

# f = (float(input("Grados Celcius")) * 9 / 5.0) + 32

f = float(input("Grados Celcius ? ")) 
c = (f * 9 / 5) + 32

print(f"La temperatura de {f} grados centigrados equivale a {c} grados farenheit")
