from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from src.data import nettoyer_donnees

app = FastAPI()
modele = joblib.load("models/RandomForest-model.joblib")

class Client(BaseModel):
    LIMIT_BAL: float
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
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
    return {'status': 'ok'}

@app.post("/predict")
def predit(client: Client):
    tableau = pd.DataFrame([client.model_dump()])
    tableau = nettoyer_donnees(tableau)
    proba = modele.predict_proba(tableau)[0, 1]
    return {"probabilite_defaut": float(proba)}