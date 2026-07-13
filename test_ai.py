import time

from ai_assistant import perguntar_ia


pergunta = input(
    "Pergunta para o Nexus: "
)

inicio = time.time()

resultado = perguntar_ia(
    pergunta
)

fim = time.time()


print(
    f"\nTempo de resposta: "
    f"{fim - inicio:.2f} segundos"
)


print(
    "\nPROVEDOR:"
)

print(
    resultado["provedor"]
)


print(
    "\nRESPOSTA COMPLETA:"
)

print(
    resultado["resposta_completa"]
)


print(
    "\nRESUMO PARA VOZ:"
)

print(
    resultado["resumo_voz"]
)