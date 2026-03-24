from fastapi import FastAPI, HTTPException
import time

app = FastAPI()

CARROS = {
    1: {"modelo": "Fusca", "marca": "VW", "ano": 1970, "cor": "Azul"},
    2: {"modelo": "Civic", "marca": "Honda", "ano": 2022, "cor": "Preto"},
    3: {"modelo": "Uno", "marca": "Fiat", "ano": 2010, "cor": "Com Escada"}
}

@app.get("/carros/{id}")
def get_carro(id: int):
    time.sleep(3)
    
    
    if id not in CARROS:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return CARROS[id]