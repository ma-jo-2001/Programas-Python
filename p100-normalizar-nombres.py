# p100-normalizar-nombres.py 
# De una lista de nombres con espacios y mayusculas se normaliza a minusculas sin espacios 

print("\033c", end="")
print("\033[1;34m" + "Normaliza nombres" + "\033[0m")

nombres = ["  Juan  ", "  Maria  ", "  Pedro  ", "  Ana  ", " Luis "]

# Se normalizan los nombres usando compresion de listas 
nombres_normalizados = [nombre.strip().lower() for nombre in nombres]

print("Nombres originales:", nombres)
print("Nombres normalizados:", nombres_normalizados)