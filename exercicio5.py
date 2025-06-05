import time
from collections import deque

processos = [
    {"nome": "P1", "chegada": 0, "exec": 5, "tempo_restante": 5, "t_inicio": -1, "t_resp": 0},
    {"nome": "P2", "chegada": 1, "exec": 3, "tempo_restante": 3, "t_inicio": -1, "t_resp": 0},
    {"nome": "P3", "chegada": 2, "exec": 6, "tempo_restante": 6, "t_inicio": -1, "t_resp": 0}
     ]

def roundrobin(processos, quantum):
    p_restantes = deque()
    p_finalizados = deque()
    tempo_atual = 0
    reserva = processos
    ordem = ""
    for a in reserva:
            if a["chegada"] <= tempo_atual:
                p_restantes.append(a)
                reserva.remove(a)
        
    while p_restantes:
        p_ativo = p_restantes.popleft()
        if p_ativo["t_inicio"] == -1:
            p_ativo["t_inicio"] = tempo_atual
            p_ativo["t_resp"] = p_ativo["t_inicio"] - p_ativo["chegada"]
        if p_ativo["tempo_restante"] < quantum:
            burst = p_ativo["tempo_restante"]
            tempo_atual += burst
            p_ativo["tempo_restante"] = 0
            print(f"{p_ativo["nome"]} foi executado por {burst}t, rest: {p_ativo["tempo_restante"]}, burst: {burst} \n --> Processo finalizado em {tempo_atual}t")
            p_finalizados.append(p_ativo)
            time.sleep(0.3)
        else:        
            burst = quantum
            p_ativo["tempo_restante"] -= burst
            tempo_atual += burst
            print(f"{p_ativo["nome"]} foi executado por {quantum}t, rest: {p_ativo["tempo_restante"]}, burst: {burst}")
            if p_ativo["tempo_restante"] == 0:
                print(f" --> processo finalizado em {tempo_atual}t")
                p_finalizados.append(p_ativo)
            time.sleep(0.3)
        
        for a in reserva[:]:
            if a["chegada"] <= tempo_atual:
                p_restantes.append(a)
                reserva.remove(a)

        if p_ativo["tempo_restante"] > 0:
            p_restantes.append(p_ativo)
        if p_restantes:
            ordem += f"{p_ativo["nome"]} -> "
        else: 
            ordem += f"{p_ativo["nome"]}"
    print(ordem)
    tempo_medio_resposta = 0
    for p in p_finalizados:
        tempo_medio_resposta += p["t_inicio"] - p["chegada"]
    tempo_medio_resposta = tempo_medio_resposta/3
    print ("O tempo médio de resposta foi: {:.1f}".format(tempo_medio_resposta))
    final = input("imprimir os estados finais? [s/n]: ")
    if final == "s":
        for i in p_finalizados:
            print(i)


roundrobin(processos, 2)