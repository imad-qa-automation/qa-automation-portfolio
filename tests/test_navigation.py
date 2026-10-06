import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_navigation_produits(page):
    page.goto("https://automationexercise.com/products")
    assert page.get_by_role("heading", name="All Products").is_visible()
    assert page.locator(".product-image-wrapper").count() == 34
