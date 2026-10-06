from pages.signup_page import SignupPage

def test_signup(page):
    signup= SignupPage(page)
    signup.naviguer()
    signup.remplir_signup("imad", "imad@test.com")
    signup.soumettre()
    assert "signup" in signup.obtenir_url()
