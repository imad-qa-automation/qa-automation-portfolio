# Exercice 1 - les listes (tableau)

utilisateurs = ["imad@test.com", "sara@test.com", "admin@test.com"]

# Afficher tous les utilisateurs
for utilisateur in utilisateurs :
    print(utilisateur)

# Ajouter un utilisateur
utilisateurs.append("nouveau@test.com")
print(f"Total utilisateurs : {len(utilisateurs)}") 

# Exercice 2 - Dictionnaire utilisateur
utilisateur = {
    "nom": "Imad-Eddine",
    "email": "imad@test.com",
    "role": "admin",
    "actif": True
}

# Afficher les infos
print(utilisateur["nom"])
print(utilisateur["email"])
print(utilisateur["role"])

# Modifier le role
utilisateur["role"] = "user"
print(f"Nouveau role : {utilisateur['role']}")

# Parcourir tout le dictionnaire
for cle, valeur in utilisateur.items():
    print(f"{cle} : {valeur}")

# Exercice 3 — Données de test multiples

utilisateurs = [
    {"email": "imad@test.com", "password": "abc12345", "role": "admin"},
    {"email": "sara@test.com", "password": "xyz98765", "role": "user"},
    {"email": "invité",        "password": "",          "role": "guest"},
]

for utilisateur in utilisateurs:
    print(f"Email : {utilisateur['email']} | Role : {utilisateur['role']}")