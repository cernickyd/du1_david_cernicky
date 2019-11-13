#   Import potřebných funkcí pro vypočítání jednotlivých zobrazení
from math import sqrt,sin,cos,tan,pi,log

#   Poloměr země v cm, tvorba proměnných a seznamů
R = 637111000
v = 0
u = 0
z = ""
Rovnobezky = []
Poledniky = []
#   Uživatelské vstupy, ošetřeno o prázdné hodnoty
#   Zobrazení
I = 0
while I != 1:
    Z = input("Zadej zkratku jednoho ze zobrazení:\nL - Lambertovo zobrazení \nA - Marinovo zobrazení\nB - Braunovo zobrazení\nM - Mercatorovo zobrazení\nKteré?: ")
    if Z == "L" or Z == "A" or Z == "B" or Z == "M":
        I = 1
#   Měřítko - ideálně něco mezi 10 - 50M
meritko = input("Jaké chceš měřítko? Zadej přirozené číslo měřítka: ")
while meritko == "":
    meritko = input("Tak znovu... Jaké chceš měřítko? Zadej přirozené číslo měřítka: ")
meritko = int(meritko)

#   Přidán 'skok' - po kolika stupních chci měřit
skok = input("Po kolika stupních chceš měřit? Zadej přirozené číslo: ")
while skok == "":
    skok = input("Tak znovu... Po kolika stupních chceš měřit? Zadej přirozené číslo: ")
skok = int(skok)

#   Poloměr země je volitelný - pokud je roven nule je mu přiřazena defaultní hodnota
R = input("Zadej poloměr země v km: ")
while R == "":
    R = input("Zadej znovu poloměr země v km: ")
R = float(R)
R = R * 100000
if R == 0:
    R = 637111000

#   Funkce pro výpočet k jednotlivým zobrazením
def Lam(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = round(x / meritko,1)
        if xm > 100 or xm < -100:
            xm = "-"
        Poledniky.append(xm)
    for u in range(-90, 91, skok):
        y = R * sin(u * pi / 180)
        ym = round(y / meritko,1)
        if ym > 100 or ym < -100:
            ym = "-"
        Rovnobezky.append(ym)
def Mar(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = round(x / meritko,1)
        if xm > 100 or xm < -100:
            xm = "-"
        Poledniky.append(xm)
    for u in range(-90, 91, skok):
        y = R * (u * pi / 180)
        ym = round(y / meritko,1)
        if ym > 100 or ym < -100:
            ym = "-"
        Rovnobezky.append(ym)
def Bra(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = round(x / meritko,1)
        if xm > 100 or xm < -100:
            xm = "-"
        Poledniky.append(xm)
    for u in range(-90, 91, skok):
        y = 2 * R * tan((u*pi/180)/2)
        ym = round(y / meritko,1)
        if ym > 100 or ym < -100:
            ym = "-"
        Rovnobezky.append(ym)
def Mer(R):
    for v in range(-180, 181, skok):
        x = R * (v * pi / 180)
        xm = round(x / meritko,1)
        if xm > 100 or xm < -100:
            xm = "-"
        Poledniky.append(xm)
    for u in range(-90, 91, skok):
        u = abs(u * pi/180)
        y = R * log(tan((u/2) + pi/4))
        ym = round(y / meritko,1)
        if ym > 100 or ym < -100:
            ym = "-"
        Rovnobezky.append(ym)

#   Cyklus vypisování hodnot
while z != "L" and z != "A" and z != "B" and z != "M":
    z = Z
    if z == "L":
        Lam(R)
        print("Lambertovo zobrazení")
    elif z == "A":
        Mar(R)
        print("Marinovo zobrazení")
    elif z == "B":
        Bra(R)
        print("Braunovo zobrazení")
    elif z == "M":
        Mer(R)
        print("Mercatorovo zobrazení")
    else:
        z = input("Neplatný vstup! Pouze:\nL - Lambertovo zobrazení \nA - Marinovo zobrazení\nB - Braunovo zobrazení\nM - Mercatorovo zobrazení\nKteré?: ")

print(f"Měřítko je 1:{meritko}\nMěříš po {skok}°\nPoloměr země je {R} mm")
print(f"Rovnoběžky (cm): {Rovnobezky}")
print(f"Poledníky (cm): {Poledniky}")

#   Kód pro vypisování jednotlivých hodnot 'u' a 'v'
u = ""
v = ""
while u != 0 or v !=0:
    u = float(input("Zadej zeměpisnou šířku: "))
    while u < -90 or u > 90:
        u = float(input("Zadej zeměpisnou šířku v intervalu (-90,90): "))
    v = float(input("Zadej zeměpisnou délku: "))
    while v < -180 or u > 180:
        v = float(input("Zadej zeměpisnou délku v intervalu (-180,180): "))

    if z == "L":
        x = R * (v * pi / 180)
        xm = round(x / meritko, 1)
        y = R * sin(u * pi / 180)
        ym = round(y / meritko, 1)
    elif z == "A":
        x = R * (v * pi / 180)
        xm = round(x / meritko, 1)
        y = R * (u * pi / 180)
        ym = round(y / meritko, 1)
    elif z == "B":
        x = R * (v * pi / 180)
        xm = round(x / meritko, 1)
        y = 2 * R * tan((u*pi/180)/2)
        ym = round(y / meritko, 1)
    elif z == "M":
        x = R * (v * pi / 180)
        xm = round(x / meritko, 1)
        y = R * log(tan((u/2) + pi/4))
        ym = round(y / meritko, 1)
    if u == 0 and v == 0:
        print("Konec!")
    else:
        print(f"Zeměpisná šířka {u}° je na mapě od středu vzdálena {ym} cm")
        print(f"Zeměpisná délka {v}° je na mapě od středu vzdálena {xm} cm")
        print("Pokud už nechceš pokračovat zadej zem. šířku i délku rovno 0")