import os
import sys

def obter_caminho_projeto():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        # Aponta direto pra dist/ mesmo rodando como .py
        base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return os.path.join(base, "dist")

BASE_DIR = obter_caminho_projeto()
CAMINHO_JSON = os.path.join(BASE_DIR, "data", "cinelog.json")