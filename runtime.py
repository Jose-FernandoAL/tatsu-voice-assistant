RODANDO = True
ATIVO = True


def pausar():
    global RODANDO
    RODANDO = False


def continuar_execucao():
    global RODANDO
    RODANDO = True


def encerrar():
    global ATIVO
    ATIVO = False


def esta_rodando():
    return RODANDO


def esta_ativo():
    return ATIVO