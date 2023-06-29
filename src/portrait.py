from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Page:
    def __init__(self, driver, baseurl):
        driver.get(f"{baseurl}/portrait.html")
        self.driver = driver
        self.taille   = driver.find_element(By.ID, "taille")
        self.canevas  = driver.find_element(By.ID, "canevas")

    def glisser_deplacer(self, id):
        ActionChains(self.driver).drag_and_drop(
            self.driver.find_element(By.ID, id),
            self.driver.find_element(By.ID, "canevas")
        ).perform()

    def glisser_fruit(self, id, x, y, zoom):
        fruit = self.driver.find_element(By.ID, id)
        dx = self.canevas.location['x'] + x - fruit.location['x']
        dy = self.canevas.location['y'] + y - fruit.location['y']
        ActionChains(self.driver)\
            .drag_and_drop_by_offset(fruit, dx, dy)\
            .send_keys_to_element(self.taille, Keys.HOME+Keys.ARROW_RIGHT*zoom)\
            .perform()