# p008-entrada-multiple.py
# Entrada multiple  en una sola linea con map

# 1. Leer 10 numeros en la misma linea (separados por espacios)
print("Ingresa 10 numeros separados por espacios:")
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = map(float, input().split())

# 2. Sumar las 10 variables 
suma =  v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10

# 3. Mostrar el resultado 
print(f"\nLa suma de los 10 valores es: {suma}")
