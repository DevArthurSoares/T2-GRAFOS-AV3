import heapq
import sys


def solve():
    
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
      
        if idx + 4 > len(input_data):
            break

        N = int(input_data[idx])
        M = int(input_data[idx + 1])
        C = int(input_data[idx + 2])
        K = int(input_data[idx + 3])
        idx += 4

        if N == 0 and M == 0 and C == 0 and K == 0:
            break

       
        grafo = [[] for _ in range(N)]

        for _ in range(M):
            u = int(input_data[idx])
            v = int(input_data[idx + 1])
            p = int(input_data[idx + 2])
            idx += 3

          
            if u < C and v < C:
                if u == v + 1:
                    grafo[v].append((u, p))
                elif v == u + 1:
                    grafo[u].append((v, p))
           
            elif u < C:
                grafo[v].append((u, p))
 
            elif v < C:
                grafo[u].append((v, p))
          
            else:
                grafo[u].append((v, p))
                grafo[v].append((u, p))

    
        dist = [float("inf")] * N
        dist[K] = 0
        pq = [(0, K)]

        while pq:
            d_atual, u = heapq.heappop(pq)

            if d_atual > dist[u]:
                continue

          
            if u == C - 1:
                break

            if u < C - 1:
                for vizinho, peso in grafo[u]:
                    if vizinho == u + 1:
                        if d_atual + peso < dist[vizinho]:
                            dist[vizinho] = d_atual + peso
                            heapq.heappush(pq, (dist[vizinho], vizinho))
               
                continue

       
            for vizinho, peso in grafo[u]:
                if d_atual + peso < dist[vizinho]:
                    dist[vizinho] = d_atual + peso
                    heapq.heappush(pq, (dist[vizinho], vizinho))

        print(dist[C - 1])


if _name_ == "_main_":
    solve()
