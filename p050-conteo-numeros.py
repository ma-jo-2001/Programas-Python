# p050-conteo-numeros.py
# El usuario introduce en numeros parar con 999, se suman y se cuentan

print("\033[2J\033[H", end="")
print("El usuario introduce en numeros parar con 999, se suman y se cuentan\n")

c = suma = cp = cn = cz =0

while True:
    num= int(input("Numero ?"))
    if num == 999: break
    c += 1
    suma += num # Acumulando
    if num > 0: 
        cp += 1 # Contando
    elif num < 0 : 
        cn += 1  # Contando
    else: 
        cz +=1  # Contando


print("\n Resumen de los calculos")
print(f"\n Cuantos : {c}")
print(f"\n Suma. : {suma}")
print(f"\n Pos : {cp}")
print(f"\n Neg : {cn}")
print(f"\n Zer : {cz}")


print("\n Proceso terminado")