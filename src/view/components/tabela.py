"""
ARQUITETURA: COMPONENTE DE INTERFACE REUTILIZÁVEL
Encapsula o widget ttk.Treeview com estilo Dark.
Ambas as abas (Diário e Watchlist) usam esta mesma classe (DRY - Don't Repeat Yourself).
"""
from tkinter import ttk
from view.theme import CORES

class TabelaEstilizada(ttk.Treeview):
    _estilo_aplicado = False

    def __init__(self, parent, colunas: list[tuple[str, str, int]], **kwargs):
        style_name = "CineLog.Treeview"

        if not TabelaEstilizada._estilo_aplicado:
            style = ttk.Style()
            style.theme_use("default")
            style.configure(
                style_name,
                background=CORES["bg_principal"],
                foreground=CORES["texto_primario"],
                fieldbackground=CORES["bg_principal"],
                borderwidth=0,
                rowheight=36,
                font=("Helvetica", 11),
            )
            style.configure(
                f"{style_name}.Heading",
                background=CORES["bg_header"],
                foreground=CORES["azul_suave"],
                font=("Helvetica", 11, "bold"),
                relief="flat",
                borderwidth=0,
            )
            style.map(style_name, background=[("selected", CORES["bg_linha_alt"])], foreground=[("selected", "#ffffff")])
            style.map(f"{style_name}.Heading", background=[("active", CORES["bg_header"])])
            TabelaEstilizada._estilo_aplicado = True

        ids_colunas = [c[0] for c in colunas]
        super().__init__(parent, style=style_name, columns=ids_colunas, show="headings", selectmode="browse", **kwargs)

        for col_id, col_label, col_width in colunas:
            self.heading(col_id, text=col_label)
            self.column(col_id, width=col_width, anchor="w", minwidth=60)

        self.tag_configure("par", background=CORES["bg_principal"])
        self.tag_configure("impar", background="#1f1f38")

    def recarregar(self, linhas: list[tuple]):
        self.delete(*self.get_children())
        for i, linha in enumerate(linhas):
            tag = "par" if i % 2 == 0 else "impar"
            self.insert("", "end", values=linha, tags=(tag,))