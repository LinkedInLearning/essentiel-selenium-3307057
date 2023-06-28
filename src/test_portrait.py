from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    driver = Chrome()
    driver.get("https://labasse.github.io/fruits/portrait.html")

def teardown_function():
    driver.quit()

def test_selection_partie():
    partie = driver.find_element(By.ID, "partie")
    
    # Sélectionner Œil
    
    fruits = driver.find_elements(By.CSS_SELECTOR, "#palette .fruit")
    ids = [f.get_attribute("id") for f in fruits]
    assert ids == ["1-3", "3-1", "2-1"]

