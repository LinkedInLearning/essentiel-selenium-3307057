from selenium.webdriver import Chrome

def setup_function():
    global driver
    driver = Chrome()

def teardown_function():
    driver.quit()

def test_title():
    driver.get("https://labasse.github.io/fruits/")
    assert driver.title == "Salade de fruits"