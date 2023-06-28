from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def setup_function():
    global driver
    driver = Chrome()
    driver.get("https://labasse.github.io/fruits/portrait.html")

def teardown_function():
    driver.quit()

def test_selection_partie():
    partie = Select(driver.find_element(By.ID, "partie"))
    
    partie.select_by_visible_text("Œil")
    
    fruits = driver.find_elements(By.CSS_SELECTOR, "#palette .fruit")
    ids = [f.get_attribute("id") for f in fruits]
    assert ids == ["1-3", "3-1", "2-1"]

def test_diminution_taille():
    """ Test de la diminution de la valeur à 3 """
    taille = driver.find_element(By.ID, "taille")
    # Action pour passer à 3
    assert driver.find_element(By.ID, "valeur").text == str(3)

def test_augmentation_taille():
    """ Test de l'augmentation de la valeur à 8 """
    pass

def test_minimum_taille():
    """ Test du passage à la valeur minimale: 0 """
    pass

def test_maximum_taille():
    """ Test du passage à la valeur maximale: 9 """
    pass
