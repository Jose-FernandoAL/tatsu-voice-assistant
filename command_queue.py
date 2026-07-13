import queue
import threading
import time
from router import executar_comando

from ai_assistant import perguntar_ia


fila_comandos = queue.Queue()


def comando_nao_reconhecido(resposta):
    """
    Verifica se o router não encontrou
    um comando local correspondente.
    """

    if resposta is None:
        return True

    texto = str(resposta).lower().strip()

    respostas_desconhecidas = [
        "",
         "comando não reconhecido",
        "comando não reconhecido.",
        "comando nao reconhecido",
        "comando nao reconhecido.",
        "comando não encontrado",
        "comando não encontrado.",
        "comando nao encontrado",
        "comando nao encontrado.",
        "não entendi",
        "não entendi.",
        "nao entendi"
        ]

    return texto in respostas_desconhecidas


def criar_resultado_local(resposta):
    """
    Padroniza a resposta de comandos locais.

    A mesma mensagem poderá ser exibida
    na web e falada pelo Nexus.
    """

    texto = str(resposta).strip()

    return {
        "tipo": "comando",
        "resposta_completa": texto,
        "resumo_voz": texto,
        "provedor": "local"
    }


def processar_comando(comando):
    """
    Primeiro tenta executar um comando local.

    Se o router não reconhecer,
    envia a pergunta para a IA.
    """

    resposta_local = executar_comando(
        comando
    )

    time.sleep(0.2
    )

    print(
    "DEBUG RESPOSTA DO ROUTER:",
    repr(resposta_local)
    )


    if not comando_nao_reconhecido(
        resposta_local
    ):

        return criar_resultado_local(
            resposta_local
        )


    print(
        "Comando local não encontrado."
    )

    print(
        "Enviando para a IA..."
    )


    resultado_ia = perguntar_ia(
        comando
    )


    resultado_ia["tipo"] = "ia"


    return resultado_ia


def processar_fila():
    """
    Consome os comandos da fila
    um por vez.
    """

    while True:

        item = fila_comandos.get()


        if item is None:

            fila_comandos.task_done()

            break


        comando = item[
            "comando"
        ]

        fila_resposta = item[
            "fila_resposta"
        ]


        try:

            print(
                "Executando comando "
                f"da fila: {comando}"
            )


            resultado = processar_comando(
                comando
            )


            fila_resposta.put(
                resultado
            )


        except Exception as erro:

            print(
                "Erro ao processar "
                f"comando: {erro}"
            )


            fila_resposta.put({

                "tipo": "erro",

                "resposta_completa":
                    "Ocorreu um erro ao "
                    "processar a solicitação.",

                "resumo_voz":
                    "Não consegui processar "
                    "a solicitação.",

                "provedor":
                    "indisponível"

            })


        finally:

            fila_comandos.task_done()


def iniciar_fila_comandos():
    """
    Inicia a única thread que executa
    comandos locais e consultas à IA.
    """

    thread = threading.Thread(

        target=processar_fila,

        daemon=True

    )


    thread.start()


    print(
        "Fila de comandos iniciada."
    )


def enviar_comando(comando):
    """
    Coloca um comando na fila
    e aguarda seu resultado.
    """

    if not comando:

        return {

            "tipo": "erro",

            "resposta_completa":
                "Nenhum comando foi recebido.",

            "resumo_voz":
                "Nenhum comando foi recebido.",

            "provedor":
                "local"

        }


    fila_resposta = queue.Queue(
        maxsize=1
    )


    fila_comandos.put({

        "comando": comando,

        "fila_resposta":
            fila_resposta

    })


    return fila_resposta.get()