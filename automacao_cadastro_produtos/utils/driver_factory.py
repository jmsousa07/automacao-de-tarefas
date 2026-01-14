from selenium import webdriver

def criar_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
