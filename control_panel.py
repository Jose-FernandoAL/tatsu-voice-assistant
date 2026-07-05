import tkinter as tk
from speaker import falar

from runtime import (
     obter_ultimo_texto,
    obter_ultimo_comando,
    pausar,
    continuar_execucao,
    encerrar,
    obter_status,
    esta_rodando,
    esta_ativo
)


def iniciar_interface():
    janela = tk.Tk()
    janela.title("Nexus Control Panel")
    janela.geometry("420x280")
    janela.resizable(False, False)

    titulo = tk.Label(
        janela,
        text="Nexus Voice Assistant",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=20)

    label_status_titulo = tk.Label(
        janela,
        text="Status atual:",
        font=("Arial", 12)
    )
    label_status_titulo.pack()

    label_status = tk.Label(
        janela,
        text="Carregando...",
        font=("Arial", 14, "bold")
    )
    label_status.pack(pady=10)
    label_ultimo_texto_titulo = tk.Label(
    janela,
    text="Último texto reconhecido:",
    font=("Arial", 10, "bold")
    )
    label_ultimo_texto_titulo.pack(pady=(10, 0))

    label_ultimo_texto = tk.Label(
    janela,
    text="-",
    font=("Arial", 10),
    wraplength=360
    )
    label_ultimo_texto.pack(pady=5)

    label_ultimo_comando_titulo = tk.Label(
    janela,
    text="Último comando:",
    font=("Arial", 10, "bold")
    )
    label_ultimo_comando_titulo.pack(pady=(10, 0))

    label_ultimo_comando = tk.Label(
    janela,
    text="-",
    font=("Arial", 10),
    wraplength=360
    )
    label_ultimo_comando.pack(pady=5)

    def atualizar_status():
        if esta_ativo():
            label_status.config(text=obter_status())
            janela.after(500, atualizar_status)
        else:
            label_status.config(text="Encerrado")
            janela.after(800, janela.destroy)

    def pausar_nexus():
            pausar()
            label_status.config(text="Pausado")
            falar("Nexus pausado.")


    def continuar_nexus():
        continuar_execucao()
        label_status.config(text="Ouvindo")
        falar("Nexus ativo.")


    def encerrar_nexus():
        encerrar()
        label_status.config(text="Encerrando...")
        falar("Encerrando Nexus.")

    btn_pausar = tk.Button(
        janela,
        text="Pausar",
        width=25,
        height=2,
        command=pausar_nexus
    )
    btn_pausar.pack(pady=5)

    btn_continuar = tk.Button(
        janela,
        text="Continuar",
        width=25,
        height=2,
        command=continuar_nexus
    )
    btn_continuar.pack(pady=5)

    btn_encerrar = tk.Button(
        janela,
        text="Encerrar Nexus",
        width=25,
        height=2,
        command=encerrar_nexus
    )
    btn_encerrar.pack(pady=5)

    atualizar_status()

    janela.mainloop()