"""
main.py — Ponto de entrada da aplicação CineLog (GUI)
------------------------------------------------------
Só inicializa a view. Nenhuma lógica de negócio vive aqui.
"""

import sys
import os

# Garante que imports entre camadas funcionem tanto em dev quanto
# no executável gerado pelo PyInstaller (sys._MEIPASS).
if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, BASE_DIR)

from view.app import CineLogApp

if __name__ == "__main__":
    app = CineLogApp()
    app.mainloop()