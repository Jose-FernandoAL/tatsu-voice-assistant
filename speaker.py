import queue
import threading
from runtime import definir_falando
import pythoncom
import win32com.client
import time

fila_fala = queue.Queue()


def worker_fala():
    """
    Única thread responsável pela fala do Nexus.
    Usa o sistema de voz nativo do Windows.
    """

    pythoncom.CoInitialize()

    voz = win32com.client.Dispatch(
        "SAPI.SpVoice"
    )

    # Velocidade:
    # valores comuns: -2 até 2
    voz.Rate = 0

    # Volume:
    # 0 até 100
    voz.Volume = 100


    while True:

        texto = fila_fala.get()

        if texto is None:

            fila_fala.task_done()

            break


        try:

            print(
                f"Nexus: {texto}"
            )

            definir_falando(True)

            voz.Speak(
                str(texto)
            )

            time.sleep(
                0.4
            )
            definir_falando(False)


        except Exception as erro:

            print(
                "Erro na fala do Nexus:"
            )

            print(
                erro
            )


        finally:


            fila_fala.task_done()


    pythoncom.CoUninitialize()


thread_fala = threading.Thread(

    target=worker_fala,

    daemon=True

)

thread_fala.start()


def falar(texto):
    """
    Adiciona uma frase à fila.
    """

    if texto is None:

        return


    texto = str(
        texto
    ).strip()


    if texto:

        fila_fala.put(
            texto
        )


def aguardar_falas():
    """
    Aguarda todas as falas terminarem.
    """

    fila_fala.join()


def encerrar_fala():
    """
    Encerra a thread de fala.
    """

    fila_fala.put(
        None
    )