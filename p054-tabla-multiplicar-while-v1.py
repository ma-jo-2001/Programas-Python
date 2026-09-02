# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla del 1 al 10, usando while 

while True: 
    print("\033[2J\033[H", end="")

    print("Tablas de multiplicar usando while\n")

    t = int(input("Que tabla quieres  ?"))
    n = int(input("Hasta donde        ?"))

    print("\nImprime la tabla del" + str(t))

    c = 1
    while c <= n:
        print(f"{t:3} x {c:3} = {c*t}")
        c+=1

    if input("\nDeseas continuar (s/n)  ?").upper()== "N" : break

print("\nTerminamos de imprimir las tablas ...")