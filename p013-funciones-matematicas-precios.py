#p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas de redondeo 


import math as mt

print("\033[H\033[J")


precio = 15.495987
print(f"Precio Original $ {precio:.2f}")
print(f"Arriba          $ {mt.ceil(precio)}")
print(f"Abajo           $ {mt.floor(precio):.2f}")
print(f"Truncar         $ {mt.trunc(precio):.2f}")
print(f"Automatico      $ {round(precio):.2f}")
print(f"Automatico Dec  $ {round(precio,3)}")
