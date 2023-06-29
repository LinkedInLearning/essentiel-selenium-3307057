from selenium.webdriver import Chrome,Edge
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

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

def test_recherche_completion():
    recherche = ecrire_recherche("abri")
    #WebDriverWait(driver, 6).until_not(cond.text_to_be_present_in_element_value(
    #    (By.CSS_SELECTOR, "input[type=search]"), "abri"
    #))
    WebDriverWait(driver, 6).until(lambda d : recherche.get_attribute("value")!="abri")
    assert find_recherche().get_attribute("value") == "Abricot"

def test_menu_cuisiner():
    try:
        driver.find_element(By.LINK_TEXT, "Cuisiner").click()
    except NoSuchElementException:
        # Pour Edge - écran restreint
        driver.find_element(By.CLASS_NAME, "navbar-toggler").click()
        WebDriverWait(driver, 10)\
            .until(cond.element_to_be_clickable((By.LINK_TEXT, "Cuisiner")))\
            .click()
    assert "#cuisiner" in driver.current_url