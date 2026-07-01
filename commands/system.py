import keyboard
import pyautogui
from runtime import encerrar


def encerrar_nexus():
    print("Encerrando Nexus...")
    encerrar()

def copiar():
    keyboard.press_and_release("ctrl+c")


def colar():
    keyboard.press_and_release("ctrl+v")


def fechar_janela():
    keyboard.press_and_release("alt+f4")

def nexus():
    print("Encerrando Nexus...")
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
    "encerrar sistema": nexus,
    "desligar nexus": encerrar_nexus,
    "sair": encerrar_nexus,
    "encerrar sistema": encerrar_nexus,
    "desligar sistema": encerrar_nexus,
    "encerrar": encerrar_nexus,
    "fechar sistema": encerrar_nexus,
    "fechar": encerrar_nexus,
}