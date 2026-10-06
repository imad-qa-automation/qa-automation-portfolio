import json 

reponse_api = '{"data": {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver"}}'
data= json.loads(reponse_api)


print(f"ID : {data['data']['id']}")
print(f"Email : {data['data']['email']}")
print(f"Prénom : {data['data']['first_name']}")
print(f"Nom : {data['data']['last_name']}")