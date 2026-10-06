import json 
with open("data/utilisateurs.json", encoding="utf-8") as f : 
    utilisateurs = json.load(f)

    reponse_api = '{"data": {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver"}}'
    data= json.loads(reponse_api)

#for utilisateur in utilisateurs :
    print(f"{ data['data'] ['id']} - {data['data']['email']} - {data['data']['first_name']} - {data['data']['last_name']}")
  # print(f"{utilisateur['id']} - {utilisateur['adresse']['ville']} - {utilisateur['adresse'] ['pays']}")