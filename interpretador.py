def verificar_saudacao(mensagem):
    palavras = [
        "olá",
        "ola",
        "oi",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]

    for palavra in palavras:
        if palavra in mensagem:
            return True

    return False


def normalizar_mensagem(mensagem):
    mensagem = mensagem.lower()
    mensagem = mensagem.strip()
    mensagem = mensagem.replace("?", "")
    mensagem = mensagem.replace("!", "")

    return mensagem


def interpretar(mensagem):
    if verificar_saudacao(mensagem):
        return "saudacao"

    elif any(frase in mensagem for frase in [
        "como você está",
        "como vc está",
        "como vc esta",
        "tudo bem",
        "está bem",
        "esta bem",
        "como vai"
    ]):
        return "status"

    elif any(frase in mensagem for frase in [
        "quem é você",
        "quem vc é",
        "o que é você",
        "o que você é",
        "o que vc é"
    ]):
        return "identidade"

    elif mensagem == "sair":
        return "despedida"

    elif mensagem.startswith("abrir "):
        programa = mensagem.removeprefix("abrir ").strip()
        return ("abrir_programa", programa)

    else:
        return "desconhecido"