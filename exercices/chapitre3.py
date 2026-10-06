#Chapitre 3 — Boucles

#  Parcourrir un tab

utilisateurs = ["imad@test.com", "sara@test.com", "admin@test.com"]

for utilisateur in utilisateurs :
    print(utilisateur)

# Valider un tableau des emails

emails = ["imad@test.com", "sansarobase.com", "", "sara@test.com"]

for email in emails :
    if "@" in email and "." in email :
        print(f"{email} valide")
    else :
        print(f"{email} invalide") 
    
# Exercice 3 -  Boucle sur codes HTTP

codes = [200, 201, 404, 500, 301]

for code in codes :
    if code == 200 or code == 201:
        print (f"{code} - Succès")
    elif code == 404 : 
        print (f"{code} - Not found")
    elif code == 500 : 
        print (f"{code} - Server error")
    else : 
        print (f"{code} - Autre !! ")