import threading
import time

ingressos_disponiveis = 1

def comprar_ingresso(nome_cliente):
    global ingressos_disponiveis
    
    # 1. CHECK (Verificação de condição)
    if ingressos_disponiveis > 0:
        print(f"[{nome_cliente}] Encontrou ingresso disponível! Processando pagamento...")
        time.sleep(0.02)  # Simula tempo de validação do cartão de crédito
        
        # 2. ACT (Ação de decremento)
        ingressos_disponiveis -= 1
        print(f"[{nome_cliente}] Compra confirmada com sucesso!")
    else:
        print(f"[{nome_cliente}] Esgotado! Não conseguiu comprar.")

t1 = threading.Thread(target=comprar_ingresso, args=("Cliente-A",))
t2 = threading.Thread(target=comprar_ingresso, args=("Cliente-B",))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"\nIngressos restantes no sistema: {ingressos_disponiveis}")