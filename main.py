import speech_recognition as sr

from config import WAKE_WORDS, LISTEN_TIME_WAKE, LISTEN_TIME_COMMAND
from speech_local import ouvir_local
from router import executar_comando
from speaker import falar

import commands.dictation as dictation


MODO_TEXTO = False


def detectar_wake_word(texto):
    return any(palavra in texto for palavra in WAKE_WORDS)


def rodar_modo_texto():
    print("Tatsu iniciado em modo texto.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        texto = input("Você: ").lower()

        if texto in ["sair", "encerrar", "fechar"]:
            falar("Encerrando sistema.")
            break

        if dictation.DICTATION_MODE:
            if detectar_wake_word(texto):
                dictation.parar_dictado()
                falar("Modo escrita desativado.")
            else:
                dictation.escrever_texto(texto + " ")

            continue

        if detectar_wake_word(texto):
            falar("Ativado.")

            comando = input("Comando: ").lower()

            resposta = executar_comando(comando)

            if resposta:
                falar(resposta)
            else:
                falar("Comando não reconhecido.")


def rodar_modo_voz():
    print("Tatsu iniciado em modo voz.")

    while True:
            print("\nAguardando ativação...")
            texto = ouvir_local()

            if texto:
                print("Ouvi:", texto)

            if texto in ["sair", "encerrar", "fechar"]:
                falar("Encerrando sistema.")
                break

            # MODO DITADO:
            # escreve qualquer coisa sem precisar dizer Tatsu
            # para quando ouvir Tatsu
            if dictation.DICTATION_MODE:
                if detectar_wake_word(texto):
                    dictation.parar_dictado()
                    falar("Modo escrita desativado.")
                elif texto:
                    dictation.escrever_texto(texto + " ")

                continue

            # MODO NORMAL:
            # precisa dizer Tatsu para ativar
            if detectar_wake_word(texto):
                falar("Sim?")

                comando = ouvir_local()

                if comando:
                    print("Comando:", comando)

                resposta = executar_comando(comando)

                if resposta:
                    falar(resposta)
                else:
                    falar("Comando não reconhecido.")


if __name__ == "__main__":
    if MODO_TEXTO:
        rodar_modo_texto()
    else:
        rodar_modo_voz()