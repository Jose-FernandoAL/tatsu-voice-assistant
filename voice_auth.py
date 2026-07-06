FRASES_AUTORIZADAS = [
    "sou jose",
    "eu sou jose",
    "sou josé",
    "eu sou josé",
    "nexus sou jose",
    "nexus sou josé",
    "jose",
    "josé",
    "ze",
    "zé",
    "fernando",
    "jose fernando",
    "josé fernando",
    "confirmar identidade",
    "identidade confirmada",
    "autorizado",
    "comando autorizado",
]


def normalizar_texto(texto):
    """
    Padroniza o texto para facilitar comparação.
    """
    if texto is None:
        return ""

    texto = texto.lower().strip()

    substituicoes = {
        "josé": "jose",
        "néxus": "nexus",
    }

    for antigo, novo in substituicoes.items():
        texto = texto.replace(antigo, novo)

    return texto


def frase_autorizada(texto):
    """
    Verifica se o texto ouvido está dentro do mini dicionário autorizado.
    """
    texto_normalizado = normalizar_texto(texto)

    for frase in FRASES_AUTORIZADAS:
        frase_normalizada = normalizar_texto(frase)

        if frase_normalizada in texto_normalizado:
            return True

    return False