# grundlagen-python.py
import random
siegera = 0
siegerb = 0

# Kommentare erfolgen mit hastag

# Ausgabe von Daten
print("Hallo Welt")

# Variable definineren (kann ohne Typen erfolgen)
heimat = "Erde"

# Mehrer Variable werden mit , getrennt
print(heimat, "an World:" , "Hallo!")

# Eingabe / liest Text (!) von der Konsole ein
wer = input("Und wer bist du?")

# und gibt den Text wieder aus
if(wer == "ich"):
    print("Hallo Du!")
else:
    print("Hallo",  wer)

lieblingszahl = input("Was ist deine Lieblingszahl?")
print("Super, ich mag die Zahl ", lieblingszahl)
print("Aber die coolere Zahl ", int(lieblingszahl)+10, "mag ich noch mehr!")

runden = input("Wie viele Runden sollen wir spielen? ")
runden = int(runden)

sieger = ""
siegerComputer = ""

for runde in range(1, runden+1):
    ## Zufallszahl erzeugen
    Zufallszahl = random.randint(1,6)
    ## ist die Zufallszahl 1,3 oder 5: bin ich der Gewinner
    ## sonst ist der Computer der Gewinner
    if (Zufallszahl == 1 or Zufallszahl == 3 or Zufallszahl == 5):
        sieger = "ich"
        siegera += 1
    else:
        sieger = "Computer"
        siegerb += 1    
    print("Runde" , runde, "von", runden, ": Sieger", sieger, ": gewuerfelte Zahl", Zufallszahl)
print("Ich habe gewonnen ", siegera)
print("Der Computer hat gewonnen" , siegerb)

if(siegera <= siegerb):
    print("Der Computer hat gewonnen")

elif(siegera == siegerb):
    print("Keiner hat gewonnen")
else:
    (siegerb <= siegera)
    print("Ich habe gewonnen!")
print("Game Over!")