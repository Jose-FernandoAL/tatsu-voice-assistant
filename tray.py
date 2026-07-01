from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import threading
import time


RODANDO = True


def criar_icone():

    imagem = Image.new("RGB", (64, 64), "black")

    draw = ImageDraw.Draw(imagem)

    draw.ellipse((16, 16, 48, 48), fill="white")

    return imagem


def pausar(icon, item):
    global RODANDO

    RODANDO = False

    print("nexus pausado")


def continuar_execucao(icon, item):
    global RODANDO

    RODANDO = True

    print("nexus ativo")


def sair(icon, item):
    print("Encerrando nexus")
    icon.stop()


def iniciar_tray():

    icon = Icon(
        "nexus",
        criar_icone(),
        menu=Menu(
            MenuItem("Pausar", pausar),
            MenuItem("Continuar", continuar_execucao),
            MenuItem("Sair", sair)
        )
    )

    icon.run()


def loop_principal():

    while True:

        if RODANDO:
            print("nexus executando...")

        time.sleep(3)


if __name__ == "__main__":

    thread = threading.Thread(target=loop_principal)

    thread.daemon = True

    thread.start()

    iniciar_tray()