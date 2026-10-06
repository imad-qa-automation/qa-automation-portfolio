import json 
with open("data/utilisateurs.json") as f : 
    utilisateurs = json.load(f)

for utilisateur in utilisateurs :
    print(f"{utilisateur['nom']} - {utilisateur['email']}")
