import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_panier(page):
    page.goto("https://automationexercise.com/product_details/1")
    page.get_by_role("button", name="Add to cart").click()
    # Attendre que la modal apparaisse
    page.wait_for_selector(".modal-body")
    assert page.get_by_text("Your product has been added to cart.").is_visible()

def test_verifier_panier(page):
    page.goto("https://automationexercise.com/product_details/1")
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    assert page.get_by_role("link", name="Blue Top").is_visible()

def test_supprimer_panier(page):
    page.goto("https://automationexercise.com/product_details/1")
    page.get_by_role("button", name="Add to cart").click()
    page.wait_for_selector(".modal-body")
    page.get_by_role("link", name="View Cart").click()
    page.locator("a.cart_quantity_delete").click()
    # Attendre que le produit disparaisse
    page.wait_for_selector("a.cart_quantity_delete", state="hidden")
    assert page.locator("a.cart_quantity_delete").count() == 0
    
    