import pandas as pd
from sklearn.metrics import precision_score, recall_score, roc_auc_score
from src.data import nettoyer_donnees
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Chargement et nettoyage des donnees
df = pd.read_csv('datasets/UCI_Credit_Card.csv')
df_propre = nettoyer_donnees(df)
# print(df_propre.shape)

# Separation des echantillons pour entrainement et test
X = df_propre.drop(columns=["default.payment.next.month", "ID"])
y = df_propre["default.payment.next.month"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=11,
    stratify=y,
)
# print(X_train.shape)
# print(X_test.shape)

# Entrainement du modele RandomForest
forest = RandomForestClassifier(n_estimators=200, min_samples_leaf=50, random_state=42, n_jobs=-1)
forest.fit(X_train, y_train)
predictions = forest.predict(X_test)
proba = forest.predict_proba(X_test)[:,1]
print(f"Recall: {recall_score(y_test, predictions):.3f}")
print(f"Precision: {precision_score(y_test, predictions):.3f}")
print(f"AUC : {roc_auc_score(y_test, proba):.3f}")

# Sauvegarde du modele
joblib.dump(forest, "models/RandomForest-model.joblib")
print('Modèle sauvegardé dans models/RandomForest-model.joblib')