#p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas y de convercion de grados

import math as mt

print("\033[H\033[J", end="")
print("Demostrar el uso de funciones trigonometricas y de convercion de grados")

angulo = int(input("Dame el angulo en grados:"))
radianes = mt.radians(angulo)

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tang = mt.tan(radianes)

grados = mt.degrees(radianes) 

salida = ( "\nResumen de funciones trigonometricas y de conversion\n"
f"El seno es      :  {seno:.4f} \n"          
f"El coseno es    :  {coseno:.4f} \n"
f"La tangente es  :  {tang:.4f} \n"      
f"El angulo de {angulo} grados, equivale a {radianes:.4f} radianes"
)

print(salida)