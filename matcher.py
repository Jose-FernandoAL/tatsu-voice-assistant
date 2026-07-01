def encontrar_comando(texto, comandos):
    texto = texto.lower()

    for frase, funcao in comandos.items():
        if frase in texto:
            return frase, funcao

    return None, None