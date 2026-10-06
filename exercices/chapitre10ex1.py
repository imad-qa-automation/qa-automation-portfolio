class validateur :

# Valider un email en utilisant une fonction
    def valider_email(self, email):
        if "@" in email and "." in email:
         return True
        else: 
            return False   

# Valider un password en utilisant une fonction
    def valider_password(self, password):
        if len(password)>=8 and password != "":
         return True
        else:
            return False
test_class = validateur ()

print(f"imad@test.com -> {test_class.valider_email('imad@test.com')}")
print(f"saratest.ca -> {test_class.valider_email('saratest.ca')}") 
print(f"abc12345 → {test_class.valider_password('abc12345')}")
print(f"abc → {test_class.valider_password('abc')}")