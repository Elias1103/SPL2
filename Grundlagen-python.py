# grundlagen-python.py

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