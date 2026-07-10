import os
import re
import subprocess
import threading


CAMINHO_CLOUDFLARED = os.path.join(
    os.path.dirname(__file__),
    "cloudflared.exe"
)


def ler_saida_tunel(processo):
    """
    Lê as mensagens do cloudflared e procura
    o endereço remoto criado.
    """

    for linha in processo.stdout:

        linha = linha.strip()

        # Mostra as mensagens do cloudflared no terminal.
        print(linha)

        # Procura o endereço terminado em trycloudflare.com.
        resultado = re.search(
            r"https://[a-zA-Z0-9-]+\.trycloudflare\.com",
            linha
        )

        if resultado:

            endereco = resultado.group()

            print("\n" + "=" * 60)

            print("ACESSO REMOTO DO NEXUS:")

            print(endereco)

            print("=" * 60 + "\n")


def iniciar_tunel():
    """
    Inicia o Cloudflare Tunnel.

    Caso ocorra uma falha, o Nexus continua
    funcionando com voz e acesso local.
    """

    if not os.path.exists(CAMINHO_CLOUDFLARED):

        print(
            "Aviso: cloudflared.exe não encontrado."
        )

        print(
            "O Nexus continuará com acesso local."
        )

        return None


    try:

        print(
            "Iniciando acesso remoto..."
        )


        processo = subprocess.Popen(

            [
                CAMINHO_CLOUDFLARED,
                "tunnel",
                "--url",
                "http://localhost:5000"
            ],

            stdout=subprocess.PIPE,

            stderr=subprocess.STDOUT,

            text=True,

            encoding="utf-8",

            errors="replace"

        )


        thread_saida = threading.Thread(

            target=ler_saida_tunel,

            args=(processo,),

            daemon=True

        )


        thread_saida.start()


        return processo


    except Exception as erro:

        print(
            "Não foi possível iniciar "
            "o acesso remoto."
        )

        print(
            f"Erro: {erro}"
        )

        print(
            "O Nexus continuará "
            "com acesso local."
        )

        return None