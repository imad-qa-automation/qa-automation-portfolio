import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

from pages.login_page import LoginPage

def test_login_pom(page):
    login= LoginPage(page)
    login.naviguer()
    login.se_connecter("imad@test.com","motdepasse123")
    assert "login" in login.obtenir_url()