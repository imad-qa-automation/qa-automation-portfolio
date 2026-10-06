# Exercice 1 - Valider un email avecen utilisant une fonction
def valider_email (email):
    if "@" in email and "." in email: 
        return "valid"
    else:
        return "invalid"
    
print(valider_email("imad@test.com"))
print(valider_email("sansarobase.com"))
print(valider_email(""))

# Exercice 2 - valider un password en utilisant une fonction

def valider_password (password) :
    if len(password) >= 8 and password != "" : 
        return "Mot de passe valide"
    else:
        return "Mot de passe invalide"

print(valider_password("abc123"))
print(valider_password("abc12345"))
print(valider_password(""))

# Exercice 3 - calculer TTC en utilisant une fonction

def calculer_ttc(prix_ht, tva=0.2):
    prix_ttc = prix_ht + (prix_ht * tva)
    return f"Prix TTC : {prix_ttc}"

print(calculer_ttc(100))
print(calculer_ttc(100, 0.14))
print(calculer_ttc(200))


