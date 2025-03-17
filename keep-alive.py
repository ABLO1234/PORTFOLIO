import time
import requests

URL = "https://ton-app.streamlit.app"  # Remplace par l'URL de ton app déployée

while True:
    try:
        requests.get(URL)
        print("Ping réussi !")
    except Exception as e:
        print(f"Erreur de ping : {e}")
    time.sleep(600)  # Ping toutes les 10 minutes
