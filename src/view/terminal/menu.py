from .io_helpers import _linha
from .forms import tela_registrar_filme, tela_adicionar_watchlist
from .reports import tela_diario, tela_watchlist

def exibir_menu() -> str:
    """
    Renderiza o menu principal e retorna a opção escolhida.
    Nenhuma lógica de decisão aqui — só coleta e repassa.
    """
    print()
    _linha("═")
    print("  🎥  CineLog — Seu diário de filmes")
    _linha("═")
    print("  1  →  Registrar filme assistido")
    print("  2  →  Ver meu Diário")
    print("  3  →  Adicionar à Watchlist")
    print("  4  →  Ver Watchlist")
    print("  0  →  Sair")
    _linha()
    return input("  Opção: ").strip()
 
 
def executar() -> None:
    """Loop principal da aplicação. Mapeia opções do menu para telas."""
    rotas = {
        "1": tela_registrar_filme,
        "2": tela_diario,
        "3": tela_adicionar_watchlist,
        "4": tela_watchlist,
    }
 
    while True:
        opcao = exibir_menu()
 
        if opcao == "0":
            print("\n  Até mais! 🎬\n")
            break
 
        tela = rotas.get(opcao)
        if tela:
            tela()
        else:
            print("\n  ❌  Opção inválida. Tente novamente.")