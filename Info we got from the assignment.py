def calc():
keuze = input ("Wat wil je berekenen, spanning (U), stroom (I) of de weerstand (R)? : ")

if keuze == "U":
    I = int(input("Geef de stroom in Ampere: "))
    R = int(input("Geef de weerstand in Ohm: "))
    U = I * R
    print ("De spanning, stroom maal weerstand, is", U =, "Volt")

calc():