"""
ARQUITETURA: CENTRAL DE ESTILO (THEME)
Centraliza a paleta de cores e configurações globais do CustomTkinter.
Isso garante Alta Coesão: mudar uma cor aqui altera o sistema inteiro.
"""
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

CORES = {
    "bg_principal":   "#14181c",  # fundo escuro Letterboxd
    "bg_painel":      "#1c2228",  # sidebar
    "bg_linha_alt":   "#2c3440",  # linha alternada
    "bg_header":      "#1c2228",  # cabeçalho tabela
    "azul_destaque":  "#00b020",  # verde Letterboxd nos botões
    "azul_suave":     "#9ab57e",  # verde claro Letterboxd
    "texto_primario": "#e0e0e0",
    "texto_muted":    "#7a8a99",
    "borda":          "#2c3440",
    "vermelho":       "#e05c5c",
    "verde":          "#00b020",
}