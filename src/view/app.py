"""
view/app.py — Camada de Apresentação Gráfica (GUI)
---------------------------------------------------
Responsabilidade: renderizar a interface e capturar eventos do usuário.
Toda lógica de validação e persistência é delegada a services.engine.
Esta classe nunca importa nada de model/ diretamente.
"""

import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import date

# Integração com a camada de negócio — única dependência permitida nesta view
from services import engine

# ── Configuração global do tema ──────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Paleta manual para os widgets ttk (Treeview não é coberto pelo CTk)
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


# ── Janela modal base ────────────────────────────────────────────────────────

class _ModalBase(ctk.CTkToplevel):
    """
    Janela modal reutilizável. Toda janela de formulário herda daqui
    para garantir comportamento consistente (modal, centralizada, tema).
    """
    def __init__(self, parent, titulo: str, largura: int = 420, altura: int = 340):
        super().__init__(parent)
        self.title(titulo)
        self.resizable(False, False)
        self.grab_set()  # Bloqueia interação com a janela principal

        # Centraliza em relação à janela pai
        self.update_idletasks()
        px = parent.winfo_x() + (parent.winfo_width()  // 2) - (largura // 2)
        py = parent.winfo_y() + (parent.winfo_height() // 2) - (altura  // 2)
        self.geometry(f"{largura}x{altura}+{px}+{py}")

        self.configure(fg_color=CORES["bg_painel"])
        self._callback_sucesso = None

    def ao_confirmar(self, callback):
        """Registra a função a ser chamada após submissão bem-sucedida."""
        self._callback_sucesso = callback
        return self

    def _notificar_sucesso(self):
        if self._callback_sucesso:
            self._callback_sucesso()


# ── Modal: Registrar Filme ───────────────────────────────────────────────────

class ModalRegistrarFilme(_ModalBase):
    def __init__(self, parent):
        super().__init__(parent, "Registrar Filme Assistido", largura=440, altura=360)
        self._construir_layout()

    def _construir_layout(self):
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=28, pady=24)

        # Título do modal
        ctk.CTkLabel(
            container, text="📽  Novo Registro",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=CORES["texto_primario"]
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))

        # --- campos ---
        campos = [
            ("Nome do filme",          "entry_titulo"),
            ("Data assistida (dd/mm/aaaa)", "entry_data"),
            ("Nota (0.5 a 5.0)",       "entry_nota"),
        ]
        for i, (label, attr) in enumerate(campos, start=1):
            ctk.CTkLabel(
                container, text=label,
                font=ctk.CTkFont(size=12),
                text_color=CORES["texto_muted"]
            ).grid(row=i*2-1, column=0, columnspan=2, sticky="w", pady=(0, 2))

            entry = ctk.CTkEntry(
                container, width=380, height=36,
                placeholder_text=label,
                border_color=CORES["borda"],
                fg_color=CORES["bg_principal"],
            )
            entry.grid(row=i*2, column=0, columnspan=2, sticky="ew", pady=(0, 10))
            setattr(self, attr, entry)

        # Pré-preenche a data com hoje
        hoje = date.today().strftime("%d/%m/%Y")
        self.entry_data.insert(0, hoje)

        # Botões
        frame_botoes = ctk.CTkFrame(container, fg_color="transparent")
        frame_botoes.grid(row=10, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        ctk.CTkButton(
            frame_botoes, text="Cancelar", width=120,
            fg_color="transparent", border_width=1,
            border_color=CORES["borda"],
            hover_color=CORES["bg_principal"],
            text_color=CORES["texto_muted"],
            command=self.destroy
        ).pack(side="left")

        ctk.CTkButton(
            frame_botoes, text="✔  Registrar", width=200,
            fg_color=CORES["azul_destaque"],
            hover_color=CORES["azul_suave"],
            font=ctk.CTkFont(weight="bold"),
            command=self._submeter
        ).pack(side="right")

    def _submeter(self):
        titulo = self.entry_titulo.get().strip()
        data   = self.entry_data.get().strip()
        nota   = self.entry_nota.get().strip()

        # A validação real acontece no engine (camada de negócio)
        try:
            engine.registrar_filme(titulo, data, nota)
            self._notificar_sucesso()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Dados inválidos", str(e), parent=self)


# ── Modal: Adicionar à Watchlist ─────────────────────────────────────────────

class ModalAdicionarWatchlist(_ModalBase):
    def __init__(self, parent):
        super().__init__(parent, "Adicionar à Watchlist", largura=420, altura=230)
        self._construir_layout()

    def _construir_layout(self):
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=28, pady=24)

        ctk.CTkLabel(
            container, text="🔖  Quero Ver",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=CORES["texto_primario"]
        ).pack(anchor="w", pady=(0, 16))

        ctk.CTkLabel(
            container, text="Nome do filme",
            font=ctk.CTkFont(size=12),
            text_color=CORES["texto_muted"]
        ).pack(anchor="w", pady=(0, 4))

        self.entry_titulo = ctk.CTkEntry(
            container, width=360, height=36,
            placeholder_text="Ex: Duna Parte 2",
            border_color=CORES["borda"],
            fg_color=CORES["bg_principal"],
        )
        self.entry_titulo.pack(fill="x", pady=(0, 16))
        self.entry_titulo.focus()

        frame_botoes = ctk.CTkFrame(container, fg_color="transparent")
        frame_botoes.pack(fill="x")

        ctk.CTkButton(
            frame_botoes, text="Cancelar", width=120,
            fg_color="transparent", border_width=1,
            border_color=CORES["borda"],
            hover_color=CORES["bg_principal"],
            text_color=CORES["texto_muted"],
            command=self.destroy
        ).pack(side="left")

        ctk.CTkButton(
            frame_botoes, text="✔  Adicionar", width=200,
            fg_color=CORES["azul_destaque"],
            hover_color=CORES["azul_suave"],
            font=ctk.CTkFont(weight="bold"),
            command=self._submeter
        ).pack(side="right")

    def _submeter(self):
        titulo = self.entry_titulo.get().strip()
        try:
            engine.adicionar_watchlist(titulo)
            self._notificar_sucesso()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Dados inválidos", str(e), parent=self)


