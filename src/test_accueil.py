# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAccueil():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_accueilRecherchefructueuse(self):
    # Test name: Accueil - Recherche fructueuse
    # Step # | name | target | value
    # 1 | open | /fruits/ | 
    self.driver.get("https://labasse.github.io/fruits/")
    # 2 | setWindowSize | 1280x720 | 
    self.driver.set_window_size(1280, 720)
    # 3 | click | css=.form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    # 4 | type | css=.form-control | ana
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("ana")
    # 5 | storeXpathCount | xpath=//div[contains(@class, "card ")] | cartes
    self.vars["cartes"] = len(self.driver.find_elements(By.XPATH, "//div[contains(@class, \"card \")]"))
    # 6 | assert | cartes | 2
    assert(self.vars["cartes"] == 2)
  
  def test_accueilRechercheinfructueuse(self):
    # Test name: Accueil - Recherche infructueuse
    # Step # | name | target | value
    # 1 | open | /fruits/ | 
    self.driver.get("https://labasse.github.io/fruits/")
    # 2 | setWindowSize | 1280x720 | 
    self.driver.set_window_size(1280, 720)
    # 3 | click | css=.form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    # 4 | type | css=.form-control | toto
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("toto")
    # 5 | assertElementNotPresent | css=.row-cols-1 > .col | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".row-cols-1 > .col")
    assert len(elements) == 0
  
