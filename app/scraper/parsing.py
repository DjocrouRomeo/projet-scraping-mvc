from selenium.webdriver.common.by import By
from app.models.produit import Produit
from config import SITE

def _texte(carte, selecteur):
    elements = carte.find_elements(By.CSS_SELECTOR, selecteur)
    if elements:
        texte = elements[0].get_attribute("textContent")
        return " ".join(texte.split())
    return ""

def _parser_amazon(driver):
    produits = []
    cartes = driver.find_elements(
        By.CSS_SELECTOR, "div[data-component-type='s-search-result']"
    )
    for carte in cartes:
        titre = _texte(carte, "h2")
        if not titre:
            continue
        prix = _texte(carte, "span.a-price span.a-offscreen")
        note = _texte(carte, "span.a-icon-alt")
        url = ""
        liens = carte.find_elements(By.CSS_SELECTOR, "a[href*='/dp/']")
        if liens:
            href = liens[0].get_dom_attribute("href") or ""
            url = "https://www.amazon.fr" + href if href.startswith("/") else href
        produits.append(Produit(titre, prix, note, url))
    return produits

def _parser_test(driver):
    produits = []
    for carte in driver.find_elements(By.CSS_SELECTOR, "div.card"):
        liens = carte.find_elements(By.CSS_SELECTOR, "a.title")
        if not liens:
            continue
        titre = liens[0].get_attribute("title") or liens[0].get_attribute("textContent").strip()
        url = liens[0].get_attribute("href") or ""
        prix = _texte(carte, ".price")
        notes = carte.find_elements(By.CSS_SELECTOR, "p[data-rating]")
        valeur = notes[0].get_attribute("data-rating") if notes else None
        note = f"{valeur}/5" if valeur else ""
        produits.append(Produit(titre, prix, note, url))
    return produits

def parser_page(driver):
    if SITE.startswith("amazon"):
        return _parser_amazon(driver)
    return _parser_test(driver)