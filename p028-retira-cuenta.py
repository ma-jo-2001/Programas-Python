# p028-retira-cuenta.py
# Simula el retiro de dinero de una cuenta con validacion 

saldo_cuenta = 1500
print("\033[2J\033[H", end="")
print("Simula el retiro de dinero de una cuenta con validacion\n")

cantidad_retiro = float(input("Cantidad a retirar de la cuenta saldo: {saldo_cuenta} ?"))

if cantidad_retiro > 0:
    print("\nProcedemos al retiro ...")
    if cantidad_retiro <= saldo_cuenta:
        nuevo_saldo = saldo_cuenta - cantidad_retiro
        print(f"\nRetiro exitoso, tu nombre saldo es : {nuevo_saldo}")
    else: 
        print(f"Quieres retirar {cantidad_retiro} pero tienes {saldo_cuenta} NO TE ALCANZA")
else:
    print("\nLa cantidad a retirar debe ser un numero positivo")

print("\nGracias por usar nuestro servicio")

print("\nPrograma finalizado")