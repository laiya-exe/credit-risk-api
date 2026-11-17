from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from src.data import nettoyer_donnees
from src.db import enregistrer_prediction
import psycopg
import logging

app = FastAPI()
modele = joblib.load("models/RandomForest-model.joblib")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Client(BaseModel):
    LIMIT_BAL: float = Field(ge=10000)  # LIMIT_BAL min est 10000
    SEX: int = Field(ge=1, le=2)  # 1 <= sexe <= 2
    EDUCATION: int = Field(ge=0, le=6)  # 0 <= education <= 6
    MARRIAGE: int = Field(ge=0, le=3)  # 0 <= marriage <= 3
    AGE: int = Field(ge=21, le=100)  # 21 <= age <= 100
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predit(client: Client):
    tableau = pd.DataFrame([client.model_dump()])
    tableau = nettoyer_donnees(tableau)
    proba = modele.predict_proba(tableau)[0, 1]
    try:
        enregistrer_prediction(client.model_dump(), float(proba))
    except psycopg.Error:
        logger.exception(
            "Échec de l'enregistrement de la prédiction en base de données"
        )
    return {"probabilite_defaut": float(proba)}
