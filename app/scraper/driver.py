from selenium import webdriver

def creer_driver(headless=False, sans_js=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    if sans_js:
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.javascript": 2}
        )
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--lang=fr-FR")
    return webdriver.Chrome(options=options)