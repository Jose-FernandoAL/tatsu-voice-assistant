import queue
import subprocess
import threading

from runtime import definir_falando


fila_fala = queue.Queue()


def escapar_texto_powershell(texto):
    """
    Escapa aspas simples para o PowerShell.
    """
    return str(texto).replace("'", "''")


def falar_windows(texto):
    """
    Usa o sintetizador de voz do Windows via PowerShell.

    Isso evita pythoncom, win32com e pywin32,
    que foram bloqueados pela segurança do Windows.
    """

    texto_seguro = escapar_texto_powershell(texto)

    comando = (
        "Add-Type -AssemblyName System.Speech; "
        "$voz = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        "$voz.Rate = 0; "
        "$voz.Volume = 100; "
        f"$voz.Speak('{texto_seguro}');"
    )

    subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            comando
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def worker_fala():
    while True:
        texto = fila_fala.get()

        if texto is None:
            fila_fala.task_done()
            break

        try:
            print(f"Nexus: {texto}")

            definir_falando(True)

            falar_windows(texto)

        except Exception as erro:
            print("Erro na fala do Nexus:")
            print(erro)

        finally:
            definir_falando(False)
            fila_fala.task_done()


thread_fala = threading.Thread(
    target=worker_fala,
    daemon=True
)

thread_fala.start()


def falar(texto):
    if texto is None:
        return

    texto = str(texto).strip()

    if texto:
        fila_fala.put(texto)


def aguardar_falas():
    fila_fala.join()


def encerrar_fala():
    fila_fala.put(None)