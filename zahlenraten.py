# zahlenraten.py
import random
max = 200
min = 1
gewonnen = False
versuche = 0

zufallszahl = random.randint(min, max)
entscheidung = print("Willst du das Spiel Zahlenraten beginnen?     Ja oder Nein? ")
if(entscheidung == "nein"):
    print("Schade, bis zum nächsten Mal!")
else:
    print("Lass uns Spielen!")
    print("Bitte raten sie eine Zahl zwischen 1 und 200!")

    while(gewonnen == False):
        Benutzerzahl = input("Welche Zahl? ")
        Benutzerzahl = int(Benutzerzahl)
        versuche += 1
        if (Benutzerzahl == zufallszahl):
            gewonnen = True
        if (Benutzerzahl < zufallszahl):
            print("Die Zufallszahl ist groesser!")
        if(Benutzerzahl > zufallszahl):
            print("Die Zufallszahl ist kleiner!")

print("Bravo du hast die Zahl mit ", versuche, " Versuche erraten")