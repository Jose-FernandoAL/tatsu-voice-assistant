import queue
import threading

from router import executar_comando


fila_comandos = queue.Queue()


def processar_fila():
    """
    Aguarda comandos e executa um por vez.

    Cada item possui:
    - comando
    - uma fila de resposta
    """

    while True:

        item = fila_comandos.get()

        if item is None:
            break

        comando = item["comando"]

        fila_resposta = item["fila_resposta"]

        try:

            print(
                f"Executando comando da fila: {comando}"
            )

            resposta = executar_comando(
                comando
            )

            if not resposta:

                resposta = (
                    "Comando executado."
                )

            fila_resposta.put(
                resposta
            )

        except Exception as erro:

            print(
                f"Erro ao executar comando: {erro}"
            )

            fila_resposta.put(
                "Erro ao executar comando."
            )

        finally:

            fila_comandos.task_done()


def iniciar_fila_comandos():

    print("DEBUG: iniciando fila")

    thread = threading.Thread(
        target=processar_fila,
        daemon=True
    )

    thread.start()

    print("Fila de comandos iniciada.")


def enviar_comando(comando):
    """
    Adiciona um comando à fila e aguarda
    a resposta do router.
    """

    if not comando:

        return "Comando vazio."

    fila_resposta = queue.Queue(
        maxsize=1
    )

    item = {
        "comando": comando,
        "fila_resposta": fila_resposta
    }

    fila_comandos.put(
        item
    )

    resposta = fila_resposta.get()

    return resposta