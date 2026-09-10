# p073-cifrado-cesar.py
# Cifra un mensaje con desplazamientos (Cifrados de cesar)

print("\033[2J\033[H", end="")
print("Cifrado de cesar\n")

mo = input("Mensaje ?")
d = int(input("Desplazamiento ?"))

ms = cn = ""

for c in mo :
    if c.isalpha(): # Solo letras
        ca = ord(c)
        # if c.islower():
        # bd = ord("a")
        # else:
        #     bd = ord("a")
        bd = ord("a") if c.islower() else ord("A")
        cn = bd + (ca - bd + d) % 26
        ms = ms + chr(cn)
    else:
        ms= ms + c

print("Mensaje cifrado:" + ms)