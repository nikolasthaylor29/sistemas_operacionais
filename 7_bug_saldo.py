import threading, time

saldo = 100
lock = threading.Lock()

def sacar(valor):
    global saldo
    if saldo >= valor:          # <-- fora do lock
        time.sleep(0.01)
        with lock:
            saldo -= valor      # só a escrita está protegida

t1 = threading.Thread(target=sacar, args=(80,))
t2 = threading.Thread(target=sacar, args=(80,))
t1.start(); t2.start()
t1.join(); t2.join()

print(saldo)  # com saldo=100, nunca deveriam sair os dois saques de 80