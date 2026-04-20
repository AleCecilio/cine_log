"""
ARQUITETURA: MAIN VIEW ORCHESTRATOR
Gerencia a janela principal e a navegação entre Abas.
"""
import customtkinter as ctk
from view.theme import CORES
from view.tabs.aba_diario import AbaDiario
from view.tabs.aba_watchlist import AbaWatchlist

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
        self._navegando_para("diario")

    def _construir_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=190, fg_color=CORES["bg_painel"], corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(sidebar, text="🎥 CineLog", font=ctk.CTkFont(size=20, weight="bold"), text_color=CORES["azul_suave"]).pack(pady=30)
        
        self._botoes = {}
        for chave, label in [("diario", "📖 Diário"), ("watchlist", "🎬 Watchlist")]:
            btn = ctk.CTkButton(sidebar, text=label, fg_color="transparent", text_color=CORES["texto_muted"], command=lambda c=chave: self._navegando_para(c))
            btn.pack(padx=16, pady=4)
            self._botoes[chave] = btn

    def _construir_area_conteudo(self):
        self._area = ctk.CTkFrame(self, fg_color=CORES["bg_principal"])
        self._area.grid(row=0, column=1, sticky="nsew")
        self._area.grid_columnconfigure(0, weight=1)
        self._area.grid_rowconfigure(0, weight=1)
        self._abas = {"diario": AbaDiario(self._area), "watchlist": AbaWatchlist(self._area)}
        for aba in self._abas.values(): aba.grid(row=0, column=0, sticky="nsew")

    def _navegando_para(self, destino):
        for k, b in self._botoes.items():
            b.configure(fg_color=CORES["bg_linha_alt"] if k == destino else "transparent")
        aba = self._abas[destino]
        aba.atualizar()
        aba.tkraise()