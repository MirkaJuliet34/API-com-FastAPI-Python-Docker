<h1 align="center">
 💡 Desenvolvendo API com FastAPI, Python e Docker
 
</h1>
  


## Configuração do Ambiente

- Certifique-se de ter o Python e o Docker instalados em seu sistema. Em seguida, crie um diretório para o projeto.Adicionei tratamento de exceções para lidar com possíveis erros de entrada do usuário, como inserir uma letra em vez de um número ao solicitar um valor.


```bash
mkdir fastapi_docker_api
cd fastapi_docker_api
```
## Instalação das Dependências

- Vamos instalar o FastAPI e o Uvicorn para criar a API, além do Docker para containerizar nossa aplicação.

```bash
pip install fastapi uvicorn
```
## Escrevendo o Código da API

- Crie um arquivo chamado main.py e adicione o seguinte código:

```python
from fastapi import FastAPI

app = FastAPI()

# Rota principal
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Rota para obter informações do usuário
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
```
## Criando o Dockerfile

- Crie um arquivo chamado Dockerfile na raiz do projeto com o seguinte conteúdo:

```Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app
```
## Construindo a Imagem Docker

- Abra um terminal na raiz do projeto e execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t fastapi-docker-api .
```
## Executando o Contêiner Docker

- Agora, podemos executar o contêiner Docker com o seguinte comando:

```bash
docker run -d --name fastapi-container -p 8000:80 fastapi-docker-api
```
## Testando a API

Você pode acessar a API no navegador ou usando o cURL:

- No navegador: `http://localhost:8000`
- Usando cURL: `curl http://localhost:8000`

Para obter informações sobre um usuário específico (por exemplo, usuário com ID 123), você pode usar:

- No navegador: `http://localhost:8000/users/123`
- Usando cURL: `curl http://localhost:8000/users/123`

<div align="center">
<img src="https://github.com/MirkaJuliet34/API-com-FastAPI-Python-Docker/assets/72041260/3764e0fc-528b-4772-90df-40665ff0dbb1" />
</div>


<p align="left">
  <a href="https://github.com/MirkaJuliet34"><img alt="Youtube" title="Youtube" src="https://img.shields.io/badge/-GitHub-red?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mirka-juliet-9bb590148/"><img alt="Twitter" title="Twitter" src="https://img.shields.io/badge/-Linkedin-1DA1F2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>


