import time
from commands.apps import abrir_opera, abrir_vscode, abrir_explorador, abrir_bloco_notas


def modo_estudo():
    abrir_opera()
    time.sleep(1)
    abrir_bloco_notas()


def modo_programacao():
    abrir_vscode()
    time.sleep(1)
    abrir_opera()
    time.sleep(1)
    abrir_explorador()


ROUTINE_COMMANDS = {
    "modo estudo": modo_estudo,
    "modo programação": modo_programacao,
    "modo programar": modo_programacao,
}