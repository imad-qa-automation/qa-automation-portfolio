import requests

# Appeler une API gratuite
response = requests.get("https://jsonplaceholder.typicode.com/users/2")

# Status code
print(f"Status : {response.status_code}")

# Affiche tous json
#print(response.json())

# Affiche Prénom et email
data = response.json()
print(f"Nom : {data['name']}")
print(f"Email : {data['email']}")




