class SignupPage:
    
    def __init__(self, page):   # constructeur — s'exécute automatiquement
        self.page = page        # stocker la référence à la page
    
    def naviguer(self):         # méthode - va sur /login
        self.page.goto("https://automationexercise.com/login")

    def remplir_signup(self, nom, email):
        self.page.get_by_placeholder("Name").fill(nom)
        self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(email)

    def soumettre(self):
        self.page.get_by_role("button", name="Signup").click()
    
    def obtenir_url(self):      # obtenir un url 
        return self.page.url
