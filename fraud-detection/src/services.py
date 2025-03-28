from pathlib import Path
from typing import Any

import joblib
import pandas as pd

from src.models import Transaction
from src.utils import hour_to_minutes

BASE_PATH = Path(__file__).parent.parent  # Caminho base do projeto

# Definindo o serviço de verificação de fraude
class CheckFraudService:
  def __load_model_and_preprocessor(self) -> tuple[Any, Any]:
    model = joblib.load(f"{BASE_PATH}/src/ml_model/modelo_fraud_detection.pkl") # Carregando o modelo de detecção de fraudes
    preprocessor = joblib.load(f"{BASE_PATH}/src/ml_model/preprocessor.pkl") # Carregando o pré-processador
    return model, preprocessor

  def execute(self, transaction: Transaction) -> tuple[str, float]:
    model, preprocessor = self.__load_model_and_preprocessor() # Carregando o modelo e o pré-processador

    # Convertendo a hora da transação para minutos
    transaction_dict = transaction.model_dump()
   
    transaction_dict["hora_transacao"] = hour_to_minutes(transaction_dict["hora_transacao"])

    # Convertendo o dicionário em um DataFrame e aplicando o pré-processador
    df_transaction = pd.DataFrame([transaction_dict])
    X_transaction = preprocessor.transform(df_transaction)

    # Fazendo a previsão de fraude
    prediction = model.predict(X_transaction)[0] # Prevendo se é fraude ou não
    proba = model.predict_proba(X_transaction)[0][prediction] # Prevendo a probabilidade de ser fraude

    # Retornando o resultado da previsão
    result = "Fraude" if prediction == 1 else "Não Fraude"
    return result, proba