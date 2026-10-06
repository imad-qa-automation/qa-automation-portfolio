from pages.login_page import LoginPage

def test_login_invalide(page):
    login= LoginPage(page)
    login.naviguer()
    login.se_connecter("mauvais@email.com", "mauvaismdp")
    assert "login" in login.obtenir_url()
    assert page.get_by_text("Your email or password is incorrect!").is_visible()