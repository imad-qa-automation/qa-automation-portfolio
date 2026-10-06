import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/2")
data = response.json()

assert response.status_code == 200 
print("✅ Status 200 OK")

assert "@" in data["email"]
print("✅ Email valide")

assert data["name"] != ""
print("✅ Nom non vide")

 