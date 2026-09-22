"""
p085_SimuladorVentaCombustible.py
Sistema interactivo de consola para la gestión de una estación de servicio.

Restricciones del Bloque 1:
- No se usan listas, tuplas, diccionarios ni funciones personalizadas (def).
- Solo variables (int, float, str), operadores aritméticos, estructuras de
  control (while, for, if/elif/else) y f-strings.
"""

# --- Constantes del sistema ---
LIMITE_LITROS = 10 ** 3        # máximo de litros permitido por venta (uso de **)
CAPACIDAD_TANQUE = 50          # litros que caben en un tanque, para la simulación
RENDIMIENTO_MIN = 0
RENDIMIENTO_MAX = 100

print("=" * 40)
print(f"{'SISTEMA - ESTACIÓN DE SERVICIO':^40}")
print("=" * 40)

# --- Ciclo principal del menú ---
while True:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Venta de Combustible")
    print("2. Simulación de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ").strip()

    if not opcion.isdigit():
        print("  [Error] Opción inválida. Escribe un número del 1 al 4.")
        continue                       # reinicia el menú

    opcion = int(opcion)

    if opcion < 1 or opcion > 4:
        print("  [Error] Opción fuera de rango. Elige entre 1 y 4.")
        continue                       # reinicia el menú

    # ------------------------------------------------------------
    # OPCIÓN 1: VENTA DE COMBUSTIBLE
    # ------------------------------------------------------------
    if opcion == 1:

        combustible = input("Tipo de combustible (Magna / Premium / Diésel): ").strip()

        # Precio por litro (float positivo)
        while True:
            texto = input("Precio por litro ($): ").strip()
            if texto.startswith("-"):
                print("  [Error] No se permiten valores negativos.")
                continue
            # Acepta dígitos con a lo más un punto decimal
            if not texto.replace(".", "", 1).isdigit():
                print("  [Error] Escribe un número positivo (ej. 24.50).")
                continue
            precio = float(texto)      # str -> float
            if precio <= 0:
                print("  [Error] El precio debe ser mayor que cero.")
                continue
            break

        # Cantidad de litros (float positivo, con límite 10 ** 3)
        while True:
            texto = input("Cantidad de litros: ").strip()
            if texto.startswith("-"):
                print("  [Error] No se permiten valores negativos.")
                continue
            if not texto.replace(".", "", 1).isdigit():
                print("  [Error] Escribe un número positivo (ej. 35.5).")
                continue
            litros = float(texto)
            if litros <= 0:
                print("  [Error] Los litros deben ser mayores que cero.")
                continue
            if litros > LIMITE_LITROS:
                print(f"  [Error] Máximo permitido por venta: {LIMITE_LITROS:,} L.")
                continue
            break

        # Cálculo del total y ticket con alineación a la derecha
        total = precio * litros
        print()
        print("=" * 40)
        print(f"{'TICKET DE VENTA':^40}")
        print("=" * 40)
        print(f"  Combustible   : {combustible:>20}")
        print(f"  Precio/litro  : ${precio:>18,.2f}")
        print(f"  Litros        :  {litros:>18,.2f}")
        print("-" * 40)
        print(f"  TOTAL A PAGAR : ${total:>18,.2f}")
        print("=" * 40)

    # ------------------------------------------------------------
    # OPCIÓN 2: SIMULACIÓN DE RENDIMIENTO
    # ------------------------------------------------------------
    elif opcion == 2:

        # Kilometraje inicial (float positivo)
        while True:
            texto = input("Kilometraje inicial (km): ").strip()
            if texto.startswith("-"):
                print("  [Error] No se permiten valores negativos.")
                continue
            if not texto.replace(".", "", 1).isdigit():
                print("  [Error] Escribe un número positivo (ej. 12500).")
                continue
            km_inicial = float(texto)
            if km_inicial < 0:
                print("  [Error] El kilometraje no puede ser negativo.")
                continue
            break

        # Rendimiento (km/L), validado entre 0 y 100
        while True:
            texto = input("Rendimiento del vehículo (km por litro): ").strip()
            if texto.startswith("-"):
                print("  [Error] No se permiten valores negativos.")
                continue
            if not texto.replace(".", "", 1).isdigit():
                print("  [Error] Escribe un número positivo (ej. 12.5).")
                continue
            rendimiento = float(texto)
            if rendimiento <= RENDIMIENTO_MIN or rendimiento > RENDIMIENTO_MAX:
                print(f"  [Error] Debe estar entre {RENDIMIENTO_MIN} y {RENDIMIENTO_MAX} km/L.")
                continue
            break

        # Kilometraje recorrido por mes (float positivo)
        while True:
            texto = input("Kilometraje estimado por mes: ").strip()
            if texto.startswith("-"):
                print("  [Error] No se permiten valores negativos.")
                continue
            if not texto.replace(".", "", 1).isdigit():
                print("  [Error] Escribe un número positivo (ej. 1200).")
                continue
            km_mensual = float(texto)
            if km_mensual <= 0:
                print("  [Error] El kilometraje mensual debe ser mayor que cero.")
                continue
            break

        # Meses a proyectar (entero positivo)
        while True:
            texto = input("Número de meses a proyectar: ").strip()
            if not texto.isdigit():
                print("  [Error] Escribe un número entero positivo (ej. 6).")
                continue
            meses = int(texto)
            if meses <= 0:
                print("  [Error] El número de meses debe ser mayor que cero.")
                continue
            break

        litros_mes = km_mensual / rendimiento

        print()
        print("=" * 72)
        print(f" Mes | Odómetro (km) | Litros mes | Litros acum. | Tanques |Sobrante (L)")
        print("=" * 72)

        # Ciclo for con range(): una fila por cada mes
        for mes in range(1, meses + 1):
            odometro = km_inicial + km_mensual * mes
            litros_acum = litros_mes * mes
            tanques = int(litros_acum // CAPACIDAD_TANQUE)   # división entera
            sobrante = litros_acum % CAPACIDAD_TANQUE         # residuo
            print(f"{mes:^5}|{odometro:>15,.1f}|{litros_mes:>12,.2f}|"
                  f"{litros_acum:>14,.2f}|{tanques:>9}|{sobrante:>13,.2f}")

        print("=" * 72)
        print(f"  Tanques llenos = litros acumulados // {CAPACIDAD_TANQUE} L | "
              f"Sobrante = litros acumulados % {CAPACIDAD_TANQUE} L")

    # ------------------------------------------------------------
    # OPCIÓN 3: CLASIFICADOR DE CLIENTE
    # ------------------------------------------------------------
    elif opcion == 3:

        while True:
            texto = input("Volumen de compra mensual (litros): ").strip()
            if texto.startswith("-"):
                print("  [Error] No se permiten valores negativos.")
                continue
            if not texto.replace(".", "", 1).isdigit():
                print("  [Error] Escribe un número positivo (ej. 250).")
                continue
            volumen = float(texto)
            if volumen <= 0:
                print("  [Error] El volumen debe ser mayor que cero.")
                continue
            break

        if volumen < 100:
            categoria = "Regular"
        elif volumen >= 100 and volumen <= 500:
            categoria = "Premium"
        else:
            categoria = "Flotilla"

        print(f"\nCliente clasificado como: {categoria}")

    # ------------------------------------------------------------
    # OPCIÓN 4: SALIR
    # ------------------------------------------------------------
    elif opcion == 4:
        break                          # salida limpia

print("\nGracias por usar el sistema. ¡Hasta pronto!")