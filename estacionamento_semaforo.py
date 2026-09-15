import threading, time

vagas = threading.Semaphore(2)  # estacionamento com 1 vagas

def carro(id):
    with vagas: 
        print(f"Carro {id}: chegando")
        print(f"Carro {id}: ESTACIONOU")
        time.sleep(1)
        print(f"Carro {id}: saiu da vaga")

for i in range(4):
    threading.Thread(target=carro, args=(i,)).start()