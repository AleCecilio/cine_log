import os
import sys

def obter_caminho_projeto():
    # Se estiver rodando como .exe
    if getattr(sys, 'frozen', False):
        # O caminho é onde o .exe está salvo (ex: pasta dist/)
        return os.path.dirname(sys.executable)
    # Se estiver rodando como .py no VS Code
    else:
        # O caminho é a raiz do projeto (cine_log/)
        # Sobe dois níveis a partir de src/model/config.py
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = obter_caminho_projeto()
CAMINHO_JSON = os.path.join(BASE_DIR, "data", "cinelog.json")