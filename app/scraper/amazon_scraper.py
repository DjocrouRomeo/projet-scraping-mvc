import time
from selenium.webdriver.common.by import By
from config import DELAI
from app.scraper.parsing import parser_page

class AmazonScraper:
    def __init__(self, driver):
        self.driver = driver

    def scraper(self, url, pages):
        produits = []
        for numero in range(1, pages + 1):
            if numero == 1:
                adresse = url
            else:
                separateur = "&" if "?" in url else "?"
                adresse = f"{url}{separateur}page={numero}"
            self.driver.get(adresse)
            time.sleep(DELAI)

            cartes = self.driver.find_elements(
                By.CSS_SELECTOR, "div[data-component-type='s-search-result']"
            )
            print("Adresse chargée :", self.driver.current_url)
            print("Titre de la page :", self.driver.title)
            print("Cartes vues par Selenium :", len(cartes))

            trouves = parser_page(self.driver)
            print("Produits lus par parser_page :", len(trouves))
            if not trouves:
                break
            produits.extend(trouves)
        return produits