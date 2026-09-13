from conversa import (
    responder_saudacao,
    responder_status,
    responder_identidade,
    responder_despedida
)

from interpretador import (
    normalizar_mensagem,
    interpretar
)

from ferramentas import abrir_programa


while True:
    mensagem = input("Você: ")
    mensagem = normalizar_mensagem(mensagem)

    intencao = interpretar(mensagem)

    if intencao == "despedida":
        print("Assistente:", responder_despedida())
        break

    elif intencao == "saudacao":
        print("Assistente:", responder_saudacao())

    elif intencao == "status":
        print("Assistente:", responder_status())

    elif intencao == "identidade":
        print("Assistente:", responder_identidade())

    elif intencao[0] == "abrir_programa":
        programa = intencao[1]
        print("Assistente:", abrir_programa(programa))

    else:
        print("Assistente: Ainda não sei responder isso.")