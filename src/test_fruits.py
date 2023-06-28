from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    driver = Chrome()
    driver.get("https://labasse.github.io/fruits/")
    
def teardown_function():
    driver.quit()

def test_init_titre():
    assert driver.title == "Salade de fruits"

def test_init_chercher_actif():
    chercher = driver.find_element(By.LINK_TEXT, "Chercher")
    assert "active" in chercher.get_attribute("class")

def test_init_liste_complete():
    cartes = driver.find_elements(By.CLASS_NAME, "card")
    assert len(cartes) == 11

def test_init_focus_recherche():
    recherche = driver.find_element(By.CSS_SELECTOR, "input[type=search]")
    assert recherche == driver.switch_to.active_element
