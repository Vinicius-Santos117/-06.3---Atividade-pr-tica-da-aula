from fastapi import FastAPI
import requests
import os

app = FastAPI()

CARROS_SERVICE_URL = os.getenv("CARROS_URL", "http://ms-carros:8000")

@app.get("/aluguel/{id}")
def get_reserva(id: int):
    reserva = {
        "reserva_id": id,
        "cliente": "Vinicius",
        "dias": 3,
        "valor_diaria": 150.0
    }

    try:
        response = requests.get(f"{CARROS_SERVICE_URL}/carros/{id}", timeout=2)
        response.raise_for_status()
        reserva["veiculo"] = response.json()
    except Exception as e:
        reserva["veiculo"] = {"erro": "Informações do veículo indisponíveis no momento"}
        reserva["detalhes_erro"] = str(e)

    return reserva