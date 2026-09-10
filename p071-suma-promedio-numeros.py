# p071-suma-promedio-numeros.py 
# Calcula la suma y el promedio de n calificaciones 

while True:
    print("\033[2J\033[H", end="")
    print("Calcular la suma y el promedio de n calificaciones\n")

    n = int(input("Cuantas calificaciones ?"))

    suma = 0
    stracals = ""
    for i in range(n):
        cal = int(input(f"Calificacion {i} :"))
        suma += cal
        stracals = stracals + str(cal) +""

    print(f"\nLos numeros fueron: {stracals}")
    print(f"L suma es: {suma}")
    print(f"El promedio es: {suma/n}")

    if input("\nSeguimos (S/N) ? ").upper() == "N":break