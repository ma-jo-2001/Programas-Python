# p110-comprension-filtra-palabras.py
# Genera una compresion de listas 

print("\033c", end="")

entrada = input("Introduzca palabras separadas por espacios: ")

# Lista original
lista_original = entrada.split()

# Comprensión de listas: palabras con más de 4 caracteres, en mayúsculas
lista_filtrada = [palabra.upper() for palabra in lista_original if len(palabra) > 4]

print("\n--- Resultados ---")
print("Lista original:", lista_original)
print("Lista filtrada (>4 caracteres en mayúsculas):", lista_filtrada)