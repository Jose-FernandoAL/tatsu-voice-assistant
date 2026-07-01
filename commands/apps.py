import os
import subprocess


def abrir(caminho_ou_comando):
    try:
        os.startfile(caminho_ou_comando)
    except Exception:
        subprocess.Popen(caminho_ou_comando, shell=True)


def abrir_opera():
    os.system ("start opera")

def abrir_spotify():
    os.startfile(r"C:\Users\josef\AppData\Roaming\Spotify\Spotify.exe")


def abrir_vscode():
    subprocess.Popen("code", shell=True)


def abrir_explorador():
    subprocess.Popen("explorer", shell=True)


def abrir_bloco_notas():
    subprocess.Popen("notepad", shell=True)


def abrir_calculadora():
    subprocess.Popen("calc", shell=True)


APP_COMMANDS = {
    "abrir spotify": abrir_spotify,
    "abrir opera": abrir_opera,
    "abre opera": abrir_opera,
    "abrir navegador": abrir_opera,
    "abre navegador": abrir_opera,
    "iniciar navegador": abrir_opera,

    "abrir vscode": abrir_vscode,
    "abre vscode": abrir_vscode,
    "abrir visual studio": abrir_vscode,
    "abrir código": abrir_vscode,
    "iniciar programação": abrir_vscode,

    "abrir pasta": abrir_explorador,
    "abre pasta": abrir_explorador,
    "abrir explorador": abrir_explorador,

    "abrir bloco de notas": abrir_bloco_notas,
    "abre bloco de notas": abrir_bloco_notas,

    "abrir calculadora": abrir_calculadora,
    "abre calculadora": abrir_calculadora,
}