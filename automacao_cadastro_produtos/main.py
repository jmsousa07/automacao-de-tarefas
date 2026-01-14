from utils.driver_factory import criar_driver
from utils.csv_reader import ler_produtos
from utils.logger import configurar_logger
from pages.login_page import LoginPage
from pages.cadastro_page import CadastroPage
import os


URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "automation.example@gmail.com"
SENHA = "example123"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "produtos.csv")

def main():
    logger = configurar_logger()
    driver = criar_driver()

    try:
        logger.info("Iniciando automação")

        login_page = LoginPage(driver)
        cadastro_page = CadastroPage(driver)

        login_page.acessar(URL)
        login_page.fazer_login(EMAIL, SENHA)

        produtos = ler_produtos(CSV_PATH)
        logger.info(f"{len(produtos)} produtos encontrados")

        for produto in produtos:
            try:
                cadastro_page.cadastrar_produto(produto)
                logger.info(f"Produto cadastrado com sucesso: {produto['codigo']}")
            except Exception as e:
                logger.error(f"Erro ao cadastrar produto {produto['codigo']} - {e}")

    except KeyboardInterrupt:
        logger.warning("Execução interrompida manualmente pelo usuário")

    except Exception as erro_geral:
        logger.critical(f"Erro crítico na automação: {erro_geral}")

    finally:
        driver.quit()
        logger.info("Automação finalizada")


if __name__ == "__main__":
    main()
