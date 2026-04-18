from datetime import datetime
from model import repository
from . import rules

def registrar_filme(titulo: str, data_str: str, nota_str: str) -> dict:
    ok, titulo_ou_erro = rules.validar_titulo(titulo)
    if not ok:
        raise ValueError(titulo_ou_erro)

    ok, data_ou_erro = rules.validar_data(data_str)
    if not ok:
        raise ValueError(data_ou_erro)

    ok, nota_ou_erro = rules.validar_nota(nota_str)
    if not ok:
        raise ValueError(nota_ou_erro)

    registro = {
        "titulo": titulo_ou_erro,
        "data_assistido": data_ou_erro.strftime("%Y-%m-%d"),
        "nota_interna": rules.nota_para_interno(nota_ou_erro),
    }

    repository.salvar_registro(registro)
    return registro

def obter_diario() -> list[dict]:
    registros = repository.buscar_diario()
    for r in registros:
        r["nota_display"] = rules.nota_para_display(r["nota_interna"])
        r["data_display"] = datetime.strptime(r["data_assistido"], "%Y-%m-%d").strftime("%d/%m/%Y")
    return registros

def adicionar_watchlist(titulo: str) -> dict:
    ok, titulo_ou_erro = rules.validar_titulo(titulo)
    if not ok:
        raise ValueError(titulo_ou_erro)

    titulo_limpo: str = titulo_ou_erro

    if repository.titulo_existe_na_watchlist(titulo_limpo):
        raise ValueError(f'"{titulo_limpo}" já está na sua watchlist.')

    entrada = {"titulo": titulo_limpo}
    repository.salvar_watchlist(entrada)
    return entrada

def obter_watchlist() -> list[dict]:
    return repository.buscar_watchlist()

def remover_watchlist(titulo: str) -> None:
    ok, titulo_ou_erro = rules.validar_titulo(titulo)
    if not ok:
        raise ValueError(titulo_ou_erro)

    removido = repository.remover_da_watchlist(titulo_ou_erro)
    if not removido:
        raise ValueError(f'"{titulo_ou_erro}" não encontrado na watchlist.')

def gerar_estrelas(nota_display: float) -> str:
    inteiras = int(nota_display)
    meia = (nota_display % 1) >= 0.5
    vazias = 5 - inteiras - (1 if meia else 0)
    return "★" * inteiras + ("½" if meia else "") + "☆" * vazias