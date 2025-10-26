# Projeto Mirai 

## Funcionalidades Implementadas
* **CRUD Completo** (Create, Read, Update, e Delete) para usuários.
* **Paginação** nas listas (`GET /users/`) para lidar com grandes volumes de dados de forma eficiente.
* **Validação de Unicidade** de e-mail ao criar ou atualizar um usuário.

## Tecnologias Utilizadas

- Python 3.x
- FastAPI
- SQLModel
- Docker / Docker Compose
- PostgreSQL

## Clone este repositório
`git clone https://github.com/MellyssaNovaes/Projeto_Mirai.git`

## Como subir todos os serviços
Execute esse comando para subir todos os serviços:
`docker compose up -d` 

Para parar todos os serviços execute: 
`docker compose down`



## Como executar o projeto
- Crie o venv: `python -m venv .venv`
- Ative o venv: `source .venv/bin/activate`
- Instale as dependências: `pip install -r requirements.txt`
- Rode o Serviço localmente: `fastapi dev app`

## Acesso à Aplicação

Após executar o projeto, acesse os seguintes links no seu navegador:

- **Servidor Local:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentação Interativa (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)