# p040-calculo-notas.py
# Calcula el promedio de 5 Calificaciones ingresadas por el usuario

print("\033[2J\033[H", end="")
print("Ingresa 5 calificaciones (el 5 al 10): \n")

c1 = float(input("Calificacion 1:"))
c2 = float(input("Calificacion 2:"))
c3 = float(input("Calificacion 3:"))
c4 = float(input("Calificacion 4:"))
c5 = float(input("Calificacion 5:"))

promedio = (c1 + c2 + c3 + c4 + c5) / 5

print(f"\n El promedio es: {promedio:.2f}")

if promedio < 6:
    print("Quedas reprobado")
elif promedio <= 7:
    print("Pasas de panzazo")
elif promedio <= 8:
    print("Muy bien, puedes mejorar")
elif promedio <= 9:
    print("Excelente, sigue asi")
elif promedio <= 10:
    print("Perfecto, tu esfuerzo valio la pena")
else:
    print("ERROR, promedio fuera de rango")

print("\n El programa termino")    