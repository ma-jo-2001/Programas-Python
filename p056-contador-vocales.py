# p056-contador-vocales.py
# Cuenta las vocales y consonantes en una frase y otros caracteres

print("\033[2J\033[H", end="")
print("Tabla de conversion de Pesos a Dolares\n")

frase = input("Traduce una frase : ").lower()
print(f"\nLa frase a analizar es : {frase} y tiene {len(frase)} caracteres")

i= vocal = constante = otro = 0
while i < len(frase):
    c = frase[i]
    print(c, end ="")
    if "a" <= c <= "z":
        if c in "aeiou":
            vocal += 1
        else:
            constante += 1
    else:
        print("no")
        otro += 1
    i += 1

print(f"Vocales: {vocal}\nconstantes: {constante}\nOtros: {otro}")