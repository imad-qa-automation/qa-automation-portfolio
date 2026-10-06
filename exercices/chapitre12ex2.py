import requests

nouvel_utilisateur = {
    "name": "Imad-Eddine",
    "username": "imad_qa",
    "email" : "imad@test.com"
}

response = requests.post("https://jsonplaceholder.typicode.com/users", json=nouvel_utilisateur)
# Données à envoyer

# Status code
print(f"Status : {response.status_code}")

data = response.json()
print(f"ID : {data['id']}")
print(f"Nom : {data['name']}")