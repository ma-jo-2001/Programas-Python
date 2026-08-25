# p026–convertir-temperaturas-v2.py
# Convierte de Celcius a Farenheit y viseversa 

print("\033[2J\033[H", end="")
print("Convierte de Celcius a Farenheit y viceversa\n")

print("[ 1 ] Convertir de Farenheit a Celcius ")
print("[ 2 ] Convertir de Celcius a Farenheit ")

op = int(input("Elige ?"))

if op==1:
    print("\n ➡️ Convirtiendo de Farenheit a Celsius")
    f=float(input("Dame la temperatura en grados Farenheit"))
    c = (f - 32)*5 / 9
    print("{f} ✔️ grados Farenheit, equivale a {c} grados Celcius")

else:
    if op==2:
        print("\n ➡️ Convirtiendo de Celcius a Farenheit")
        c=float(input("Dame la temperatura en grados Centigrados"))
        f = (c * 9/5) * 32
        print("{f} ✔️ grados Celcius, equivale a {f} grados Farenheit")
    else:
        print("\nOpcion invalida")

print("\nPrograma finalizado" )
