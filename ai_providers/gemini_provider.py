import os

from google import genai


def perguntar_gemini(
    pergunta,
    instrucoes
):
    """
    Envia uma pergunta para o Gemini.

    Retorna o texto produzido pelo modelo.
    """

    chave = os.getenv(
        "GEMINI_API_KEY"
    )

    modelo = os.getenv(
        "GEMINI_MODEL"
    )


    if not chave:

        raise RuntimeError(
            "GEMINI_API_KEY não encontrada."
        )


    if not modelo:

        raise RuntimeError(
            "GEMINI_MODEL não definido."
        )


    cliente = genai.Client(
        api_key=chave
    )


    prompt = f"""
{instrucoes}

PERGUNTA DO USUÁRIO:

{pergunta}
"""


    resposta = (
        cliente.models.generate_content(

            model=modelo,

            contents=prompt

        )
    )


    texto = resposta.text


    if not texto:

        raise RuntimeError(
            "O Gemini retornou uma resposta vazia."
        )


    return texto