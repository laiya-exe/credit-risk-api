import pandas as pd
from src.data import nettoyer_donnees


def test_valeurs_inconnues_regroupees():
    df = pd.DataFrame({"EDUCATION": [0, 5, 6, 1], "MARRIAGE": [0, 1, 2, 3]})
    resultat = nettoyer_donnees(df)
    assert resultat["EDUCATION"].tolist() == [4, 4, 4, 1]
    assert resultat["MARRIAGE"].tolist() == [3, 1, 2, 3]
