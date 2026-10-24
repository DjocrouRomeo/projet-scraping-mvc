import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

produits = {
    "MSI Katana 17": "https://www.amazon.fr/dp/B097PN92BN",
    "adidas F50 Club": "https://www.amazon.fr/dp/B0F1X3SG7N",")"
    "PlayStation 5": "https://www.amazon.fr/dp/B0FP2S1MNB",
}

driver = webdriver.Chrome()
resultats = []

for nom, url in produits.items():
    driver.get(url)
    time.sleep(4)


    try:
        titre = driver.find_element(By.ID, "productTitle").text.strip()
    except Exception:
        titre = None


    prix = None
    for sel in ["#corePrice_feature_div .a-offscreen", ".a-price .a-offscreen"]:
        try:
            prix = driver.find_element(By.CSS_SELECTOR, sel).get_attribute("textContent").strip()
            #vue que  l’élément .a-offscreen est masqué on utilise get_attribute("textContent") car .text renverrait une chaîne vide.
            if prix:
                break
        except Exception:
            pass
    if not prix:
        prix = "Indisponible"

    # Disponibilitéd
    try:
        dispo = driver.find_element(By.ID, "availability").text.strip()
    except Exception:
        dispo = None

    resultats.append({"produit": nom, "titre": titre, "prix": prix, "dispo": dispo, "url": url})
    print(f"{nom} | {prix} | {dispo}")

driver.quit()

# Export CSV
with open("produits_amazon.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["produit", "titre", "prix", "dispo", "url"])
    writer.writeheader()
    writer.writerows(resultats)

print("Fichier produits_amazon.csv créé.")