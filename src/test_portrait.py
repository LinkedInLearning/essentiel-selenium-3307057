from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from os import path

def _test_changement_de_taille(raccourci, valeur):
    taille = driver.find_element(By.ID, "taille")
    taille.send_keys(raccourci)
    assert driver.find_element(By.ID, "valeur").text == str(valeur)

def setup_function():
    global driver
    driver = Chrome()
    driver.get("https://labasse.github.io/fruits/portrait.html")

def teardown_function():
    driver.quit()

def test_selection_partie():
    """ Test de la sélection d'Œil """
    partie = Select(driver.find_element(By.ID, "partie"))
    
    partie.select_by_visible_text("Œil")
    
    fruits = driver.find_elements(By.CSS_SELECTOR, "#palette .fruit")
    ids = [f.get_attribute("id") for f in fruits]
    assert ids == ["1-3", "3-1", "2-1"]

def test_diminution_taille():
    """ Test de la diminution de la valeur à 3 """
    _test_changement_de_taille(Keys.ARROW_LEFT*2, 3)

def test_augmentation_taille():
    """ Test de l'augmentation de la valeur à 8 """
    _test_changement_de_taille(Keys.ARROW_RIGHT*3, 8)

def test_minimum_taille():
    """ Test du passage à la valeur minimale: 0 """
    _test_changement_de_taille(Keys.HOME, 0)

def test_maximum_taille():
    """ Test du passage à la valeur maximale: 9 """
    _test_changement_de_taille(Keys.END, 9)

def test_televersement_fond():
    """ Test du téléversement d'une image de fond """
    fond = driver.find_element(By.ID, "fond")
    fond.send_keys(path.abspath("banner.jpg"))
    assert "data:image/jpeg;base64" in driver.find_element(By.ID, "canevas").get_attribute("style")