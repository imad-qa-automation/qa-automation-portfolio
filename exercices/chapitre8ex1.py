import json
try :
    with open("data/fichier_introuvabl.json", encoding = "utf-8") as f:
        fichier_introuvable = json.load(f)
except FileNotFoundError :
    print(f"Fichier introuvable")



