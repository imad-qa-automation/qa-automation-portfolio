from pages.login_page import LoginPage

import pytest

@pytest.mark.skip(reason="Test volontairement cassé - debugging")

def test_login_casse(page):
    try:
        login = LoginPage(page)
        login.naviguer()
        login.se_connecter("imad@test.com","motdepasse123")
        assert "dashboard" in login.obtenir_url()

    except Exception as e :
        page.screenshot(path="screenshots/echec.png")
        raise e
