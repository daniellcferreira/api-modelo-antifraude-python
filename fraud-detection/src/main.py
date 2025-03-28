from fastapi import FastAPI
from src.controllers import router

app = FastAPI(
  title="API de Detecção de Fraudes",
  description="API para detectar fraudes em transações financeiras usando aprendizado de máquina.",
  version="1.0.0"
)

# Definindo uma rota para a raiz
@app.get("/")
def read_root():
    return {"message": "API de detecção de fraude em funcionamento"}

# Incluindo o router com as rotas de fraude
app.include_router(router)
