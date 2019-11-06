from math import sqrt,sin,cos,tan,pi,log
#   Poloměr země
R = 6371110000
v = 0
u = 0
Rovnobezky = []
Poledniky = []

#   Uživatelské vstupy
meritko = int(input("Zadej celočíselné měřítko: "))
skok = int(input("Po kolika stupních chceš měřit? Zadej celočíselné číslo: "))
R = float(input("Zadej poloměr země v km: "))
R = R * 1000000
if R == 0:
    R = 6371110000
z = ""

#   Funkce pro výpočet k jednotlivým zobrazením
def Lam(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = x / meritko
        if xm > 1000 and xm < 1000:
            xm = "-"
        Poledniky.append(xm)
        for u in range(-90, 91, skok):
            y = R * sin(u * pi / 180)
            ym = y / meritko
            if ym > 1000 and ym < 1000:
                ym = "-"
            Rovnobezky.append(ym)
def Mar(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = x / meritko
        if xm > 1000 and xm < 1000:
            xm = "-"
        Poledniky.append(xm)
        for u in range(-90, 91, skok):
            y = R * (u * pi / 180)
            ym = y / meritko
            if ym > 1000 and ym < 1000:
                ym = "-"
            Rovnobezky.append(ym)
def Bra(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = x / meritko
        if xm > 1000 and xm < 1000:
            xm = "-"
        Poledniky.append(xm)
        for u in range(-90, 91, skok):
            y = 2 * R * tan((u*pi/180)/2)
            ym = y / meritko
            if ym > 1000 and ym < 1000:
                ym = "-"
            Rovnobezky.append(ym)
def Mer(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = x / meritko
        if xm > 1000 and xm < 1000:
            xm = "-"
        Poledniky.append(xm)
        for u in range(-90, 91, skok):
            y = R * log(tan(2/((90-u)*pi/180)))
            ym = y / meritko
            if ym > 1000 and ym < 1000:
                ym = "-"
            Rovnobezky.append(ym)

#   Cyklus vypisování hodnot
while z != "L" and z != "A" and z != "B" and z != "M":
    z = input("Zadej zkratku jednoho ze zobrazení:\nL - Lambertovo zobrazení \nA - Marinovo zobrazení\nB - Braunovo zobrazení\nM - Mercatorovo zobrazení\nKteré?: ")
    if z == "L":
        Lam(R)
    elif z == "A":
        Mar(R)
    elif z == "B":
        Bra(R)
    elif z == "M":
        Mer(R)
    else:
        z = input("Neplatný vstup! Pouze:\nL - Lambertovo zobrazení \nA - Marinovo zobrazení\nB - Braunovo zobrazení\nM - Mercatorovo zobrazení\nKteré?: ")

print(f"Rovnoběžky (mm): {Rovnobezky}")
print(f"Poledníky (mm): {Poledniky}")