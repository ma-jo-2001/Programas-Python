# p035-tipo-triangulo.py 
# # p034-tipo-angulo.py
# Dame un angulo en el rango de 0 a 360 indicar que tipo de angulo es 

print("\033[2J\033[H", end="")
print("Dame un angulo en el rango de 0 a 360 indicar que tipo de angulo es\n")

ang = int(input("angulo ?"))

if ang >= 0  and ang <= 360:
    print("Tu angulo es : ", end="")
    if ang < 90: 
        print("ANGULO")
    elif ang == 90: 
        print("RECTO")
    elif ang > 90 and ang < 180: 
        print("OBTUSO")
    elif ang == 180: print("LLANO")
    elif ang >180 and ang < 360: 
        print("CONCAVO")
    else: 
        print("\nAngulo fuera de rango")

print(" \n Proceso terminado")