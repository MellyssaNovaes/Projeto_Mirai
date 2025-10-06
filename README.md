# Projeto Mirai 

## Tecnologias Utilizadas

- Python 3.x
- FastAPI
- SQLModel
- Docker / Docker Compose
- PostgreSQL

## Clone este repositório
`git clone https://github.com/MellyssaNovaes/Projeto_Mirai.git`

## Como subir o Banco de Dados
Execute esse comando para subir o Banco de Dados:
`docker compose up db -d` 

Para parar todos os serviços execute: 
`docker compose down`



## Como executar o projeto
- Crie o venv: `python -m venv .venv`
- Ative o venv: `source .venv/bin/activate`
- Instale as dependências: `pip install -r requirements.txt`
- Rode o Serviço localmente: `fastapi dev app/main.py`

## Acesso à Aplicação

Após executar o projeto, acesse os seguintes links no seu navegador:

- **Servidor Local:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentação Interativa (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)