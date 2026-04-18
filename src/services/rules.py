from datetime import datetime, date

NOTAS_VALIDAS = {round(i * 0.5, 1) for i in range(1, 11)}

def nota_para_interno(nota_usuario: float) -> int:
    return int(nota_usuario * 2)

def nota_para_display(nota_interna: int) -> float:
    return nota_interna / 2

def validar_nota(nota_str: str) -> tuple[bool, str | float]:
    try:
        nota = float(nota_str.replace(",", "."))
    except ValueError:
        return False, "Nota inválida. Use um número como 3.5 ou 4."

    if nota not in NOTAS_VALIDAS:
        return False, "Nota deve estar entre 0.5 e 5.0 em incrementos de 0.5."

    return True, nota

def validar_data(data_str: str) -> tuple[bool, str | date]:
    try:
        data = datetime.strptime(data_str.strip(), "%d/%m/%Y").date()
    except ValueError:
        return False, "Formato de data inválido. Use dd/mm/aaaa."

    if data > date.today():
        return False, "Não é possível registrar um filme com data futura."

    return True, data

def validar_titulo(titulo: str) -> tuple[bool, str]:
    titulo = titulo.strip()
    if not titulo:
        return False, "O nome do filme não pode estar em branco."
    return True, titulo