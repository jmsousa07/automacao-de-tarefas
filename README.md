# automacao-de-tarefas

Automação web em **Python + Selenium** que lê produtos de um CSV e os cadastra em lote em um
sistema web, estruturada em **Page Object Model**.

> **Projeto de estudo.** A URL usada pertence à Hashtag Treinamentos e serve apenas como
> ambiente de demonstração; as credenciais no código são fictícias.

## Estrutura

```
automacao_cadastro_produtos/
├── main.py                 # orquestração do fluxo
├── data/produtos.csv       # entrada
├── logs/execucao.log       # saída de log
├── pages/
│   ├── login_page.py       # Page Object: login
│   └── cadastro_page.py    # Page Object: cadastro
└── utils/
    ├── driver_factory.py   # criação do WebDriver
    ├── csv_reader.py       # leitura do CSV
    └── logger.py           # configuração de logging
```

## Decisões

- **Page Object Model** — seletores e interações ficam nas classes de página; `main.py` só
  orquestra. Trocar um seletor não exige mexer no fluxo.
- **Esperas explícitas** (`WebDriverWait` + `expected_conditions`) em vez de `sleep`.
- **Logging estruturado** com nível por evento (`info` / `error` / `critical`).
- **Tratamento por registro** — uma falha de cadastro é logada e o loop continua; o driver é
  encerrado no `finally` mesmo em erro crítico ou `KeyboardInterrupt`.

## Como rodar

```bash
pip install -r automacao_cadastro_produtos/requirements.txt
cd automacao_cadastro_produtos
python main.py
```

Requer Chrome e ChromeDriver compatíveis (Selenium 4.39).

## Licença

Apache License 2.0 — ver [LICENSE](LICENSE).
