import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_logout(page):
    login= LoginPage(page)
    login.naviguer()
    login.se_connecter(
        os.getenv("TEST_EMAIL"),
        os.getenv("TEST_PASSWORD"))
    login.se_deconnecter()
    assert "login" in login.obtenir_url()
 