# ── Componente: Tabela estilizada ────────────────────────────────────────────

class TabelaEstilizada(ttk.Treeview):
    """
    Treeview com estilo dark aplicado via ttk.Style.
    Encapsula a configuração visual para que as abas não precisem
    se preocupar com detalhes de estilo do widget legado.
    """
    _estilo_aplicado = False  # Singleton: aplica o estilo apenas uma vez

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
            style.map(
                style_name,
                background=[("selected", CORES["bg_linha_alt"])],
                foreground=[("selected", "#ffffff")],
            )
            style.map(
                f"{style_name}.Heading",
                background=[("active", CORES["bg_header"])],
            )
            TabelaEstilizada._estilo_aplicado = True

        ids_colunas = [c[0] for c in colunas]
        super().__init__(
            parent,
            style=style_name,
            columns=ids_colunas,
            show="headings",
            selectmode="browse",
            **kwargs,
        )

        for col_id, col_label, col_width in colunas:
            self.heading(col_id, text=col_label)
            self.column(col_id, width=col_width, anchor="w", minwidth=60)

        # Linhas alternadas
        self.tag_configure("par",   background=CORES["bg_principal"])
        self.tag_configure("impar", background="#1f1f38")

    def recarregar(self, linhas: list[tuple]):
        """Limpa e reinsere todos os dados. Chamado sempre que os dados mudam."""
        self.delete(*self.get_children())
        for i, linha in enumerate(linhas):
            tag = "par" if i % 2 == 0 else "impar"
            self.insert("", "end", values=linha, tags=(tag,))


# ── Aba: Diário ──────────────────────────────────────────────────────────────

