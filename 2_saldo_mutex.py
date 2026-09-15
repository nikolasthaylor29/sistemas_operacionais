"""
threadS_v1.py
Sistemas Operacionais - Aula 06 - Mutex e Semáforos

Simulação de uma conta bancária sofrendo transações concorrentes:
PIX (depósito), débito automático (saque) e rendimento (juros).

Ainda SEM nenhum mecanismo de sincronização - o objetivo é observar
a disputa pelo mesmo recurso (a variável "saldo") na memória RAM.

Saldo esperado ao final:
    100 (inicial) + 50 (depósito) - 20 (saque) + 10 (juros) = R$ 140
"""

import threading
import time

saldo = 100 #Declarando a variavel saldo

def depositar(): #Definição da função de depósito
    global saldo
    copia = saldo
    time.sleep(0.01)
    saldo = copia + 50


def sacar(): #Função de saque
    global saldo
    copia = saldo
    time.sleep(0.01)
    saldo = copia - 20

t1 = threading.Thread(target=depositar)
t2 = threading.Thread(target=sacar)

t1.start()
t2.start()

t1.join().join()

print(f"Saldo final:    R$ {saldo}")
print(f"Saldo esperado: R$ 130")
if saldo == 140:
    print("OK! (mas rode várias vezes - com 3 threads concorrendo, "
          "o resultado nem sempre bate)")
else:
    print("Deu ruim! Condição de corrida detectada.")