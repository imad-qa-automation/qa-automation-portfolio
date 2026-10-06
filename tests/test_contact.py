import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_contact(page):
    # Gérer la dialog automatiquement
    page.on("dialog", lambda dialog: dialog.accept())
    page.goto("https://automationexercise.com/contact_us")
    page.get_by_placeholder("Name").fill("Imad-Eddine")
    page.get_by_role("textbox", name="Email", exact=True).fill("imad@test.com")
    page.get_by_placeholder("Your Message Here").fill("Test message")
    page.get_by_role("button", name="Submit").click()
    page.wait_for_timeout(2000)  # attendre 2 secondes
    assert page.locator("#contact-page").get_by_text("Success! Your details have been submitted successfully.").is_visible()
    