# p136-segundo-examen-parcial.py
# Procesar el registro de vuelos de una aerolínea ("AeroRegistro").

# ==========================================================
# AeroRegistro
# Registro y análisis de vuelos - Computación Aplicada
# ==========================================================

# ----------------------------------------------------------
# 1. ESTRUCTURAS DE DATOS INICIALES
# ----------------------------------------------------------
vuelos = []                  # Lista de diccionarios (un diccionario por vuelo)
destinos_unicos = set()      # Conjunto de destinos sin repetir
historial_inmutable = []     # Lista de tuplas (numero_vuelo, aerolinea, destino)

print("=== AeroRegistro ===")
print("Para terminar, escribe * o deja vacío el número de vuelo.\n")

# ----------------------------------------------------------
# 2. CAPTURA DE VUELOS (ciclo while)
# ----------------------------------------------------------
while True:
    numero_vuelo = input("Número de vuelo: ").strip()

    # Condición de salida: asterisco o número de vuelo vacío
    if numero_vuelo == "*" or numero_vuelo == "":
        break

    # Datos restantes del vuelo (pasajeros entero, tarifa decimal)
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    aerolinea = input("Aerolínea: ").strip()
    pasajeros = int(input("Pasajeros: "))
    tarifa = float(input("Tarifa: "))

    # Diccionario con los datos del vuelo
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa
    }

    # Guardar el vuelo en la lista y en las colecciones especiales
    vuelos.append(vuelo)
    destinos_unicos.add(destino)
    historial_inmutable.append((numero_vuelo, aerolinea, destino))

    print("Vuelo registrado.\n")

print("Captura terminada.")
print("Vuelos registrados:", len(vuelos))

# ----------------------------------------------------------
# 3. VISUALIZACIÓN DE LOS DATOS
# ----------------------------------------------------------

# 3.1 Datos crudos: lista completa de diccionarios
print("\n=== DATOS CRUDOS ===")
print(vuelos)

# 3.2 Destinos únicos: conjunto sin ciudades repetidas
print("\n=== DESTINOS ÚNICOS ===")
print("Destinos únicos:", destinos_unicos)

# 3.3 Historial inmutable: lista de tuplas
print("\n=== HISTORIAL INMUTABLE ===")
print("Historial inmutable:", historial_inmutable)

# 3.4 Tabla formateada (< alinea a la izquierda, > a la derecha)
print("\n=== TABLA DE VUELOS ===")
print(f"{'No. Vuelo':<10} {'Origen':<20} {'Destino':<20} {'Aerolínea':<18} {'Pasajeros':>10} {'Tarifa':>14}")
print("-" * 97)

for vuelo in vuelos:
    # Se arma primero la tarifa con $, separador de miles y 2 decimales
    tarifa_texto = f"${vuelo['tarifa']:,.2f}"
    print(f"{vuelo['numero_vuelo']:<10} {vuelo['origen']:<20} {vuelo['destino']:<20} {vuelo['aerolinea']:<18} {vuelo['pasajeros']:>10} {tarifa_texto:>14}")

# ----------------------------------------------------------
# 4. ANALÍTICA Y CÁLCULOS ESTADÍSTICOS
# ----------------------------------------------------------
print("\n=== ANALÍTICA DE VUELOS ===")

# Si no hay vuelos, se evita dividir entre cero y buscar máximos/mínimos
if len(vuelos) == 0:
    print("No se registraron vuelos, por lo que no hay estadísticas que mostrar.")
else:
    # 4.1 Total de vuelos
    total_vuelos = len(vuelos)
    print("\n--- Total de vuelos ---")
    print(f"Vuelos registrados: {total_vuelos}")

    # 4.2 y 4.3 Conteo de vuelos por aerolínea y por destino (diccionarios contadores)
    conteo_aerolineas = {}
    conteo_destinos = {}

    for v in vuelos:
        conteo_aerolineas[v["aerolinea"]] = conteo_aerolineas.get(v["aerolinea"], 0) + 1
        conteo_destinos[v["destino"]] = conteo_destinos.get(v["destino"], 0) + 1

    print("\n--- Vuelos por aerolínea ---")
    for nombre, cantidad in conteo_aerolineas.items():
        print(f"{nombre}: {cantidad}")

    print("\n--- Vuelos por destino ---")
    for ciudad, cantidad in conteo_destinos.items():
        print(f"{ciudad}: {cantidad}")

    # 4.4 y 4.5 Sumas y promedios (acumuladores; una sola tarifa por vuelo)
    total_pasajeros = 0
    total_tarifas = 0

    for v in vuelos:
        total_pasajeros = total_pasajeros + v["pasajeros"]
        total_tarifas = total_tarifas + v["tarifa"]

    promedio_pasajeros = total_pasajeros / total_vuelos
    promedio_tarifas = total_tarifas / total_vuelos

    print("\n--- Pasajeros ---")
    print(f"Total de pasajeros: {total_pasajeros:,}")
    print(f"Promedio de pasajeros por vuelo: {promedio_pasajeros:,.2f}")

    print("\n--- Tarifas ---")
    print(f"Suma total de tarifas: ${total_tarifas:,.2f}")
    print(f"Tarifa promedio: ${promedio_tarifas:,.2f}")

    # 4.6 Vuelo más caro y más barato (se parte del primer vuelo y se compara)
    vuelo_mas_caro = vuelos[0]
    vuelo_mas_barato = vuelos[0]

    for v in vuelos:
        if v["tarifa"] > vuelo_mas_caro["tarifa"]:
            vuelo_mas_caro = v
        if v["tarifa"] < vuelo_mas_barato["tarifa"]:
            vuelo_mas_barato = v

    print("\n--- Vuelo más caro y más barato ---")
    print(f"Más caro: {vuelo_mas_caro['numero_vuelo']} con tarifa de ${vuelo_mas_caro['tarifa']:,.2f}")
    print(f"Más barato: {vuelo_mas_barato['numero_vuelo']} con tarifa de ${vuelo_mas_barato['tarifa']:,.2f}")