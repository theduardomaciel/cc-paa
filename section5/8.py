"""
QUESTÃO 8:
Desenvolva um algoritmo baseado em programação dinâmica para encontrar o caminho mais curto em um grafo acíclico direcionado (DAG).
"""

# 1. Caracterizar a sub-estrutura ótima:
# O caminho mais curto de um vértice de origem a um vértice de destino
# em um DAG pode ser encontrado usando a técnica de relaxação.
# A ideia é que, para cada aresta (u, v) do grafo, se o caminho mais curto até u é conhecido,
# podemos relaxar a aresta (u, v) e atualizar o caminho mais curto até v se encontrarmos um caminho mais curto.

# 2. Definir recursivamente o valor de uma solução ótima:
# dp[v] = comprimento do caminho mais curto até o vértice v
# dp[v] = min(dp[u] + peso(u, v)) para todas as arestas (u, v) do grafo
# dp[v] = 0, se v for o vértice de origem (caso base)
# dp[v] = ∞, se v não for alcançável a partir do vértice de origem (caso base)

""" 
função CaminhoMaisCurtoDag(G, origem):
    # Passo 1: Realizar ordenação topológica
    ordemTopologica = OrdenacaoTopologica(G)

    # Passo 2: Inicializar distâncias
    distancia = [infinito] * (número de vértices em G)
    distancia[origem] = 0

    3. Calcular o valor de uma solução ótima
    # Passo 3: Processar vértices na ordem topológica
    para cada vértice v em ordemTopologica:
        # Só processamos vértices alcançáveis
        se distancia[v] != infinito:
            para cada vizinho u adjacente a v:
                # Relaxamento da aresta (v, u)
                se distancia[u] > distancia[v] + peso(v, u):
                    distancia[u] = distancia[v] + peso(v, u)

    4. Construir uma solução ótima com as informações calculadas
    # Passo 4: Retornar as distâncias mínimas
    retornar distancia
"""


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for u, _ in graph[v]:
            if u not in visited:
                dfs(u)
        stack.append(v)

    for v in range(len(graph)):
        if v not in visited:
            dfs(v)

    return stack[::-1]  # Retorna a ordem reversa


def shortest_path_dag(graph, start):
    """
    graph: lista de adjacência do grafo, onde:
        - graph[v] é uma lista de tuplas (u, peso) representando arestas de v para u com peso
    start: vértice de origem
    """

    # Passo 1: Realizar ordenação topológica
    order = topological_sort(graph)

    # Passo 2: Inicializar distâncias
    distance = [float("inf")] * len(graph)
    distance[start] = 0

    # Passo 3: Processar vértices na ordem topológica
    for v in order:
        if distance[v] != float("inf"):
            for u, weight in graph[v]:
                if distance[u] > distance[v] + weight:
                    distance[u] = distance[v] + weight

    # Passo 4: Retornar as distâncias mínimas
    return distance


# Exemplo de uso
graph = [
    [(1, 2), (2, 3)],  # Vértice 0: arestas para 1 (peso 2) e 2 (peso 3)
    [(3, 6)],  # Vértice 1: aresta para 3 (peso 6)
    [(3, 4)],  # Vértice 2: aresta para 3 (peso 4)
    [],  # Vértice 3: sem arestas
]
start_vertex = 0

result = shortest_path_dag(graph, start_vertex)
print(f"Caminho mais curto a partir do vértice {start_vertex}: {result}")

""" 
RECONSTRUÇÃO DO CAMINHO:
Para reconstruir o caminho mais curto, podemos manter um array de predecessores.
Quando relaxamos uma aresta (v, u), se atualizamos a distância de u, também atualizamos o predecessor de u para v.
Assim, ao final do algoritmo, podemos reconstruir o caminho mais curto a partir do vértice de destino até o vértice de origem.
função CaminhoMaisCurtoDagComCaminho(G, origem, destino):
    # Passos 1-3 como antes
    ...

    # Adicionar array de predecessores
    predecessor = [null] * (número de vértices em G)

    para cada vértice v em ordemTopologica:
        se distancia[v] != infinito:
            para cada vizinho u adjacente a v:
                se distancia[u] > distancia[v] + peso(v, u):
                    distancia[u] = distancia[v] + peso(v, u)
                    predecessor[u] = v

    # Reconstruir o caminho
    caminho = []
    atual = destino
    enquanto atual != null:
        caminho.inserir_no_início(atual)
        atual = predecessor[atual]

    retornar distancia[destino], caminho
"""


def shortest_path_dag_with_path(graph, start, end):
    """
    graph: lista de adjacência do grafo, onde:
        - graph[v] é uma lista de tuplas (u, peso) representando arestas de v para u com peso
    start: vértice de origem
    end: vértice de destino
    """

    # Passo 1: Realizar ordenação topológica
    order = topological_sort(graph)

    # Passo 2: Inicializar distâncias e predecessores
    distance = [float("inf")] * len(graph)
    predecessor = [None] * len(graph)
    distance[start] = 0

    # Passo 3: Processar vértices na ordem topológica
    for v in order:
        if distance[v] != float("inf"):
            for u, weight in graph[v]:
                # Relaxamento da aresta (v, u)
                # Atualiza a distância e o predecessor se necessário
                if distance[u] > distance[v] + weight:
                    distance[u] = distance[v] + weight
                    predecessor[u] = v

    # Passo 4: Reconstruir o caminho
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()  # Inverte o caminho para a ordem correta

    return distance[end], path


# Exemplo de uso com reconstrução do caminho
graph = [
    [(1, 2), (2, 3)],  # Vértice 0: arestas para 1 (peso 2) e 2 (peso 3)
    [(3, 6)],  # Vértice 1: aresta para 3 (peso 6)
    [(3, 4)],  # Vértice 2: aresta para 3 (peso 4)
    [],  # Vértice 3: sem arestas
]
start_vertex = 0
end_vertex = 3

result, path = shortest_path_dag_with_path(graph, start_vertex, end_vertex)
print(
    f"Caminho mais curto a partir do vértice {start_vertex} até o vértice {end_vertex}: {result}, caminho: {path}"
)
