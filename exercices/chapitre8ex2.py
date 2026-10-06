import json


try: 
    reponse_api = '{"id": 2, "email": "janet@reqres.in"'
    data = json.loads(reponse_api)

except json.JSONDecodeError :
    print(f"Erreur dans le code - JSON invalide ")

finally:
    print("Test terminé - avec ou sans erreur")