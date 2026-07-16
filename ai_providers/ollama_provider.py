import json
import urllib.request
import urllib.error

from config import AI_LOCAL_MODEL


OLLAMA_URL = "http://localhost:11434/api/chat"


def perguntar_ollama(pergunta, instrucoes):
    """
    Consulta a IA local usando a API HTTP do Ollama.

    Não usa a biblioteca 'ollama' do Python.
    Isso evita erro com pydantic_core bloqueado pelo Windows.
    """

    dados = {
        "model": AI_LOCAL_MODEL,
        "stream": False,
        "messages": [
            {
                "role": "system",
                "content": instrucoes
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
    }

    corpo = json.dumps(dados).encode("utf-8")

    requisicao = urllib.request.Request(
        OLLAMA_URL,
        data=corpo,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(
            requisicao,
            timeout=120
        ) as resposta:

            conteudo = resposta.read().decode("utf-8")
            resultado = json.loads(conteudo)

    except urllib.error.URLError as erro:
        raise RuntimeError(
            "Não foi possível conectar ao Ollama. "
            "Verifique se ele está aberto ou rode: ollama serve"
        ) from erro

    texto = (
        resultado
        .get("message", {})
        .get("content", "")
        .strip()
    )

    if not texto:
        raise RuntimeError(
            "O Ollama retornou uma resposta vazia."
        )

    return texto