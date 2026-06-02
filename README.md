Resolução de Problemas com Grafos - T2 AV3

Prof. Ricardo Carubbi

Grupo: Aaron Magno, Arthur Soares, Davi Dias
O Problema: Route Change (UVa 11833)
Linguagem: Python
Resolução do problema 11833 do UVa Online Judge. O objetivo é calcular o menor custo de pedágio da cidade K até o destino final C−1.
Restrição de Estado

    Fora da rota (≥C): O veículo pode andar livremente por qualquer estrada.

    Dentro da rota (<C): Ao entrar na rota de serviço, o veículo perde a liberdade de escolha e é obrigado a seguir a sequência exata de cidades (u→u+1) até o final.

Solução e Modelagem

Implementamos o algoritmo de Dijkstra com modificação de estado:

    Estrutura Própria: Modelamos o grafo usando classes nativas para Grafo e Aresta, sem estruturas genéricas.

    MinHeap Autoral: Desenvolvemos a fila de prioridade do zero (heap binário), sem importar a biblioteca heapq.

    Relaxamento Customizado: Se o vértice atual pertence à rota, o código ignora vizinhos externos e força o caminho para a próxima cidade da sequência.

Complexidade

    Tempo: O((V+E)logV)

    Espaço: O(V+E)
