"""
ARQUITETURA: CAMADA DE CAPTURAS (INPUT MODALS)
Responsável por validar a entrada visual e chamar a lógica de negócio (Engine).
"""
import customtkinter as ctk
from tkinter import messagebox
from datetime import date
from view.utils import CORES
from services import engine

class _ModalBase(ctk.CTkToplevel):
    def __init__(self, parent, titulo: str, largura: int = 420, altura: int = 340):
        super().__init__(parent)
        self.title(titulo)
        self.resizable(False, False)
        self.grab_set()
        self.update_idletasks()
        px = parent.winfo_x() + (parent.winfo_width() // 2) - (largura // 2)
        py = parent.winfo_y() + (parent.winfo_height() // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{px}+{py}")
        self.configure(fg_color=CORES["bg_painel"])
        self._callback_sucesso = None

    def ao_confirmar(self, callback):
        self._callback_sucesso = callback
        return self

    def _notificar_sucesso(self):
        if self._callback_sucesso: self._callback_sucesso()

class ModalRegistrarFilme(_ModalBase):
    def __init__(self, parent):
        super().__init__(parent, "Registrar Filme Assistido", largura=440, altura=360)
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=28, pady=24)
        ctk.CTkLabel(container, text="📽  Novo Registro", font=ctk.CTkFont(size=18, weight="bold"), text_color=CORES["texto_primario"]).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))
        
        self.entry_titulo = self._criar_campo(container, "Nome do filme", 1)
        self.entry_data = self._criar_campo(container, "Data assistida (dd/mm/aaaa)", 2)
        self.entry_nota = self._criar_campo(container, "Nota (0.5 a 5.0)", 3)
        self.entry_data.insert(0, date.today().strftime("%d/%m/%Y"))

        ctk.CTkButton(container, text="✔  Registrar", fg_color=CORES["azul_destaque"], command=self._submeter).grid(row=8, column=1, pady=(20,0))

    def _criar_campo(self, master, label, pos):
        ctk.CTkLabel(master, text=label, font=ctk.CTkFont(size=12), text_color=CORES["texto_muted"]).grid(row=pos*2-1, column=0, sticky="w")
        entry = ctk.CTkEntry(master, width=380, fg_color=CORES["bg_principal"])
        entry.grid(row=pos*2, column=0, columnspan=2, pady=(0,10))
        return entry

    def _submeter(self):
        try:
            engine.registrar_filme(self.entry_titulo.get(), self.entry_data.get(), self.entry_nota.get())
            self._notificar_sucesso()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e), parent=self)

class ModalAdicionarWatchlist(_ModalBase):
    def __init__(self, parent):
        super().__init__(parent, "Adicionar à Watchlist", largura=420, altura=230)
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=28, pady=24)
        self.entry_titulo = ctk.CTkEntry(container, width=360, placeholder_text="Ex: Duna Parte 2", fg_color=CORES["bg_principal"])
        self.entry_titulo.pack(pady=20)
        ctk.CTkButton(container, text="✔  Adicionar", fg_color=CORES["azul_destaque"], command=self._submeter).pack()

    def _submeter(self):
        try:
            engine.adicionar_watchlist(self.entry_titulo.get())
            self._notificar_sucesso()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", str(e), parent=self)