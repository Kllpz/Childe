import random


def responder_saudacao():
    saudacoes = [
        "Olá! É bom falar com você.",
        "Oi! O que vamos fazer hoje?",
        "Olá! Estou ouvindo.",
        "E aí! Que bom que apareceu."
    ]

    return random.choice(saudacoes)


def responder_status():
    return "Estou funcionando muito bem!"


def responder_identidade():
    return "Eu sou o seu assistente pessoal."


def responder_despedida():
    despedidas = [
        "Tchau Tchau!",
        "See you later.",
        "Até mais.",
        "Nos vemos depois.",
        "Bye ;)"
    ]

    return random.choice(despedidas)