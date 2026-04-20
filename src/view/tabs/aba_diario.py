"""
ARQUITETURA: SUB-VIEW (TELA DIÁRIO)
Encapsula apenas os widgets e comportamentos da aba de histórico.
"""
import customtkinter as ctk
from view.theme import CORES
from view.components.tabela import TabelaEstilizada
from view.components.modais import ModalRegistrarFilme
from services import engine

class AbaDiario(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 12))
        ctk.CTkLabel(topo, text="📖  Diário de Filmes", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left")
        self.lbl_total = ctk.CTkLabel(topo, text="", text_color=CORES["texto_muted"])
        self.lbl_total.pack(side="left", padx=10)
        ctk.CTkButton(topo, text="+ Registrar", fg_color=CORES["azul_destaque"], command=self._abrir_modal_registro).pack(side="right")
        
        self.tabela = TabelaEstilizada(self, [("titulo", "Título", 320), ("data", "Assistido em", 120), ("nota", "Nota", 100)])
        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)

    def atualizar(self):
        registros = engine.obter_diario()
        linhas = [(r["titulo"], r["data_display"], f"{r['nota_display']:.1f}  {engine.gerar_estrelas(r['nota_display'])}") for r in registros]
        self.tabela.recarregar(linhas)
        self.lbl_total.configure(text=f"({len(linhas)} filmes)")

    def _abrir_modal_registro(self):
        ModalRegistrarFilme(self.winfo_toplevel()).ao_confirmar(self.atualizar)