class AbaDiario(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self._construir_layout()
        self.atualizar()

    def _construir_layout(self):
        # Cabeçalho da aba
        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 12))

        ctk.CTkLabel(
            topo, text="📖  Diário de Filmes",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=CORES["texto_primario"]
        ).pack(side="left")

        self.lbl_total = ctk.CTkLabel(
            topo, text="",
            font=ctk.CTkFont(size=12),
            text_color=CORES["texto_muted"]
        )
        self.lbl_total.pack(side="left", padx=12, pady=(4, 0))

        ctk.CTkButton(
            topo, text="+ Registrar Filme",
            width=160, height=34,
            fg_color=CORES["azul_destaque"],
            hover_color=CORES["azul_suave"],
            font=ctk.CTkFont(weight="bold"),
            command=self._abrir_modal_registro
        ).pack(side="right")

        # Tabela
        frame_tabela = ctk.CTkFrame(self, fg_color=CORES["bg_principal"], corner_radius=10)
        frame_tabela.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.tabela = TabelaEstilizada(
            frame_tabela,
            colunas=[
                ("titulo", "Título",        320),
                ("data",   "Assistido em",  120),
                ("nota",   "Nota",          100),
            ]
        )

        scroll = ctk.CTkScrollbar(frame_tabela, command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y", padx=(0, 4), pady=4)
        self.tabela.pack(fill="both", expand=True, padx=4, pady=4)

    def atualizar(self):
        """Busca dados no engine e repopula a tabela. Chamado externamente após mutações."""
        registros = engine.obter_diario()
        linhas = [
            (
                r["titulo"],
                r["data_display"],
                f"{r['nota_display']:.1f}  {engine.gerar_estrelas(r['nota_display'])}",
            )
            for r in registros
        ]
        self.tabela.recarregar(linhas)
        total = len(linhas)
        self.lbl_total.configure(
            text=f"({total} filme{'s' if total != 1 else ''})"
        )

    def _abrir_modal_registro(self):
        modal = ModalRegistrarFilme(self.winfo_toplevel())
        modal.ao_confirmar(self.atualizar)


# ── Aba: Watchlist ───────────────────────────────────────────────────────────

class AbaWatchlist(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self._construir_layout()
        self.atualizar()

    def _construir_layout(self):
        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 12))

        ctk.CTkLabel(
            topo, text="🎬  Watchlist",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=CORES["texto_primario"]
        ).pack(side="left")

        self.lbl_total = ctk.CTkLabel(
            topo, text="",
            font=ctk.CTkFont(size=12),
            text_color=CORES["texto_muted"]
        )
        self.lbl_total.pack(side="left", padx=12, pady=(4, 0))

        ctk.CTkButton(
            topo, text="+ Quero Ver",
            width=140, height=34,
            fg_color=CORES["azul_destaque"],
            hover_color=CORES["azul_suave"],
            font=ctk.CTkFont(weight="bold"),
            command=self._abrir_modal_watchlist
        ).pack(side="right")

        ctk.CTkButton(
            topo, text="🗑  Remover",
            width=110, height=34,
            fg_color="transparent",
            border_width=1,
            border_color=CORES["vermelho"],
            hover_color="#3a1a1a",
            text_color=CORES["vermelho"],
            command=self._remover_selecionado
        ).pack(side="right", padx=(0, 8))

        frame_tabela = ctk.CTkFrame(self, fg_color=CORES["bg_principal"], corner_radius=10)
        frame_tabela.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.tabela = TabelaEstilizada(
            frame_tabela,
            colunas=[("titulo", "Título do Filme", 500)]
        )

        scroll = ctk.CTkScrollbar(frame_tabela, command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y", padx=(0, 4), pady=4)
        self.tabela.pack(fill="both", expand=True, padx=4, pady=4)

    def atualizar(self):
        filmes = engine.obter_watchlist()
        linhas = [(f["titulo"],) for f in filmes]
        self.tabela.recarregar(linhas)
        total = len(linhas)
        self.lbl_total.configure(
            text=f"({total} filme{'s' if total != 1 else ''})"
        )

    def _abrir_modal_watchlist(self):
        modal = ModalAdicionarWatchlist(self.winfo_toplevel())
        modal.ao_confirmar(self.atualizar)

    def _remover_selecionado(self):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning(
                "Nenhuma seleção",
                "Selecione um filme na lista antes de remover.",
                parent=self.winfo_toplevel()
            )
            return

        titulo = self.tabela.item(selecao[0])["values"][0]
        confirmar = messagebox.askyesno(
            "Confirmar remoção",
            f'Remover "{titulo}" da watchlist?',
            parent=self.winfo_toplevel()
        )
        if confirmar:
            try:
                engine.remover_watchlist(titulo)
                self.atualizar()
            except ValueError as e:
                messagebox.showerror("Erro", str(e), parent=self.winfo_toplevel())


# ── Janela Principal ─────────────────────────────────────────────────────────

class CineLogApp(ctk.CTk):
    """
    Classe raiz da aplicação. Herda de ctk.CTk (janela principal do CustomTkinter).
    Monta o layout geral: barra lateral de navegação + área de conteúdo com abas.
    """
    LARGURA  = 900
    ALTURA   = 600
    TITULO   = "CineLog"

    def __init__(self):
        super().__init__()
        self._configurar_janela()
        self._construir_sidebar()
        self._construir_area_conteudo()
        # Inicia na aba Diário
        self._navegando_para("diario")

    def _configurar_janela(self):
        self.title(self.TITULO)
        self.geometry(f"{self.LARGURA}x{self.ALTURA}")
        self.minsize(760, 480)
        self.configure(fg_color=CORES["bg_principal"])

        # Grid principal: sidebar (fixo) + conteúdo (expansível)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _construir_sidebar(self):
        sidebar = ctk.CTkFrame(
            self, width=190,
            fg_color=CORES["bg_painel"],
            corner_radius=0
        )
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        # Logo / Título
        ctk.CTkLabel(
            sidebar,
            text="🎥  CineLog",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=CORES["azul_suave"],
        ).pack(pady=(28, 32), padx=16, anchor="w")

        # Botões de navegação
        self._botoes_nav = {}
        itens_nav = [
            ("diario",    "📖  Diário"),
            ("watchlist", "🎬  Watchlist"),
        ]
        for chave, label in itens_nav:
            btn = ctk.CTkButton(
                sidebar, text=label,
                width=158, height=40,
                anchor="w",
                fg_color="transparent",
                hover_color=CORES["bg_linha_alt"],
                text_color=CORES["texto_muted"],
                font=ctk.CTkFont(size=13),
                command=lambda c=chave: self._navegando_para(c)
            )
            btn.pack(padx=16, pady=4)
            self._botoes_nav[chave] = btn

        # Separador e versão no rodapé
        ctk.CTkFrame(sidebar, height=1, fg_color=CORES["borda"]).pack(
            fill="x", padx=16, pady=16
        )
        ctk.CTkLabel(
            sidebar, text="v1.0  •  Trabalho ADS",
            font=ctk.CTkFont(size=10),
            text_color=CORES["texto_muted"]
        ).pack(side="bottom", pady=16)

    def _construir_area_conteudo(self):
        self._area_conteudo = ctk.CTkFrame(
            self, fg_color=CORES["bg_principal"], corner_radius=0
        )
        self._area_conteudo.grid(row=0, column=1, sticky="nsew")
        self._area_conteudo.grid_columnconfigure(0, weight=1)
        self._area_conteudo.grid_rowconfigure(0, weight=1)

        # Instancia as abas antecipadamente para reutilizá-las
        self._abas = {
            "diario":    AbaDiario(self._area_conteudo),
            "watchlist": AbaWatchlist(self._area_conteudo),
        }
        for aba in self._abas.values():
            aba.grid(row=0, column=0, sticky="nsew")

    def _navegando_para(self, destino: str):
        """Troca a aba visível e atualiza o estilo dos botões da sidebar."""
        # Atualiza destaque dos botões de navegação
        for chave, btn in self._botoes_nav.items():
            if chave == destino:
                btn.configure(
                    fg_color=CORES["bg_linha_alt"],
                    text_color=CORES["azul_suave"],
                    font=ctk.CTkFont(size=13, weight="bold")
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=CORES["texto_muted"],
                    font=ctk.CTkFont(size=13, weight="normal")
                )

        # Recarrega dados e traz a aba para frente
        aba = self._abas[destino]
        aba.atualizar()
        aba.tkraise()