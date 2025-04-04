# Projeto de Análise de Dados

Este projeto contém dois scripts Python para análise de dados:

1. `corpo_docente.py`: Scraper para extrair dados dos docentes do PPGTI do IFPB
2. `ibge.py`: Script para consumir a API do IBGE e listar cidades de um estado

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd <NOME_DO_REPOSITÓRIO>
   ```

2. Crie um ambiente virtual Python:

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando os Scripts

### Script corpo_docente.py

Este script extrai informações dos docentes do PPGTI do IFPB, incluindo:

- Nome
- Linha de pesquisa
- URL do Lattes
- E-mail

Para executar:

```bash
python corpo_docente.py
```

### Script ibge.py

Este script lista as cidades de um estado específico usando a API do IBGE.

Para executar:

```bash
python ibge.py
```

## Observações

- Certifique-se de que o ambiente virtual está ativado antes de executar os scripts
- O script `corpo_docente.py` depende da estrutura atual da página do PPGTI
- O script `ibge.py` usa a API pública do IBGE, que pode ter limitações de requisições

## Estrutura do Projeto

```
projeto/
│
├── venv/                    # Ambiente virtual Python
├── corpo_docente.py         # Script de scraping do PPGTI
├── ibge.py                  # Script de consumo da API do IBGE
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```
