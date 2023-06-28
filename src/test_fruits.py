from selenium.webdriver import Chrome

def setup_function():
    global driver
    driver = Chrome()

def teardown_function():
    driver.quit()

def test_init_titre():
    driver.get("https://labasse.github.io/fruits/")
    assert driver.title == "Salade de fruits"

def test_init_chercher_actif():
    pass

def test_init_liste_complete():
    pass

def test_init_focus_recherche():
    pass
