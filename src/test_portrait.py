from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip, portrait

def _test_changement_de_taille(raccourci, valeur):
    page.get_taille().send_keys(raccourci)
    assert page.get_texte_taille() == str(valeur)

def setup_function():
    global driver, page
    driver = Chrome()
    page = portrait.Page(driver, "https://labasse.github.io/fruits")
    
def teardown_function():
    driver.quit()

def test_selection_partie():
    """ Test de la sélection d'Œil """
    page.filtrer_palette("Œil")
    ids = [f.get_attribute("id") for f in page.fruits_de_la_palette()]
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
    page.charger_fond("banner.jpg")
    assert "data:image/jpeg;base64" in driver.find_element(By.ID, "canevas").get_attribute("style")

def test_glisser_deplacer_fruit_sur_canevas():
    """ Glisser/Déplace le premier fruit de la palette sur le Canevas """
    page.glisser_deplacer("0-0")
    portrait = page.fruits_du_portrait()
    assert len(portrait)==1
    assert "cur" in portrait[0].get_attribute("class")

def test_coller_titre():
    """ Test de collage du presse-papier dans titre """
    pyperclip.copy("Hommage à Arcimboldo")
    titre = page.get_titre()
    titre.send_keys(Keys.CONTROL, "v")
    assert titre.get_attribute('value') == "Hommage à Arcimboldo"

def test_js_select():
    """ Test de la désélection javascript select(null) """
    page.glisser_deplacer("0-0")
    page.deselectionner()
    portrait = page.fruits_du_portrait()
    assert "cur" not in portrait[0].get_attribute("class")

def test_lecture_donnees_javascript():
    """ Test du contenu de la variable fruit """
    page.redimmensionner(1280, 720)
    page.glisser_deplacer("0-0")
    donnees_fruits = page.lire_js_fruits()
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
    page.redimmensionner(1280, 720)
    page.charger_fond("banner.jpg")
    page.deplacer_fond(-200, -100)
    page.glisser_fruit("4-2",  18,  68, 9)
    page.glisser_fruit("2-0", 163, 203, 7)
    page.glisser_fruit("1-2", 162, 269, 7)
    page.glisser_fruit("1-3",  92, 145, 6)
    page.glisser_fruit("1-3", 253, 145, 6)
    page.deselectionner()
    driver.save_screenshot("dessin.png")

def test_aller_retour_dessin_vide():
    page.glisser_deplacer("0-0")
    # Aller sur "https://labasse.github.io/fruits"
    page.recharger() 
    assert len(page.fruits_du_portrait()) == 0

def test_rafraichir_dessin_vide():
    page.glisser_deplacer("0-0")
    page.recharger()
    assert len(page.fruits_du_portrait()) == 0
