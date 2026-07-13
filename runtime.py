RODANDO = True
ATIVO = True
STATUS = "Iniciando..."
ULTIMO_TEXTO = ""
ULTIMO_COMANDO = ""
ORIGEM_ULTIMO_COMANDO = ""
LINK_REMOTO = ""
STATUS_TUNEL = "Desconectado"


FALANDO = False


def definir_falando(valor):
    global FALANDO
    FALANDO = valor


def esta_falando():
    return FALANDO

def definir_origem_comando(origem):
    global ORIGEM_ULTIMO_COMANDO
    ORIGEM_ULTIMO_COMANDO = origem


def obter_origem_comando():
    return ORIGEM_ULTIMO_COMANDO


def definir_link_remoto(link):
    global LINK_REMOTO
    LINK_REMOTO = link


def obter_link_remoto():
    return LINK_REMOTO


def definir_status_tunel(status):
    global STATUS_TUNEL
    STATUS_TUNEL = status


def obter_status_tunel():
    return STATUS_TUNEL

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