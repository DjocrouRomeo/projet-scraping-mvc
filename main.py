from config import SITE, BASE_URL, MAX_PAGES
from app.scraper.driver import creer_driver
from app.scraper.amazon_scraper import AmazonScraper
from app.models.depot import Depot
from app.views.console_view import ConsoleView
from app.views.export_view import ExportView
from app.controllers.scraping_controller import ScrapingController

def main():
    driver = creer_driver(headless=False, sans_js=(SITE == "amazon_local"))
    depot = Depot()
    try:
        controleur = ScrapingController(
            AmazonScraper(driver),
            depot,
            ConsoleView(),
            ExportView()
        )
        controleur.lancer(BASE_URL, MAX_PAGES)
    finally:
        depot.fermer()
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()