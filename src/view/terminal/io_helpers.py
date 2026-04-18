def _linha(char: str = "─", largura: int = 52) -> None:
    print(char * largura)

def _cabecalho(titulo: str) -> None:
    _linha()
    print(f"  {titulo}")
    _linha()

def _pausar() -> None:
    input("\n  [ Pressione Enter para continuar ] ")