RODANDO = True
ATIVO = True
STATUS = "Iniciando..."
ULTIMO_TEXTO = ""
ULTIMO_COMANDO = ""

def definir_ultimo_texto(texto):
    global ULTIMO_TEXTO
    ULTIMO_TEXTO = texto


def obter_ultimo_texto():
    return ULTIMO_TEXTO


def definir_ultimo_comando(comando):
    global ULTIMO_COMANDO
    ULTIMO_COMANDO = comando


def obter_ultimo_comando():
    return ULTIMO_COMANDO

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