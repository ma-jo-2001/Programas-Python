# p055-tabla-multiplicar-while-v2.py
#  Imprime la tabla del 1 al 10, usando while 

while True: 
    print("\033[2J\033[H", end="")
    print("Tablas de multiplicar usando while\n")

    n = int(input("Hasta cual tabla quieres  ?"))
    m = int(input("Hasta donde llega.        ?"))

    t = 1 
    while t <= n:
        print(f"\nTabla del {t} \n")
        c = 1
        while c <= m:
            print(f"{t:3} x {c:3} = {c*t}")
            c += 1

        t += 1


    if input("\nDeseas continuar (s/n)  ?").upper()== "N" : break

    print("\nTerminamos de imprimir las tablas ...")