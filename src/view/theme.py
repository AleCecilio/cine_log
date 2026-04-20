"""
ARQUITETURA: CENTRAL DE ESTILO (THEME)
Centraliza a paleta de cores e configurações globais do CustomTkinter.
Isso garante Alta Coesão: mudar uma cor aqui altera o sistema inteiro.
"""
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

CORES = {
    "bg_principal":   "#1a1a2e",
    "bg_painel":      "#16213e",
    "bg_linha_alt":   "#0f3460",
    "bg_header":      "#0f3460",
    "azul_destaque":  "#1e90ff",
    "azul_suave":     "#4a9eff",
    "texto_primario": "#e0e0e0",
    "texto_muted":    "#8a8a9a",
    "borda":          "#2a2a4a",
    "vermelho":       "#e05c5c",
    "verde":          "#4caf7d",
}