import speech_recognition as sr
from runtime import esta_rodando, esta_ativo
from config import WAKE_WORDS, LISTEN_TIME_WAKE, LISTEN_TIME_COMMAND
from speech_local import ouvir_local
from router import executar_comando
from speaker import falar
from runtime import esta_rodando
from tray import iniciar_tray
import threading
import time
import commands.dictation as dictation
import threading
import time

from runtime import esta_rodando, esta_ativo, definir_status
from control_panel import iniciar_interface



MODO_TEXTO = False


def detectar_wake_word(texto):
    return any(palavra in texto for palavra in WAKE_WORDS)


def rodar_modo_texto():
    print("Nexus iniciado em modo texto.")
    print("Digite 'sair' para encerrar.\n")

    while esta_ativo():
        
        if not esta_rodando():
            time.sleep(1)
            continue
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
    print("Nexus iniciado em modo voz.")
    definir_status("Ouvindo")
    falar("Nexus iniciado.")

    while esta_ativo():

        if not esta_rodando():
            definir_status("Pausado")
            time.sleep(1)
            continue

        definir_status("Aguardando ativação")
        print("\nAguardando ativação...")

        texto = ouvir_local()

        print("Texto recebido:", texto)

        if dictation.DICTATION_MODE:
            definir_status("Modo ditado ativo")

            if detectar_wake_word(texto):
                dictation.parar_dictado()
                definir_status("Ouvindo")
                falar("Modo escrita desativado.")

            elif texto:
                dictation.escrever_texto(texto + " ")

            continue

        if detectar_wake_word(texto):
            definir_status("Aguardando comando")
            falar("Sim?")

            comando = ouvir_local()

            print("Comando recebido:", comando)

            definir_status(f"Executando: {comando}")

            resposta = executar_comando(comando)

            if resposta:
                falar(resposta)
            else:
                falar("Comando não reconhecido.")

            definir_status("Ouvindo")

    falar("Nexus encerrado.")

if __name__ == "__main__":

    if MODO_TEXTO:
        rodar_modo_texto()

    else:
        voz_thread = threading.Thread(
            target=rodar_modo_voz
        )

        voz_thread.daemon = True
        voz_thread.start()

        iniciar_interface()