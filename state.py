estado = {
    "modo": None
}


def definir_modo(nome):
    estado["modo"] = nome


def obter_modo():
    return estado["modo"]