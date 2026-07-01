RODANDO = True
ATIVO = True
STATUS = "Iniciando..."


def pausar():
    global RODANDO, STATUS
    RODANDO = False
    STATUS = "Pausado"


def continuar_execucao():
    global RODANDO, STATUS
    RODANDO = True
    STATUS = "Ouvindo"


def encerrar():
    global ATIVO, STATUS
    ATIVO = False
    STATUS = "Encerrando"


def esta_rodando():
    return RODANDO


def esta_ativo():
    return ATIVO


def definir_status(novo_status):
    global STATUS
    STATUS = novo_status


def obter_status():
    return STATUS