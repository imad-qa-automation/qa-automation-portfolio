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
    

    
  