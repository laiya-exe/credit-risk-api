FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY models ./models

CMD [ "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000" ]


# FROM l'image officielle python:3.12-slim     # slim = version allégée
# WORKDIR /app
# COPY requirements.txt dans la boîte
# RUN installer les bibliothèques de requirements.txt avec pip
# COPY le dossier src/ dans la boîte
# COPY le dossier models/ dans la boîte