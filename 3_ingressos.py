"""
ingressos.py
Sistemas Operacionais - Aula 06 - Mutex e Semáforos

Um site de shows possui apenas 1 ingresso restante. Dois compradores
(Cliente-A e Cliente-B) tentam comprar esse ingresso no mesmo
milissegundo.

Tarefa:
    1. Rode o programa algumas vezes e observe a saída no terminal.
    2. Identifique a condição de corrida (dica: preste atenção em
       quantos clientes conseguem "comprar" e no valor final de
       ingressos_disponiveis).
    3. Corrija o código usando um "with lock:" ao redor da região
       crítica.
"""

import threading
import time

ingressos_disponiveis = 1


def comprar(cliente):
    global ingressos_disponiveis

    if ingressos_disponiveis > 0:
        print(f"{cliente}: verificou -> há ingresso disponível!")
        time.sleep(0.01)  # simula o tempo de processar o pagamento
        ingressos_disponiveis -= 1
        print(f"{cliente}: compra CONFIRMADA! Ingressos restantes: {ingressos_disponiveis}")
    else:
        print(f"{cliente}: que pena, ingresso esgotado.")


cliente_a = threading.Thread(target=comprar, args=("Cliente-A",))
cliente_b = threading.Thread(target=comprar, args=("Cliente-B",))

cliente_a.start()
cliente_b.start()

cliente_a.join()
cliente_b.join()

print(f"\nIngressos restantes no sistema: {ingressos_disponiveis}")
print("Esperado: no máximo 1 pessoa deveria conseguir comprar, "
      "e o estoque nunca deveria ficar negativo.")