import json
import os

from model.config import CAMINHO_JSON

def carregar_banco() -> dict:
    if not os.path.exists(CAMINHO_JSON):
        return {"diario": [], "watchlist": []}

    with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_banco(dados: dict) -> None:
    os.makedirs(os.path.dirname(CAMINHO_JSON), exist_ok=True)
    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)