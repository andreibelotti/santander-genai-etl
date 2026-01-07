# Santander GenAI ETL

Projeto de pipeline ETL desenvolvido em Python, com foco em boas práticas de Engenharia de Dados, organização de código e automação de processos de dados.

Este projeto simula um fluxo real de ETL, desde a extração de dados até a carga final, servindo como base para projetos mais complexos.

---

##  Objetivo

Desenvolver um pipeline ETL modular e escalável, separando claramente as responsabilidades de:

- Extração de dados
- Transformação e tratamento
- Carga dos dados processados

O projeto também visa demonstrar organização de código, versionamento com Git e estrutura típica de projetos de dados utilizados no mercado.

---

##  Descrição do Pipeline

O pipeline funciona da seguinte forma:

1. **Extract**  
   Responsável por coletar os dados de origem (API, arquivo ou fonte simulada).

2. **Transform**  
   Realiza limpeza, padronização e transformações necessárias nos dados extraídos.

3. **Load**  
   Carrega os dados transformados para o destino final (arquivo, banco de dados ou camada analítica).

4. **Pipeline**  
   Orquestra a execução das etapas de forma sequencial.

---

##  Estrutura do projeto

config/
settings.py # Configurações do projeto
src/
extract.py # Extração dos dados
transform.py # Transformações
load.py # Carga dos dados
pipeline.py # Orquestração do ETL
requirements.txt # Dependências do projeto

yaml
Copiar código

---

##  Tecnologias utilizadas

- Python
- Pandas
- Requests
- Git / GitHub

---

##  Como executar

1. Clone o repositório:
```bash
git clone https://github.com/andreibelotti/santander-genai-etl.git
cd santander-genai-etl
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute o pipeline:

bash
Copiar código
python src/pipeline.py