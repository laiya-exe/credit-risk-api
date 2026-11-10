import pandas as pd

def nettoyer_donnees(df : pd.DataFrame) -> pd.DataFrame:
    """Regroupe les valeurs inconnues de EDUCATION et MARRIAGE"""

    df = df.copy()
    df["EDUCATION"] = df["EDUCATION"].replace([0, 5, 6], 4)
    df["MARRIAGE"] = df["MARRIAGE"].replace(0, 3)
    return df