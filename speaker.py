import pyttsx3
import threading
import queue
import time


fila_fala = queue.Queue()

engine = pyttsx3.init()
engine.setProperty("rate", 149.3)  # Velocidade da fala (palavras por minuto)
engine.setProperty("volume", 1.0)


def worker_fala():
    """
    Thread única responsável por falar.
    Isso evita várias partes do sistema tentando usar o pyttsx3 ao mesmo tempo.
    """
    while True:
        texto = fila_fala.get()

        if texto is None:
            break

        try:
            print(f"Nexus: {texto}")
            engine.say(texto)
            engine.runAndWait()

            # pequena pausa para evitar cortes entre frases
            time.sleep(0.2)

        except Exception as erro:
            print("Erro ao falar:")
            print(erro)

        finally:
            fila_fala.task_done()


thread_fala = threading.Thread(target=worker_fala)
thread_fala.daemon = True
thread_fala.start()


def falar(texto):
    """
    Adiciona uma fala na fila.
    Não fala diretamente.
    """
    if texto:
        fila_fala.put(texto)


def encerrar_fala():
    fila_fala.put(None)