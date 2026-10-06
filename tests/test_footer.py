import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_footer(page):
    page.goto("https://automationexercise.com/")
    assert page.get_by_text("SUBSCRIPTION").is_visible()
    assert page.get_by_text("Copyright © 2021 All rights reserved").is_visible()
    # assert page.locator("#contact-page").get_by_text("Success! Your details have been submitted successfully.").is_visible()