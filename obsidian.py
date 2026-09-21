from pathlib import Path


COFRE = Path("/home/kalil/Criação/Historias/Sussurro das Estrelas/Universo")


def listar_notas():
    return list(COFRE.rglob("*.md"))

def buscar_nota(nome):
    for nota in listar_notas():
        if nota.stem.lower() == nome.lower():
            return nota

    return None

def ler_nota(nome):
    nota = buscar_nota(nome)

    if nota is None:
        return None

    return nota.read_text(encoding="utf-8")