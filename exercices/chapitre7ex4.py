import json
resultats = [
    {"test": "test_login", "statut": "passed", "duree": 3.89 },
    {"test": "test_inscription", "statut": "failed", "duree": 5.12 }
]

with open("data/resultats.json", "w", encoding= "utf-8") as f:
    json.dump(resultats, f, indent= 4)

with open("data/resultats.json", encoding="utf-8") as f :
    resultats = json.load(f)

for resultat in resultats:
    print(f" {resultat ['test']} : {resultat['statut']}")
    

