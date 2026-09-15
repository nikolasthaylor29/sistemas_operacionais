import threading

lock = threading.Lock()

def trabalhador(id):
    print(f"Thread {id}: entrando na região crítica")
    print(f"Thread {id}: saindo da região crítica")

threads = [threading.Thread(target=trabalhador, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()