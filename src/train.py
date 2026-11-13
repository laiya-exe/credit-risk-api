import pandas as pd
from src.data import nettoyer_donnees

df = pd.read_csv('datasets/UCI_Credit_Card.csv')
df_propre = nettoyer_donnees(df)
print(df_propre.shape)