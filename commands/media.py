import pyautogui
import keyboard


def pausar_video():
    pyautogui.press("space")


def proxima_musica():
    pyautogui.press("nexttrack")


def musica_anterior():
    pyautogui.press("prevtrack")


def aumentar_volume():
    pyautogui.press("volumeup")


def diminuir_volume():
    pyautogui.press("volumedown")


def mutar():
    pyautogui.press("volumemute")


def tela_cheia():
    keyboard.press_and_release("f")


MEDIA_COMMANDS = {
    "pausar vídeo": pausar_video,
    "pausar": pausar_video,
    "continuar vídeo": pausar_video,
    "continuar": pausar_video,

    "próxima música": proxima_musica,
    "próximo vídeo": proxima_musica,

    "música anterior": musica_anterior,
    "vídeo anterior": musica_anterior,

    "aumentar volume": aumentar_volume,
    "diminuir volume": diminuir_volume,
    "mutar": mutar,
    "tirar som": mutar,

    "tela cheia": tela_cheia,
}