# p039-numeros-romanos.py
# Convertir numero entero a numero romano

print("\033[2J\033[H", end="")
print("Dame un numero entre 1 y 10 \n")

numero = int(input())

if numero == 1:
    print(f"El numero {numero} equivale a I en numero romano")
elif numero == 2:
    print(f"El numero {numero} equivale a II en numero romano")
elif numero == 3:
    print(f"El numero {numero} equivale a III en numero romano")
elif numero == 4:
    print(f"El numero {numero} equivale a IV en numero romano")
elif numero == 5:
    print(f"El numero {numero} equivale a V en numero romano")
elif numero == 6:
    print(f"El numero {numero} equivale a VI en numero romano")
elif numero == 7:
    print(f"El numero {numero} equivale a VII en numero romano")
elif numero == 8:
    print(f"El numero {numero} equivale a VIII en numero romano")
elif numero == 9:
    print(f"El numero {numero} equivale a IX en numero romano")
elif numero == 10:
    print(f"El numero {numero} equivale a X en numero romano")
else:
    print("ERROR: el numero tiene que estar entre 1 y 10.")

print("\nPrograma terminado") 