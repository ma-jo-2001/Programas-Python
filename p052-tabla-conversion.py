# p052-tabla-conversion.py 
# Imprime una tabla de conversion de Pesos a Dolares 

tc = 16.80 # establecemos el tipo de cambio actual

while True:
    print("\033[2J\033[H", end="")
    print("Tabla de conversion de Pesos a Dolares\n")
    print(f"Tipo de cambio: {tc}")
    print("_" * 40)

    while True: # Valida que los valores inicial y final sean correctos
        inicial = float(input("Valor inicial del rango  ?"))
        final = float(input("Valor final del rango  ?"))
        if inicial < final and inicial > 0 and final > 0: break
        else: print("Inicial debe ser menor al final")

    c = inicial
    print("\n Pesos \t Dolares")
    print("_" * 30)
    while c <= final:
        print(f"{c:>10.2f} \t {c/tc:>10.2f}")
        c += 1
    print("_" * 30)

    if input("Desea continuar con otro rango (s/n) ?").upper() == "n": break