#p020-operaciones-matematicas.py 
#Demuestra el uso de los operadores aritmeticos

print("\033[H\033[J") 
print("_" * 50)
print("calculadora de Operaciones matematicas \n")
print("_" * 50)

x = float(input("Valor de x : "))
y = float(input("Valor de y : "))

suma = x + y
resta = x - y
mult = x * y
div = x / y
modu = x % y 
pot = x ** y
dive = x // y

print("Resultado de las operaciones realizadas \n")
print("=" * 50)
print(f"Numeros: {x} , {y}")
print(f"Suma: {suma:>20.3f}")
print(f"Resta: {resta:>20.3f}")
print(f"Multiplicación: {mult:>20.3f}")
print(f"División: {div:>20.3f}")
print(f"Modulo: {modu:>20.3f}")
print(f"Potencia: {pot:>20,.3f}")
print(f"Division Entera: {dive:.3f}")
print("=" * 50)