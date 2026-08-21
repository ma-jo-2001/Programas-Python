# p022-resistencia-equivalente-paralelo.py
# Calcula la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo 

# Formula rt = 1 / (1/r1 + 1/r2 +1/r3 + 1/r4)

print("\033[H\033[J", end="")
print("Calcular la resistencia equivalente de un circuito en paralelo\n")

R1 = float(input("Ingresa el valor de la resistencia: R1"))
R2 = float(input("Ingresa el valor de la resistencia: R2"))
R3 = float(input("Ingresa el valor de la resistencia: R3"))
R4 = float(input("Ingresa el valor de la resistencia: R4"))

# Calcular la resistencia equivalente 

rt = 1 / ((1/R1) + (1/R2) + (1/R3) + (1/R4))

print("La resistencia equivalente del circuito es:", rt)