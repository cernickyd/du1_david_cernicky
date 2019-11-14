#   Import potřebných funkcí pro vypočítání jednotlivých zobrazení
from math import sqrt,sin,cos,tan,pi,log

#   Poloměr země v cm, tvorba proměnných a seznamů
v = 0 # zeměpisná délka
u = 0 # zeměpisná šířka
z = "" # vstup zobrazení
Rovnobezky = []
Poledniky = []

#   Uživatelské vstupy, ošetřeno o prázdné hodnoty
#   Zobrazení
z = input("Zadej zkratku jednoho ze zobrazení:\nL - Lambertovo zobrazení \nA - Marinovo zobrazení\nB - Braunovo zobrazení\nM - Mercatorovo zobrazení\nKteré?: ")
while z != "L" and z != "A" and z != "B" and z != "M":
    z = input("Zadej zkratku jednoho ze zobrazení:\nL - Lambertovo zobrazení \nA - Marinovo zobrazení\nB - Braunovo zobrazení\nM - Mercatorovo zobrazení\nKteré?: ")

#   Měřítko - ideálně něco mezi 10 - 50M
meritko = int(input("Jaké chceš měřítko? Zadej přirozené číslo měřítka: "))
while meritko <= 0:
    meritko = int(input("Tak znovu... Jaké chceš měřítko? Zadej přirozené číslo měřítka: "))

#   Přidán 'skok' - po kolika stupních chci měřit
skok = int(input("Po kolika stupních chceš měřit? Zadej přirozené číslo: "))
while skok <= 0:
    skok = int(input("Tak znovu... Po kolika stupních chceš měřit? Zadej přirozené číslo: "))

#   Poloměr země je volitelný - pokud je roven nule je mu přiřazena defaultní hodnota
R = float(input("Zadej poloměr země v km: "))
while R < 0:
    R = float(input("Zadej znovu poloměr země v km: "))
R = R * 100000
if R == 0:
    R = 637111000

#   Funkce pro výpočet k jednotlivým zobrazením
def lam(R):
    v = 0  # zeměpisná délka
    u = 0  # zeměpisná šířka
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
def mar(R):
    v = 0  # zeměpisná délka
    u = 0  # zeměpisná šířka
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
def bra(R):
    v = 0  # zeměpisná délka
    u = 0  # zeměpisná šířka
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
def mer(R):
    v = 0  # zeměpisná délka
    u = 0  # zeměpisná šířka
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

#   Vypisování hodnot
if z == "L":
    lam(R)
    print("Lambertovo zobrazení")
elif z == "A":
    mar(R)
    print("Marinovo zobrazení")
elif z == "B":
    bra(R)
    print("Braunovo zobrazení")
elif z == "M":
    mer(R)
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