import time
from selenium.webdriver.common.by import By
from app.scraper.driver import creer_driver
from config import BASE_URL

d = creer_driver(headless=True, sans_js=True)
d.get(BASE_URL)
time.sleep(3)

cartes = d.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
print("cartes :", len(cartes))
print("h2 sur la page :", len(d.find_elements(By.CSS_SELECTOR, "h2")))

for n, c in enumerate(cartes[:3], start=1):
    print(f"--- carte {n} ---")
    print("h2 :", len(c.find_elements(By.CSS_SELECTOR, "h2")))
    print("prix :", len(c.find_elements(By.CSS_SELECTOR, "span.a-price span.a-offscreen")))
    print("TEXTE :", c.get_attribute("textContent").strip()[:200])

if cartes:
    print("HTML carte 1 :", cartes[0].get_attribute("outerHTML")[:1500])

d.quit()