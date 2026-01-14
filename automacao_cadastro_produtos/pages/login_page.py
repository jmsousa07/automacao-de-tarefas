from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def acessar(self, url):
        self.driver.get(url)

    def fazer_login(self, email, senha):
        self.wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(senha)
        self.wait.until(EC.element_to_be_clickable((By.ID, "pgtpy-botao"))).click()
