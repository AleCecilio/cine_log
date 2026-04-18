from view.io_helpers import _cabecalho, _pausar
from services import engine

 
def tela_diario() -> None:
    """Exibe o histórico de filmes assistidos."""
    _cabecalho("📖  Meu Diário de Filmes")
 
    registros = engine.obter_diario()
 
    if not registros:
        print("  Nenhum filme registrado ainda.")
    else:
        for i, r in enumerate(registros, start=1):
            estrelas = engine.gerar_estrelas(r["nota_display"])
            print(f"  {i:>2}. {r['titulo']}")
            print(f"       {r['data_display']}  •  {estrelas}  ({r['nota_display']:.1f})")
            if i < len(registros):
                print()
 
    _pausar()
 

def tela_watchlist() -> None:
    """Exibe a watchlist e oferece a opção de remover um item."""
    _cabecalho("🎬  Minha Watchlist")
 
    filmes = engine.obter_watchlist()
 
    if not filmes:
        print("  Sua watchlist está vazia.")
        _pausar()
        return
 
    for i, f in enumerate(filmes, start=1):
        print(f"  {i:>2}. {f['titulo']}")
 
    print()
    remover = input("  Remover algum filme? (deixe em branco para voltar): ").strip()
 
    if remover:
        try:
            engine.remover_watchlist(remover)
            print(f"\n  ✅  \"{remover}\" removido da watchlist.")
        except ValueError as e:
            print(f"\n  ❌  Erro: {e}")
 
    _pausar()