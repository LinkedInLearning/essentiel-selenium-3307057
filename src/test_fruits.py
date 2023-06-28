from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setup_function():
    global driver
    driver = Chrome()
    driver.get("https://labasse.github.io/fruits/")
    
def teardown_function():
    driver.quit()

def find_recherche():
    return driver.find_element(By.CSS_SELECTOR, "input[type=search]")

def ecrire_recherche(texte):
    recherche = find_recherche()
    recherche.click()
    recherche.send_keys(texte)
    return recherche

def assert_nombre_cartes(attendu):
    cartes = driver.find_elements(By.CLASS_NAME, "card")
    assert len(cartes) == attendu

def test_init_titre():
    assert driver.title == "Salade de fruits"

def test_init_chercher_actif():
    chercher = driver.find_element(By.LINK_TEXT, "Chercher")
    assert "active" in chercher.get_attribute("class")

def test_init_liste_complete():
    assert_nombre_cartes(11)

def test_init_focus_recherche():
    recherche = find_recherche()
    assert recherche == driver.switch_to.active_element

def test_recherche_fructueuse():
    ecrire_recherche("ana")
    assert_nombre_cartes(2)

def test_recherche_infructueuse():
    ecrire_recherche("radis")
    assert_nombre_cartes(0)

def test_recherche_raz():
    recherche = ecrire_recherche("radis")
    for i in range(5):
        recherche.send_keys(Keys.BACKSPACE)
    assert_nombre_cartes(11)
