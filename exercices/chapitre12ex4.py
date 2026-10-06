import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/9999")

if response.status_code == 404:
    print(f" Status: {response.status_code}")
    print(f" ❌ Utilisateur introuvable")