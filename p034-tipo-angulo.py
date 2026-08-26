# p034-tipo-angulo.py
# Dame un angulo en el rango de 0 a 360 indicar que tipo de angulo es 

print("\033[2J\033[H", end="")
print("Dame un angulo en el rango de 0 a 360 indicar que tipo de angulo es\n")

ang = int(input("angulo ?"))

if ang < 0  and ang > 360:
    print("\nAngulo fuera de rango")
else:
    print("Tu angulo es : ", end="")
    if ang < 90: 
        print("ANGULO")
    elif ang == 90: 
        print("RECTO")
    elif ang < 180: 
        print("OBTUSO")
    elif ang == 180: 
        print("LLANO")
    elif ang < 360: 
        print("CONCAVO")
    
print(" \n Proceso terminado")

