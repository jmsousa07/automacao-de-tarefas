from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CadastroPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def preencher_campo(self, nome, valor):
        campo = self.wait.until(EC.presence_of_element_located((By.NAME, nome)))
        campo.clear()
        campo.send_keys(valor)

    def cadastrar_produto(self, produto):
        self.preencher_campo("codigo", produto["codigo"])
        self.preencher_campo("marca", produto["marca"])
        self.preencher_campo("tipo", produto["tipo"])
        self.preencher_campo("categoria", produto["categoria"])
        self.preencher_campo("preco_unitario", produto["preco_unitario"])
        self.preencher_campo("custo", produto["custo"])
        self.preencher_campo("obs", produto["obs"])

        self.wait.until(EC.element_to_be_clickable((By.ID, "pgtpy-botao"))).click()
