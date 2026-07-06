from voice_auth import frase_autorizada

testes = [
    "sou jose",
    "eu sou josé",
    "nexus sou jose",
    "abrir opera",
    "qualquer coisa",
    "identidade confirmada",
    "comando autorizado"
]

for texto in testes:
    print(texto, "=>", frase_autorizada(texto))