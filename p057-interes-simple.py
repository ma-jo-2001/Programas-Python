#p 057-interes-simple.py
# Calcula los años necesarios para alcanzar una meta de ahorro

print("\033[2J\033[H", end="")
print("Calcula los años necesarios para alcanzar una meta de ahorro\n")

ci = float(input("Capital inicial  ?"))
ti = float(input("Tasa de interes anual (%)  ?"))
ma = float(input("Meta ahorro ?"))

ca = ci
años = iaf = 0
td = (ti/100)

while ca <= ma:
    print(f"{años:2} - {ca:>15,.2f}")
    iaf = ca * td
    ca += iaf
    años += 1

print(f"\nPara llegar a {ma} debe pasar {años} años, el capital es de {ca:,.2f} ")