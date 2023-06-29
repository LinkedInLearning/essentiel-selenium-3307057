from selenium.webdriver import Chrome, Firefox, Edge, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from os import path
import json, math

class Page:
    def __init__(self, driver: Chrome or Firefox or Edge, baseurl: str):
        """ Charge la page grâce au driver selenium en partant de l'url spécifié """
        self.driver = driver
        self.url_portrait = f"{baseurl}/portrait.html"
        self.driver.get(self.url_portrait)
        self._maj_cache()

    def _maj_cache(self):
        """ Met à jour les objets cherchés par avance ie. en cache """
        self.taille   = self.driver.find_element(By.ID, "taille")
        self.canevas  = self.driver.find_element(By.ID, "canevas")

    def glisser_deplacer(self, id: str) -> None:
        """ Déplace le fruit d'identifiant id au centre du portrait """
        ActionChains(self.driver).drag_and_drop(
            self.driver.find_element(By.ID, id),
            self.driver.find_element(By.ID, "canevas")
        ).perform()

    def glisser_fruit(self, id: str, x: int, y: int, zoom: int) -> None:
        """ Glisse le fruit d'identifiant id à l'offset x, y du portrait avec le zoom spécifié """
        fruit = self.driver.find_element(By.ID, id)
        dx = self.canevas.location['x'] + x - fruit.location['x']
        dy = self.canevas.location['y'] + y - fruit.location['y']
        ActionChains(self.driver)\
            .drag_and_drop_by_offset(fruit, dx, dy)\
            .send_keys_to_element(self.taille, Keys.HOME+Keys.ARROW_RIGHT*zoom)\
            .perform()
    
    def redimmensionner(self, largeur: int, hauteur: int) -> None:
        """ Redimensionne la page aux largeur et hauteur spécifiées """
        self.driver.set_window_size(largeur, hauteur)

    def lire_js_fruits(self) -> dict:
        """ Retourne un dictionnaire de la donnée interne javascript 'fruits'  """
        return json.loads(self.driver.execute_script("return JSON.stringify(fruits)"))
    
    def deselectionner(self) -> None:
        """ Désélectionne le fruit sur le portrait """
        self.driver.execute_script("select(null)")

    def fruits_du_portrait(self) -> list[WebElement]:
        """ Retourne une liste des div correspondant aux fruits qui composent le portrait """
        return self.driver.find_elements(By.CSS_SELECTOR, "div.fruit")
    
    def fruits_de_la_palette(self) -> list[WebElement]:
        """ Retourne une liste des li correspondant aux fruits qui composent la palette """
        return self.driver.find_elements(By.CSS_SELECTOR, "#palette .fruit")
    
    def filtrer_palette(self, filtre: str) -> None:
        """ Filtre les fruits de la palette, 'Tout' pour retirer le filtre """
        Select(self.driver.find_element(By.ID, "partie")).select_by_visible_text(filtre)

    def get_titre(self) -> WebElement:
        """ Retourne le composant 'Titre' de la page """
        return self.driver.find_element(By.NAME, "titre")
    
    def get_taille(self) -> WebElement:
        """ Retourne le composant 'Taille' de la page """
        return self.driver.find_element(By.ID, "taille")
    
    def get_texte_taille(self) -> str:
        """ Retourne le texte du composant 'Taille' de la page """
        return self.driver.find_element(By.ID, "valeur").text

    def charger_fond(self, fichier: str) -> None:
        """ Charge l'image spécifiée pour le fond du portrait """
        self.driver.find_element(By.ID, "fond").send_keys(path.abspath(fichier))

    def _coin(self, delta: int, taille: int) -> int:
        """ Détermine la coordonnée extrême à utiliser en 
            fonction de la dimension du portrait et du signe du delta 
        """
        return (5-taille/2)*math.copysign(1, delta) 

    def deplacer_fond(self, dx: int, dy: int) -> None:
        """ Décale le fond du portrait à la souris de la distance spécifiée par dx et dy """
        coin_x = self._coin(self.canevas.rect['width' ], dx)
        coin_y = self._coin(self.canevas.rect['height'], dy)
        ActionChains(self.driver)\
            .move_to_element_with_offset(self.canevas, coin_x, coin_y)\
            .click_and_hold(None)\
            .move_by_offset(dx, dy)\
            .release()\
            .perform()
    
    def recharger(self) -> None:
        """ Charge ou rafrîchit la page """
        pass
