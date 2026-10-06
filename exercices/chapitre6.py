email = "IMAD@TEST.COM"

email_lower = email.lower()

print(email_lower)
    
if "@" and "." in email_lower :
    print (f"{email_lower} - valide")
else : 
    print(f"{email_lower} - invalide")

base_url = "http://reqres.in"
endpoint = "users"
user_id = 2

url = f"{base_url}/api/{endpoint}/{user_id}"
print(f"URL généré : {url}")

from datetime import datetime

email = f"test_{datetime.now().strftime('%H%M%S')}@mail.com"
print(f"Email généré : {email}")
