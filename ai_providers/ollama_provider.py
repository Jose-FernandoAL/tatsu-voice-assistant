from ollama import chat

from config import AI_LOCAL_MODEL


def perguntar_ollama(
    pergunta,
    instrucoes
):
    """
    Consulta a IA local usando Ollama.

    Não envia a pergunta para a internet.
    """

    resposta = chat(

        model=AI_LOCAL_MODEL,

        messages=[

            {
                "role": "system",
                "content": instrucoes
            },

            {
                "role": "user",
                "content": pergunta
            }

        ]

    )


    texto = resposta[
        "message"
    ][
        "content"
    ]


    if not texto:

        raise RuntimeError(
            "O Ollama retornou uma resposta vazia."
        )


    return texto