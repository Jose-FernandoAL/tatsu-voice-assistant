from os import link
import tkinter as tk
from speaker import falar

from runtime import (
    obter_origem_comando,
    obter_link_remoto,
    obter_status_tunel,
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
    janela.geometry("460x600")
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

    label_origem_titulo = tk.Label(
    janela,
    text="Origem do comando:",
    font=("Arial", 10, "bold")
    )
    label_origem_titulo.pack(pady=(10, 0))

    label_origem = tk.Label(
        janela,
        text="-",
        font=("Arial", 10)
    )
    label_origem.pack(pady=5)


    label_tunel_titulo = tk.Label(
        janela,
        text="Acesso remoto:",
        font=("Arial", 10, "bold")
    )
    label_tunel_titulo.pack(pady=(10, 0))

    label_tunel = tk.Label(
        janela,
        text="Desconectado",
        font=("Arial", 10)
    )
    label_tunel.pack(pady=5)


    label_link = tk.Label(
        janela,
        text="Link ainda não disponível",
        font=("Arial", 9),
        wraplength=360
    )
    label_link.pack(pady=5)


    def copiar_link():
        link = obter_link_remoto()

        if not link:
            return

        janela.clipboard_clear()
        janela.clipboard_append(link)
        janela.update()

        btn_copiar.config(
            text="Link copiado!"
        )

        janela.after(
            1500,
            restaurar_texto_botao
        )


    def restaurar_texto_botao():
        btn_copiar.config(
            text="Copiar link"
        )


    btn_copiar = tk.Button(
        janela,
        text="Copiar link",
        command=copiar_link
    )

    btn_copiar.pack(
        pady=10
    )

    def atualizar_status():
        if esta_ativo():
            label_status.config(text=obter_status())
            janela.after(500, atualizar_status)
        else:
            label_status.config(text="Encerrado")
            janela.after(800, janela.destroy)
        label_origem.config(
    text=obter_origem_comando() or "-"
    )

    label_tunel.config(
        text=obter_status_tunel()
    )

    label_link.config(
        text=(
            obter_link_remoto()
            or
            "Link ainda não disponível"
        )
    )

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
    btn_copiar = tk.Button(
    janela,
    text="Copiar link",
    command=copiar_link
)

    btn_copiar.pack(
    pady=10
    )

    atualizar_status()

    janela.mainloop()