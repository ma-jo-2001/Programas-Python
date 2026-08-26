# p031-2da-ley-de-newton.py
#Calcula los valores de la 2da ley de newton

print("\033[2J\033[H", end="")
print("Calcula los valores de la 2da ley de newton\n")
print("[F] uerza (f = m * a)")
print("[M] asa (m = f / a)")
print("[A] celeracion (a = f / m)")
print("Elige ?")
op = input().upper()

f = m = a = 0

if op == "F":
    print("\nCalculando la Fuerza")
    m = float(input("Dame la masa ? "))
    a = float(input("Dame la aceleracion ? "))
    f = m * a
    print("La fuerza es  " + str(f))
elif op == "M":
    print("\nCalcula la Masa")
    f = float(input("Dame la fuerza ? "))
    a = float(input("Dame la aceleracion ?"))
    m = f / a
    print("\nLa masa es " + str(f))
elif op == "A":
    print("\nCalcula la aceleracion ")
    f = float(input("Dame la fuerza ?"))
    m = float(input("Dame la masa. ?"))
    a = f / m 
    print("\nLa aceleracion es " + str(f))

print(" \n Proceso terminado")