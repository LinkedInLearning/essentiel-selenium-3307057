import sys
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def main() -> int:
    """ Extraction des fruits du site et de leur description """
    url = "https://labasse.github.io/fruits/"
    driver = Chrome()
    driver.get(url)
    cartes = driver.find_elements(By.CLASS_NAME, "card")
    for c in cartes:
        nom = c.find_element(By.CLASS_NAME, "card-title").text
        img = c.find_element(By.TAG_NAME, "img").get_attribute("src")[len(url):]
        txt = c.find_element(By.CLASS_NAME, "card-text" ).text
        print(f"- {nom: <10}{img:<20}{txt}")
    return 0

if __name__ == '__main__':
    sys.exit(main()) 