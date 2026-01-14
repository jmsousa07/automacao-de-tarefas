import logging
import os


def configurar_logger():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_dir = os.path.join(base_dir, "logs")

    os.makedirs(logs_dir, exist_ok=True)

    log_path = os.path.join(logs_dir, "execucao.log")

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()
