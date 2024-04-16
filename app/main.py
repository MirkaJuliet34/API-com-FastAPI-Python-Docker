from fastapi import FastAPI

app = FastAPI()

# Rota principal
@app.get("/")
async def read_root():
    return{"message": "Hello, FastAPI!"}

# Rota para obter informações do usuário
@app.get(" /users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}