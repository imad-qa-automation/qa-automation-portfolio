import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_product(page):
    # Aller directement sur la page produit — évite la pub !
    page.goto("https://automationexercise.com/product_details/1")
    #page.get_by_role("link", name="View Product").first.click()
    assert "product_details" in page.url
    assert page.get_by_role("heading", name="Blue Top").is_visible()