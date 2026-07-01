import speech_recognition as sr

from config import WAKE_WORDS, LISTEN_TIME_WAKE, LISTEN_TIME_COMMAND
from speech import preparar_microfone, ouvir
from router import executar_comando
from speaker import falar


MODO_TEXTO = False


def detectar_wake_word(texto):
    return any(palavra in texto for palavra in WAKE_WORDS)


def rodar_modo_texto():
    print("Tatsu iniciado em modo texto.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        texto = input("Você: ").lower()

        if texto == "sair":
            print("Encerrando...")
            break

        if detectar_wake_word(texto):
            falar("Ativado.")
            comando = input("Comando: ").lower()

            if not executar_comando(comando):
                falar("Comando não reconhecido.")


def rodar_modo_voz():
    with sr.Microphone() as source:
        preparar_microfone(source)

        falar("Sistema iniciado.")

        while True:
            print("\nAguardando ativação...")
            texto = ouvir(source, LISTEN_TIME_WAKE)

            if texto:
                print("Ouvi:", texto)

            if detectar_wake_word(texto):
                falar("Sim?")

                comando = ouvir(source, LISTEN_TIME_COMMAND)

                if comando:
                    print("Comando:", comando)

                if not executar_comando(comando):
                    falar("Comando não reconhecido.")


if __name__ == "__main__":
    if MODO_TEXTO:
        rodar_modo_texto()
    else:
        rodar_modo_voz()