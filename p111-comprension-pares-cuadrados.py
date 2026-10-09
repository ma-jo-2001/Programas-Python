# p111-comprension-pares-cuadrados.py
# Generar una lista de números enteros del 1 al n (donde n es ingresado por el usuario).

print("\033c", end="")

n = int(input("Introduzca el límite n: "))

# Lista original del 1 al n
lista_original = list(range(1, n + 1))

# Comprensión de listas: cuadrados solo de los números pares
cuadrados_pares = [num ** 2 for num in lista_original if num % 2 == 0]

# Suma de los cuadrados
suma_cuadrados = sum(cuadrados_pares)

print("\n--- Resultados ---")
print(f"Lista original (1 a {n}):", lista_original)
print("Cuadrados de números pares:", cuadrados_pares)
print("Suma de cuadrados:", suma_cuadrados)