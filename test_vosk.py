from speech_local import ouvir_local

while True:
    texto = ouvir_local()
    print("Você disse:", texto)

    if "sair" in texto:
        break