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

    print("Tatsu pausado")


def continuar_execucao(icon, item):
    global RODANDO

    RODANDO = True

    print("Tatsu ativo")


def sair(icon, item):
    print("Encerrando Tatsu")

    icon.stop()


def iniciar_tray():

    icon = Icon(
        "Tatsu",
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
            print("Tatsu executando...")

        time.sleep(3)


if __name__ == "__main__":

    thread = threading.Thread(target=loop_principal)

    thread.daemon = True

    thread.start()

    iniciar_tray()