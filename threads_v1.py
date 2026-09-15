import threading #importação da biblioteca de Threads
import time #biblioteca tempo

saldo = 100
#cadeado = threading.Lock()

def depositar():
    global saldo
    copia = saldo          # 1. Leu 100
    time.sleep(0.01)       # 2. SO interrompeu!
    saldo = copia + 50     # 3. Gravou 150

def sacar():
    global saldo
    copia = saldo          # 1. Leu 100
    time.sleep(0.01)       # 2. SO interrompeu!
    saldo = copia - 20     # 3. Gravou 80

def render_juros():
    global saldo
    copia = saldo
    time.sleep(0.01)
    saldo = copia + 10

# Criação das duas threads
t1 = threading.Thread(target=depositar)
t2 = threading.Thread(target=sacar)
t3 = threading.Thread(target=render_juros)

# Disparo das threads
t1.start()
t2.start()
t3.start()

# Aguarda ambas terminarem
t1.join()
t2.join()
t3.join()

print("=" * 45)
print("Saldo esperado (100 + 50 - 20): R$ 130")
print(f"Saldo real gravado no sistema:  R$ {saldo}")
print("=" * 45)