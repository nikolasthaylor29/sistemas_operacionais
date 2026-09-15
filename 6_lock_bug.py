import threading

contador = 0

def incrementar():
    global contador
    lock = threading.Lock()
    for _ in range(100000):
        with lock:
            contador += 1

t1 = threading.Thread(target=incrementar)
t2 = threading.Thread(target=incrementar)
t1.start(); t2.start()
t1.join(); t2.join()

print(contador)  