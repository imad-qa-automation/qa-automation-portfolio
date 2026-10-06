# Exercice 1 - Validation code HTTP
status_code = 404

if status_code == 200 : 
    print("OK - Test passé")
elif status_code == 404 :
    print("Not found - Page intruovable")
elif status_code == 500 :
    print("Server error - Erreur serveur")
else:
    print("Code inconnu")

# Exercice 2 - Validation mot de passe
password = ""

if len (password) >= 8 and password != "" :
     print("Mot de passe valide ")
else:
    print("Mot de passe trop court ") 

# Exercice 3 - Validation email
email = ""

if "@" in email and "." in email: 
    print("Email valid")
else:
    print("Email invalid")







