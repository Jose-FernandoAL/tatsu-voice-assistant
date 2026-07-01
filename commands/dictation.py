import pyautogui

DICTATION_MODE = False


def ativar_dictado():
    global DICTATION_MODE
    DICTATION_MODE = True
    print("Modo ditado ativado")


def parar_dictado():
    global DICTATION_MODE
    DICTATION_MODE = False
    print("Modo ditado desativado")


def escrever_texto(texto):
    pyautogui.write(texto, interval=0.03)


DICTATION_COMMANDS = {
    "modo escrita": ativar_dictado,
    "ativar escrita": ativar_dictado,
    "modo ditado": ativar_dictado,
    "ativar ditado": ativar_dictado,
    "parar escrita": parar_dictado,
    "parar ditado": parar_dictado,
}