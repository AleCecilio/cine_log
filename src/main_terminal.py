"""
main.py — Ponto de entrada da aplicação CineLog
-------------------------------------------------
Responsabilidade: inicializar e passar o controle para a camada de
apresentação. Este arquivo não contém lógica de negócio nem acesso a dados.
"""
 
import sys
import os
 
# Garante que os imports relativos entre camadas funcionem independentemente
# de onde o script é executado.
sys.path.insert(0, os.path.dirname(__file__))
 
from view.terminal import executar
 
if __name__ == "__main__":
    executar()