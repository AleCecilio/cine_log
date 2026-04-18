from .io_helpers import _cabecalho, _pausar
from services import engine

def tela_registrar_filme() -> None:
    """Coleta dados do usuário e delega a criação do registro ao serviço."""
    _cabecalho("📽  Registrar Filme Assistido")
 
    titulo = input("  Nome do filme: ")
    data_str = input("  Data em que assistiu (dd/mm/aaaa): ")
    nota_str = input("  Nota (0.5 a 5.0, em passos de 0.5): ")
 
    try:
        # A camada de negócio faz todas as validações; a view só repassa.
        registro = engine.registrar_filme(titulo, data_str, nota_str)
        estrelas = engine.gerar_estrelas(registro["nota_interna"] / 2)
        print(f"\n  ✅  \"{registro['titulo']}\" registrado com sucesso! {estrelas}")
    except ValueError as e:
        print(f"\n  ❌  Erro: {e}")
 
    _pausar()

 
def tela_adicionar_watchlist() -> None:
    """Adiciona um filme à watchlist delegando ao serviço."""
    _cabecalho("🔖  Adicionar à Watchlist")
 
    titulo = input("  Nome do filme que quer ver: ")
 
    try:
        entrada = engine.adicionar_watchlist(titulo)
        print(f"\n  ✅  \"{entrada['titulo']}\" adicionado à sua watchlist!")
    except ValueError as e:
        print(f"\n  ❌  Erro: {e}")
 
    _pausar()
 
 
