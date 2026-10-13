# p121-area-figuras.py
# Crear una lista de diccionarios para almacenar los datos de varias figuras 

import math

figuras = {
    "1":{
        "nombre": "Circulo",
        "parametros": ["radio"],
        "formula": "pi * radio ** 2"
    }, 
    "2": {
        "nombre": "Triangulo",
        "parametros": ["base", "altura"],
        "formula": "base * altura / 2"
    }, 
    "3":{
        "nombre": "Rectangulo",
        "parametros": ["base", "altura"],
        "formula": "base * altura"
    }
}

while True:
    print("\nCalculadora de areas")
    for opcion, figura in figuras.items():
        print(f"{opcion}. {figura["nombre"]}")
    print("0. Salir")

    opcion = input("Elija una figura: ")
    if opcion == "0":
        print("Hasta luego.")
        break

    if opcion not in figuras:
        print("Opcion no valida. Intente de nuevo.")
        continue

    figura = figuras[opcion]
    valores = {}
    for parametro in figura["parametros"]:
        while True:
            try:
                valor = float(input(f"Ingrese {parametro}:"))
                if not math.isfinite(valor) or valor <= 0:
                    print("El valor debe ser un numero mayor que cero.")
                    continue 
                valores[parametro] = valor
                break 
            except ValueError:
                print("Ingrese un numero valido.")

    contexto = {"pi": math.pi, ** valores}
    area = eval(figura["formula"], {"__builtins__": {}}, contexto)
    print(f"Formula: {figura["formula"]}")
    print(f"Area del {figura['nombre'].lower()}: {area:.2f}")