import keyboard
import pyautogui


def copiar():
    keyboard.press_and_release("ctrl+c")


def colar():
    keyboard.press_and_release("ctrl+v")


def fechar_janela():
    keyboard.press_and_release("alt+f4")

def encerrar_tatsu():
    print("Encerrando Tatsu...")
    raise SystemExit

def enter():
    keyboard.press_and_release("enter")


def pausar():
    keyboard.press_and_release("space")



SYSTEM_COMMANDS = {
    "copiar": copiar,
    "colar": colar,
    "fechar janela": fechar_janela,
    "dar enter": enter,
    "pressionar enter": enter,
    "pausar": pausar,
    "continuar": pausar,
    "encerrar sistema": encerrar_tatsu,
    "desligar tatsu": encerrar_tatsu,
    "sair": encerrar_tatsu,
   
}