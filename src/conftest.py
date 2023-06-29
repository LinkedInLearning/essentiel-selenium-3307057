def pytest_addoption(parser):
    parser.addini("selenium_driver", default="chrome", help="Driver à utiliser")
    parser.addini("selenium_hub"   , default="", help="Addresse du hub ou vide")
    parser.addini("selenium_mobile", default="", help="Appareil mobile ou vide")