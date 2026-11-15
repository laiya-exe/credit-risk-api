from fastapi.testclient import TestClient
from src.api import app

testeur = TestClient(app)
CLIENT_VALIDE = {
    "LIMIT_BAL": 180000,
    "SEX": 2,
    "EDUCATION": 1,
    "MARRIAGE": 2,
    "AGE": 25,
    "PAY_0": 1,
    "PAY_2": 2,
    "PAY_3": 0,
    "PAY_4": 0,
    "PAY_5": 0,
    "PAY_6": 0,
    "BILL_AMT1": 41402,
    "BILL_AMT2": 41742,
    "BILL_AMT3": 42758,
    "BILL_AMT4": 43510,
    "BILL_AMT5": 44420,
    "BILL_AMT6": 45319,
    "PAY_AMT1": 1300,
    "PAY_AMT2": 2010,
    "PAY_AMT3": 1762,
    "PAY_AMT4": 1762,
    "PAY_AMT5": 1790,
    "PAY_AMT6": 1622,
}


def test_health_repond_ok():
    response = testeur.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_refuse_age_0():
    donnees = CLIENT_VALIDE.copy()
    donnees["AGE"] = 0
    response = testeur.post(
        "/predict",
        json=donnees,
    )
    assert response.status_code == 422


def test_predict_client_valide():
    donnees = CLIENT_VALIDE.copy()
    response = testeur.post(
        "/predict",
        json=donnees,
    )
    assert response.status_code == 200
    assert 1 >= response.json()["probabilite_defaut"] >= 0
