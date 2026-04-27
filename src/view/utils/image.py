"""
ARQUITETURA: GERENCIADOR DE ASSETS
Centraliza o carregamento de imagens para evitar repetição de código e tratar caminhos absolutos.
"""
import os
import sys
from PIL import Image
import customtkinter as ctk

def carregar_imagem(nome_arquivo: str, tamanho: tuple[int, int]) -> ctk.CTkImage:

    BASE = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    
    caminho_completo = os.path.join(BASE, nome_arquivo)
    
    return ctk.CTkImage(Image.open(caminho_completo), size=tamanho)