import heapq
import sys


def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    idx = 0
    while idx < len(data):
        N = int(data[idx])
        M = int(data[idx + 1])
        C = int(data[idx + 2])
        K = int(data[idx + 3])
        idx += 4

        if N == 0 and M == 0 and C == 0 and K == 0:
            break

        # Lista de adjacência para o grafo geral
        grafo = [[] for _ in range(N)]
        # Matriz/Dicionário para consultar rápido o pedágio direto da rota
        pedagio_rota = {}

        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx + 1])
            p = int(data[idx + 2])
            idx += 3

            grafo[u].append((v, p))
            grafo[v].append((u, p))

            # Guarda o pedágio se fizer parte do caminho sequencial da rota
            if (u < C and v < C) and abs(u - v) == 1:
                pedagio_rota[(min(u, v), max(u, v))] = p

        # --- ALGORITMO DE DIJKSTRA MODIFICADO ---
        dist = [float("inf")] * N
        dist[K] = 0
        pq = [(0, K)]  # (custo, vertice)

        while pq:
            d_atual, u = heapq.heappop(pq)

            if d_atual > dist[u]:
                continue

            if u == C - 1:
                break  # Chegou no destino final da rota

            # REGRA 1: Se está FORA da rota, olha os vizinhos do grafo
            if u >= C:
                for vizinho, peso in grafo[u]:
                    if d_atual + peso < dist[vizinho]:
                        dist[vizinho] = d_atual + peso
                        heapq.heappush(pq, (dist[vizinho], vizinho))

            # REGRA 2: Se está DENTRO da rota, só pode ir para o próximo (u + 1)
            else:
                proximo = u + 1
                # Pega o custo do pedágio exato entre u e u+1
                peso = pedagio_rota[(u, proximo)]
                if d_atual + peso < dist[proximo]:
                    dist[proximo] = d_atual + peso
                    heapq.heappush(pq, (dist[proximo], proximo))

        print(dist[C - 1])


if __name__ == "__main__":
    solve()