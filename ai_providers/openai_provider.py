import os

from openai import OpenAI


def perguntar_openai(
    pergunta,
    instrucoes
):
    """
    Envia uma pergunta para a OpenAI.

    Retorna o texto produzido pelo modelo.
    """

    chave = os.getenv(
        "OPENAI_API_KEY"
    )

    modelo = os.getenv(
        "OPENAI_MODEL"
    )


    if not chave:

        raise RuntimeError(
            "OPENAI_API_KEY não encontrada."
        )


    if not modelo:

        raise RuntimeError(
            "OPENAI_MODEL não definido."
        )


    cliente = OpenAI(
        api_key=chave
    )


    resposta = cliente.responses.create(

        model=modelo,

        instructions=instrucoes,

        input=pergunta

    )


    texto = resposta.output_text


    if not texto:

        raise RuntimeError(
            "A OpenAI retornou uma resposta vazia."
        )


    return texto