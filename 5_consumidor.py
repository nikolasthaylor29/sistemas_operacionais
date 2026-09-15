"""
produtor_consumidor.py
Sistemas Operacionais - Aula 06 - Mutex e Semáforos

Exercício: Produtor/Consumidor com Semáforo

A thread consumidora não pode tentar pegar um item do buffer antes
que a thread produtora tenha colocado esse item ali - senão ela
tentaria consumir algo que ainda não existe.

Complete o código usando um threading.Semaphore para que a thread
CONSUMIDORA só prossiga DEPOIS que a thread PRODUTORA sinalizar que
o item está pronto.
"""

import threading
import time

buffer = []

# 1: crie um semáforo binário (valor inicial 0) chamado
#         "item_pronto". Começa em 0 porque, no início, ainda não
#         existe nenhum item pronto no buffer.
# item_pronto = threading.Semaphore(0)


def produtor():
    print("[Produtor] preparando o item...")
    time.sleep(1)
    buffer.append("dado")
    print("[Produtor] item colocado no buffer")

    # 2: sinalize que o item está pronto (libere o semáforo)


def consumidor():
    print("[Consumidor] aguardando item...")

    # 3: espere o sinal do produtor (adquira o semáforo) antes
    #         de tentar tirar o item do buffer

    item = buffer.pop()
    print("[Consumidor] consumiu:", item)


t1 = threading.Thread(target=produtor)
t2 = threading.Thread(target=consumidor)

# repare que o consumidor é iniciado PRIMEIRO de propósito: sem o
# semáforo, ele tentaria consumir um buffer ainda vazio
t2.start()
t1.start()

t1.join()
t2.join()