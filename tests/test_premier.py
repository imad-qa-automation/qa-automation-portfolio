def test_login(page):
    page.goto("https://automationexercise.com/")
    assert "Automation Exercise" in page.title()
    # Cliquer sur le bouton Login
    page.get_by_role("link", name="Signup / Login").click()
    # Remplir email
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("imad@test.com")
    # Remplir mot de passe
    page.get_by_placeholder("Password").fill("motdepasse123")
    # Cliquer sur Login
    page.get_by_role("button", name="Login").click()
    # Vérifier le résultat
    print(f"URL après login : {page.url}")
    assert "login" in page.url


