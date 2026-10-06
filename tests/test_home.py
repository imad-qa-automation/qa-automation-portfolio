import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_home(page):
    page.goto("https://automationexercise.com")
   
    assert page.title() in "Automation Exercise"
    assert page.get_by_alt_text("Website for automation practice").is_visible()
    assert page.get_by_role("link", name="Home").is_visible()
   