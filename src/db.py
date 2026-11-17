import os
import psycopg
from psycopg.types.json import Jsonb

VERSION_MODELE = "rf-200-leaf50-v1"


def enregistrer_prediction(donnees, probabilite):
    url = os.getenv("DATABASE_URL")
    if not url:
        return  # La CI et Render n'ont pas de base

    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO predictions (version_modele, donnees, probabilite)
                VALUES (%s, %s, %s)
                """,
                (VERSION_MODELE, Jsonb(donnees), float(probabilite)),
            )
