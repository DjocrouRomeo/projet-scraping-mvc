import os

SITE = "amazon_local"   # "amazon", "amazon_local" ou "test"

URLS = {
    "amazon": "https://www.amazon.fr/s?k=smartphone&i=electronics",
    "amazon_local": "file:///" + os.path.abspath("data/page_smartphone.html").replace("\\", "/"),
    "test": "https://webscraper.io/test-sites/e-commerce/static/computers/laptops",
}
BASE_URL = URLS[SITE]

MAX_PAGES = 1
DELAI = 3
EXPORT_DIR = "exports"
FICHIER_EXPORT = "produits_tech.csv"
DB_PATH = os.path.abspath(os.path.join("data", "produits.db"))