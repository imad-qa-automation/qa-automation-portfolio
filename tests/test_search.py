import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_search(page):
    page.goto("https://automationexercise.com/products")
    page.get_by_placeholder("Search Product").fill("dress")
    page.locator("#submit_search").click()
    assert "search" in page.url

def test_resultats_recherche(page):
    page.goto("https://automationexercise.com/products")
    page.get_by_placeholder("Search Product").fill("dress")
    page.locator("#submit_search").click()
    assert page.get_by_text("Searched Products").is_visible()
    assert page.locator(".product-overlay").count() > 0
