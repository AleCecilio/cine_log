"""
ARQUITETURA: MAIN VIEW ORCHESTRATOR
Gerencia a janela principal e a navegação entre Abas.
"""
import os
import sys
from PIL import Image
import customtkinter as ctk
from view.utils import CORES
from view.utils import carregar_imagem
from view.tabs import AbaDiario, AbaWatchlist


class CineLogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CineLog")
        self.geometry("900x600")
        self.configure(fg_color=CORES["bg_principal"])
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._construir_sidebar()
        self._construir_area_conteudo()

    def _construir_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=200, fg_color=CORES["bg_painel"], corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.pack_propagate(False)

        # Logo
        logo_img_sidebar = carregar_imagem("logocinema.ico", (32, 32))
        ctk.CTkLabel(
            sidebar, image=logo_img_sidebar, text="  CineLog", compound="left",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=CORES["azul_suave"]
        ).pack(pady=30, padx=20, anchor="w")

        # Separador
        ctk.CTkFrame(sidebar, height=1, fg_color=CORES["borda"]).pack(fill="x", padx=16, pady=(0, 16))

        # Botões de navegação
        self._botoes = {}
        nav_items = [
            ("home",      "  Home"),
            ("diario",    "  Diário"),
            ("watchlist", "  Watchlist"),
        ]
        for chave, label in nav_items:
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                anchor="w",
                height=40,
                corner_radius=8,
                fg_color="transparent",
                text_color=CORES["texto_muted"],
                hover_color=CORES["bg_linha_alt"],
                font=ctk.CTkFont(size=14),
                command=lambda c=chave: self._navegando_para(c)
            )
            btn.pack(padx=12, pady=3, fill="x")
            self._botoes[chave] = btn

    def _construir_area_conteudo(self):
        self._area = ctk.CTkFrame(self, fg_color=CORES["bg_principal"])
        self._area.grid(row=0, column=1, sticky="nsew")
        self._area.grid_columnconfigure(0, weight=1)
        self._area.grid_rowconfigure(0, weight=1)

        # Tela inicial com botões
        self._tela_inicio = ctk.CTkFrame(self._area, fg_color="transparent")
        self._tela_inicio.grid(row=0, column=0, sticky="nsew")

        logo_img_inicio = carregar_imagem("logocinema.ico", (48, 48))

        ctk.CTkLabel(
            self._tela_inicio,
            text="  CineLog",
            image=logo_img_inicio,
            compound="left",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color=CORES["azul_suave"]
        ).pack(pady=(100, 6))

        ctk.CTkLabel(
            self._tela_inicio,
            text="Seu diário pessoal de cinema.",
            font=ctk.CTkFont(size=14),
            text_color=CORES["texto_muted"]
        ).pack(pady=(0, 40))

        ctk.CTkButton(
            self._tela_inicio,
            text="📖  Abrir Diário",
            width=220, height=44,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=CORES["azul_destaque"],
            hover_color="#009018",
            command=lambda: self._navegando_para("diario")
        ).pack(pady=8)

        ctk.CTkButton(
            self._tela_inicio,
            text="🎬  Ver Watchlist",
            width=220, height=44,
            font=ctk.CTkFont(size=14),
            fg_color="transparent",
            border_width=1,
            border_color=CORES["azul_destaque"],
            text_color=CORES["azul_destaque"],
            hover_color=CORES["bg_linha_alt"],
            command=lambda: self._navegando_para("watchlist")
        ).pack(pady=8)

        # Abas
        self._abas = {"diario": AbaDiario(self._area), "watchlist": AbaWatchlist(self._area)}
        for aba in self._abas.values():
            aba.grid(row=0, column=0, sticky="nsew")

        self._tela_inicio.tkraise()

    def _navegando_para(self, destino):
        for k, b in self._botoes.items():
            b.configure(
                fg_color=CORES["bg_linha_alt"] if k == destino else "transparent",
                text_color=CORES["texto_primario"] if k == destino else CORES["texto_muted"]
            )
        if destino == "home":
            self._tela_inicio.tkraise()
            return
        aba = self._abas[destino]
        aba.atualizar()
        aba.tkraise()