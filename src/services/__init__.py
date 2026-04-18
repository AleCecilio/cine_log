from .engine import (
    registrar_filme,
    obter_diario,
    adicionar_watchlist,
    obter_watchlist,
    remover_watchlist,
    gerar_estrelas
)


# Isso garante que a View possa importar 'from services import engine'
from . import engine


__all__ = [
    "registrar_filme",
    "obter_diario",
    "adicionar_watchlist",
    "obter_watchlist",
    "remover_watchlist",
    "gerar_estrelas"
]

