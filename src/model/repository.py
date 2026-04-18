from . import database_handler

def salvar_registro(registro: dict) -> None:
    dados = database_handler.carregar_banco()
    dados["diario"].append(registro)
    database_handler.salvar_banco(dados)

def buscar_diario() -> list[dict]:
    dados = database_handler.carregar_banco()
    return sorted(dados["diario"], key=lambda r: r["data_assistido"], reverse=True)

def salvar_watchlist(entrada: dict) -> None:
    dados = database_handler.carregar_banco()
    dados["watchlist"].append(entrada)
    database_handler.salvar_banco(dados)

def buscar_watchlist() -> list[dict]:
    dados = database_handler.carregar_banco()
    return dados["watchlist"]

def remover_da_watchlist(titulo_normalizado: str) -> bool:
    dados = database_handler.carregar_banco()
    lista_original = dados["watchlist"]
    
    dados["watchlist"] = [
        f for f in lista_original
        if f["titulo"].lower() != titulo_normalizado.lower()
    ]
    
    removido = len(dados["watchlist"]) < len(lista_original)
    if removido:
        database_handler.salvar_banco(dados)
        
    return removido

def titulo_existe_na_watchlist(titulo_normalizado: str) -> bool:
    watchlist = buscar_watchlist()
    return any(f["titulo"].lower() == titulo_normalizado.lower() for f in watchlist)