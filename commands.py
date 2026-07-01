import os
import subprocess
import time


# =========================
# FUNÇÃO BASE
# =========================

def abrir(caminho_ou_comando):
    try:
        os.startfile(caminho_ou_comando)
    except Exception:
        try:
            subprocess.Popen(caminho_ou_comando, shell=True)
        except Exception as erro:
            print(f"Erro ao abrir: {caminho_ou_comando}")
            print(erro)


# =========================
# PROGRAMAS
# =========================

def abrir_opera():
    print("Abrindo Opera...")
    os.system("start opera")

def abrir_vscode():
    print("Abrindo VS Code...")
    subprocess.Popen("code", shell=True)


def abrir_explorador():
    print("Abrindo Explorador de Arquivos...")
    subprocess.Popen("explorer", shell=True)


def abrir_bloco_notas():
    print("Abrindo Bloco de Notas...")
    subprocess.Popen("notepad", shell=True)


def abrir_calculadora():
    print("Abrindo Calculadora...")
    subprocess.Popen("calc", shell=True)


def abrir_paint():
    print("Abrindo Paint...")
    subprocess.Popen("mspaint", shell=True)


def abrir_cmd():
    print("Abrindo Prompt de Comando...")
    subprocess.Popen("cmd", shell=True)


def abrir_powershell():
    print("Abrindo PowerShell...")
    subprocess.Popen("powershell", shell=True)


def abrir_configuracoes():
    print("Abrindo Configurações...")
    subprocess.Popen("start ms-settings:", shell=True)


def abrir_downloads():
    print("Abrindo Downloads...")
    abrir(r"C:\Users\josef\Downloads")


def abrir_documentos():
    print("Abrindo Documentos...")
    abrir(r"C:\Users\josef\Documents")


def abrir_area_trabalho():
    print("Abrindo Área de Trabalho...")
    abrir(r"C:\Users\josef\Desktop")


# =========================
# ROTINAS / COMBOS
# =========================

def modo_estudo():
    print("Ativando modo estudo...")
    abrir_opera()
    time.sleep(1)
    abrir_bloco_notas()
    time.sleep(1)
    abrir_documentos()


def modo_programacao():
    print("Ativando modo programação...")
    abrir_vscode()
    time.sleep(1)
    abrir_opera()
    time.sleep(1)
    abrir_explorador()


def modo_terminal():
    print("Ativando modo terminal...")
    abrir_cmd()
    time.sleep(1)
    abrir_powershell()


def modo_faculdade():
    print("Ativando modo faculdade...")
    abrir_opera()
    time.sleep(1)
    abrir_documentos()
    time.sleep(1)
    abrir_bloco_notas()


# =========================
# LISTA DE COMANDOS
# =========================

COMANDOS = {
    # Navegador
    "abrir navegador": abrir_opera,
    "abrir opera": abrir_opera,

    # Programação
    "abrir vscode": abrir_vscode,
    "abrir visual studio": abrir_vscode,
    "abrir código": abrir_vscode,

    # Windows
    "abrir pasta": abrir_explorador,
    "abrir explorador": abrir_explorador,
    "abrir arquivos": abrir_explorador,
    "abrir downloads": abrir_downloads,
    "abrir documentos": abrir_documentos,
    "abrir área de trabalho": abrir_area_trabalho,

    # Ferramentas
    "abrir bloco de notas": abrir_bloco_notas,
    "abrir calculadora": abrir_calculadora,
    "abrir paint": abrir_paint,
    "abrir cmd": abrir_cmd,
    "abrir terminal": abrir_cmd,
    "abrir powershell": abrir_powershell,
    "abrir configurações": abrir_configuracoes,

    # Combos
    "modo estudo": modo_estudo,
    "modo programação": modo_programacao,
    "modo programar": modo_programacao,
    "modo terminal": modo_terminal,
    "modo faculdade": modo_faculdade,
}