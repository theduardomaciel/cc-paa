"""
QUESTÃO 3:
Apresente o pseudocódigo do algoritmo de Floyd-Warshall para o
problema dos caminhos mínimos entre todos os pares de vértices.
Apresente a recorrência para o cálculo da distância.
"""

# Floyd-Warshall: Algoritmo para encontrar o caminho mais curto entre todos os pares de vértices em um grafo ponderado.


def floyd_warshall(graph):
    """
    graph: matriz de adjacência (n x n), onde:
        - graph[i][j] é o peso da aresta de i para j
        - graph[i][j] = float('inf') se não houver aresta entre i e j
    """
    V = len(graph)
    # Cria a matriz de distâncias D, inicialmente igual ao grafo
    dist = [row[:] for row in graph]  # cópia profunda da matriz

    for k in range(V):  # vértice intermediário
        for i in range(V):  # vértice de origem
            for j in range(V):  # vértice de destino
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Exemplo de uso
INF = float("inf")
# fmt: off
graph = [
    [0,     3,      INF,    7],
    [8,     0,      2,      INF],
    [5,     INF,    0,      1],
    [2,     INF,    INF,    0]
]
# fmt: on

result = floyd_warshall(graph)

for row in result:
    print(row)

# Saída esperada:
""" 
[0, 3, 5, 6]
[5, 0, 2, 3]
[3, 6, 0, 1]
[2, 5, 7, 0]
# O caminho mais curto entre todos os pares de vértices é:
# 0 -> 1: 3
# 0 -> 2: 5
# 0 -> 3: 6
# 1 -> 0: 5
# 1 -> 2: 2
... e assim por diante para todos os pares de vértices.
"""
