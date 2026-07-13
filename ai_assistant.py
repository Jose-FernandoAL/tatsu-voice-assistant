from dotenv import load_dotenv
from ai_providers.ollama_provider import (
    perguntar_ollama
)
from config import (
    AI_SYSTEM_PROMPT,
    AI_PRIMARY_PROVIDER,
    AI_FALLBACK_PROVIDER,
    AI_LAST_PROVIDER
)

from ai_providers.openai_provider import (
    perguntar_openai
)

from ai_providers.gemini_provider import (
    perguntar_gemini
)


load_dotenv()


PROVEDORES = {

    "openai": perguntar_openai,
    "ollama": perguntar_ollama,
    "gemini": perguntar_gemini

}


def separar_resposta(texto):
    """
    Separa a resposta completa
    do resumo que será falado.
    """

    marcador_resposta = (
        "RESPOSTA_COMPLETA:"
    )

    marcador_resumo = (
        "RESUMO_VOZ:"
    )


    if (
        marcador_resposta in texto
        and
        marcador_resumo in texto
    ):

        parte_completa = texto.split(
            marcador_resposta,
            1
        )[1]


        resposta_completa, resumo_voz = (
            parte_completa.split(
                marcador_resumo,
                1
            )
        )


        resposta_completa = (
            resposta_completa.strip()
        )


        resumo_voz = (
            resumo_voz.strip()
        )


        return {
            "resposta_completa":
                resposta_completa,

            "resumo_voz":
                resumo_voz
        }


    # Fallback caso o modelo não siga
    # exatamente o formato solicitado.

    texto = texto.strip()


    resumo = texto


    if len(resumo) > 350:

        resumo = (
            resumo[:347]
            + "..."
        )


    return {

        "resposta_completa": texto,

        "resumo_voz": resumo

    }


def consultar_provedor(
    nome_provedor,
    pergunta
):
    """
    Consulta um provedor específico.
    """

    funcao = PROVEDORES.get(
        nome_provedor
    )


    if funcao is None:

        raise ValueError(
            f"Provedor inválido: "
            f"{nome_provedor}"
        )


    return funcao(

        pergunta,

        AI_SYSTEM_PROMPT

    )


def perguntar_ia(pergunta):
    """
    Tenta o provedor principal.

    Se ocorrer erro,
    tenta o provedor reserva.
    """

    erros = []


    for provedor in [

        AI_PRIMARY_PROVIDER,

        AI_FALLBACK_PROVIDER,

        AI_LAST_PROVIDER

]:  

        try:

            print(
                f"Consultando IA: "
                f"{provedor}"
            )


            texto = consultar_provedor(

                provedor,

                pergunta

            )


            resultado = separar_resposta(
                texto
            )


            resultado["provedor"] = (
                provedor
            )


            return resultado


        except Exception as erro:

            mensagem = (
                f"{provedor}: {erro}"
            )


            erros.append(
                mensagem
            )


            print(
                "Falha no provedor:",
                mensagem
            )


    return {

        "resposta_completa": (
            "Os serviços de inteligência "
            "artificial estão indisponíveis "
            "no momento."
        ),

        "resumo_voz": (
            "Não consegui acessar os "
            "serviços de pesquisa."
        ),

        "provedor": "indisponível",

        "erros": erros

    }