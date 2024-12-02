# Basis-Image
FROM python:3.9-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY . /app

# Flask-Port-Umgebung setzen (optional)
ENV FLASK_RUN_PORT=5000
ENV FLASK_APP=app.py

# Port im Container freigeben
EXPOSE 5000

# Startkommando
CMD ["flask", "run", "--host=0.0.0.0"]