"""
Pacote View (Camada de Apresentação)
------------------------------------
Este arquivo atua como uma "Fachada" (Facade). 
Ele exporta apenas a função 'executar' do main_menu, escondendo 
toda a complexidade dos sub-módulos (forms, reports, helpers) 
do resto do sistema.
"""

# Importa a função principal de dentro do pacote
from .menu import executar

# Define o que fica disponível se alguém fizer `from view import *`
__all__ = ["executar"]