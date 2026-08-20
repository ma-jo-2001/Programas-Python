# p011-operadores-asignacion.py
# Demuestra el uso de operadores de asignacion

print("\033[H\033[J")
print("Operadores de asignacion en python \n")

x = 100

x = int(input("Dame el valor de x :"))

x += 5
print(f"sumar 5 a x : {x}")
x -= 3
print(f"restar 3 a x : {x}")
x *= 2
print(f"multiplicar 2 a x : {x}")
x /= 4
print(f"dividir 4 a x : {x}")
x %= 4
print(f"modulo 4 a x : {x}")
x **= 2
print(f"x elevada al cuadrado : {x}")
x //= 2
print(f"Dividir x entre 2 entera : {x}")


