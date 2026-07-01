from commands.apps import APP_COMMANDS
from commands.routines import ROUTINE_COMMANDS
from commands.system import SYSTEM_COMMANDS
from commands.media import MEDIA_COMMANDS
from matcher import encontrar_comando
from commands.dictation import DICTATION_COMMANDS


COMMANDS = {}
COMMANDS.update(APP_COMMANDS)
COMMANDS.update(ROUTINE_COMMANDS)
COMMANDS.update(SYSTEM_COMMANDS)
COMMANDS.update(MEDIA_COMMANDS)
COMMANDS.update(DICTATION_COMMANDS)

def executar_comando(texto):
    frase, funcao = encontrar_comando(texto, COMMANDS)

    if funcao:
        funcao()
        return f"Executando {frase}"

    return None