from fastapi import APIRouter

from src.models import Transaction
from src.services import CheckFraudService

router = APIRouter()

service = CheckFraudService()

# Definindo uma rota para verificar fraudes

@router.post("/check-fraud")
def check_fraud(transaction: Transaction):
  result = service.execute(transaction) # Executando o serviço de verificação de fraude
  return {
    "result": result[0],
    "probability": result[1]
  }