import speech_recognition as sr
from runtime import definir_ultimo_comando, esta_rodando, esta_ativo
from config import WAKE_WORDS, LISTEN_TIME_WAKE, LISTEN_TIME_COMMAND
from speech_local import ouvir_local
from router import executar_comando
from speaker import falar
from runtime import esta_rodando
from tray import iniciar_tray
from voice_auth import frase_autorizada
import threading
import time
import commands.dictation as dictation
import threading
import time
from config import (
    WAKE_WORDS,
    LISTEN_TIME_WAKE,
    LISTEN_TIME_COMMAND,
    AUTH_VOICE_ENABLED,
    MODO_TEXTO
)
from runtime import (
    esta_rodando,
    esta_ativo,
    definir_status,
    definir_ultimo_texto,
    definir_ultimo_comando
)
from control_panel import iniciar_interface
from web_server import iniciar_servidor_web
from tunnel import iniciar_tunel
import time




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
        definir_ultimo_texto(texto)

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

            if AUTH_VOICE_ENABLED:
                definir_status("Confirmando identidade")
                falar("Confirme sua identidade.")

                confirmacao = ouvir_local()
                definir_ultimo_texto(confirmacao)

                print("Confirmação recebida:", confirmacao)

        if not frase_autorizada(confirmacao):
            definir_status("Voz não autorizada")
            falar("Voz não autorizada.")
            definir_status("Ouvindo")
            continue

        definir_status("Aguardando comando")
        falar("Sim?")

        print("DEBUG: vai ouvir comando agora")

        comando = ouvir_local()
        definir_ultimo_comando(comando)

        print("Comando recebido:", comando)

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
            target=rodar_modo_voz,
            daemon=True
        )

        web_thread = threading.Thread(
            target=iniciar_servidor_web,
            daemon=True
        )

        voz_thread.start()

        web_thread.start()

        time.sleep(2)

        iniciar_tunel()

        iniciar_interface()