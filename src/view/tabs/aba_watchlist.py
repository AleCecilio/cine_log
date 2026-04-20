"""
ARQUITETURA: SUB-VIEW (TELA WATCHLIST)
Encapsula apenas os widgets e comportamentos da aba 'Quero Ver'.
"""
import customtkinter as ctk
from tkinter import messagebox
from view.theme import CORES
from view.components.tabela import TabelaEstilizada
from view.components.modais import ModalAdicionarWatchlist
from services import engine

class AbaWatchlist(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 12))
        ctk.CTkLabel(topo, text="🎬  Watchlist", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left")
        ctk.CTkButton(topo, text="+ Quero Ver", fg_color=CORES["azul_destaque"], command=self._abrir_modal_watchlist).pack(side="right")
        ctk.CTkButton(topo, text="🗑 Remover", fg_color="transparent", border_width=1, border_color=CORES["vermelho"], text_color=CORES["vermelho"], command=self._remover_selecionado).pack(side="right", padx=5)

        self.tabela = TabelaEstilizada(self, [("titulo", "Título do Filme", 500)])
        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)

    def atualizar(self):
        filmes = engine.obter_watchlist()
        self.tabela.recarregar([(f["titulo"],) for f in filmes])

    def _abrir_modal_watchlist(self):
        ModalAdicionarWatchlist(self.winfo_toplevel()).ao_confirmar(self.atualizar)

    def _remover_selecionado(self):
        selecao = self.tabela.selection()
        if not selecao: return
        titulo = self.tabela.item(selecao[0])["values"][0]
        if messagebox.askyesno("Confirmar", f'Remover "{titulo}"?'):
            engine.remover_watchlist(titulo)
            self.atualizar()