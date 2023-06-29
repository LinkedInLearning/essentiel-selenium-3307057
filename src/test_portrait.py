from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from os import path
import pyperclip, json, portrait

def _test_changement_de_taille(raccourci, valeur):
    taille = driver.find_element(By.ID, "taille")
    taille.send_keys(raccourci)
    assert driver.find_element(By.ID, "valeur").text == str(valeur)

def setup_function():
    global driver, page
    driver = Chrome()
    page = portrait.Page(driver, "https://labasse.github.io/fruits")
    
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

def test_glisser_deplacer_fruit_sur_canevas():
    """ Glisser/Déplace le premier fruit de la palette sur le Canevas """
    fruit   = driver.find_element(By.ID, "0-0")
    canevas = driver.find_element(By.ID, "canevas")
    
    actions = ActionChains(driver)
#    actions.drag_and_drop(fruit, canevas).perform()
    actions.drag_and_drop_by_offset(fruit,
        canevas.rect['x'] + canevas.rect['width' ]/2 - fruit.location['x'], 
        canevas.rect['y'] + canevas.rect['height']/2 - fruit.location['y']
    ).perform()
    portrait = driver.find_elements(By.CSS_SELECTOR, "div.fruit")
    assert len(portrait)==1
    assert "cur" in portrait[0].get_attribute("class")

def test_coller_titre():
    """ Test de collage du presse-papier dans titre """
    pyperclip.copy("Hommage à Arcimboldo")
    titre = driver.find_element(By.NAME, "titre")
    titre.send_keys(Keys.CONTROL, "v")
    assert titre.get_attribute('value') == "Hommage à Arcimboldo"

def test_js_select():
    """ Test de la désélection javascript select(null) """
    page.glisser_deplacer("0-0")
    driver.execute_script("select(null)")
    portrait = driver.find_elements(By.CSS_SELECTOR, "div.fruit")
    assert "cur" not in portrait[0].get_attribute("class")

def test_lecture_donnees_javascript():
    """ Test du contenu de la variable fruit """
    driver.set_window_size(1280, 720)
    page.glisser_deplacer("0-0")
    donnees_fruits = json.loads(driver.execute_script("return JSON.stringify(fruits)"))
    assert donnees_fruits == {
        "f1": {
            "icone":"0-0",
            "sprite":["0","0"],
            "taille":2,
            "x":167, "y":219
        }
    }    

def test_dessin_complexe():
    """ Test d'un dessin complexe avec capture du résultat """
    driver.set_window_size(1280, 720)
    taille   = driver.find_element(By.ID, "taille")
    canevas  = driver.find_element(By.ID, "canevas")

    page.glisser_fruit("4-2",  18,  68, 9)
    page.glisser_fruit("2-0", 163, 203, 7)
    page.glisser_fruit("1-2", 162, 269, 7)
    page.glisser_fruit("1-3",  92, 145, 6)
    page.glisser_fruit("1-3", 253, 145, 6)
    driver.execute_script("select(null)")
    driver.find_element(By.ID, "fond").send_keys(path.abspath("banner.jpg"))
    driver.save_screenshot("dessing.jpg")