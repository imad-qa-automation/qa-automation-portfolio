import os
from dotenv import load_dotenv

load_dotenv()

class LoginPage:                # déclarer la classe
    def __init__(self, page):   # constructeur — s'exécute automatiquement
        self.page = page        # stocker la référence à la page
        self.email = os.getenv("TEST_EMAIL")
        self.password = os.getenv("TEST_PASSWORD")
        
    def naviguer(self):         # méthode 
        self.page.goto("https://automationexercise.com/login")

    def se_connecter(self, email, password):    # méthode avec paramètres (remplit et soumet le formulaire)
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def se_deconnecter(self):
        self.page.get_by_role("link", name="Logout").click()     
    
    def obtenir_url(self):      # obtenir un url 
        return self.page.url
    

