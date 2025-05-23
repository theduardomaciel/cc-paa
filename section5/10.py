"""
QUESTÃO 10:
Mostre uma algoritmo de programação dinâmica para o problema do CAMINHO MÁXIMO entre dois vértices $$s$$ e $$t$$ (caminho simples).

Qual a complexidade do algoritmo (tempo e memória)?
"""

# Como estamos trabalhando com um DAG (direcionado acíclico), podemos resolver da seguinte forma:
# 1. Realizar uma ordenação topológica dos vértices
# 2. Inicializar as distâncias máximas
# 3. Relaxar as arestas na ordem topológica
# 4. Retornar a distância máxima do vértice inicial para o vértice final

""" 
procedure LONGEST_PATH_DAG(G, s, t)
     topo_order ← TOPOLOGICAL_SORT(G)

     # Inicializar distâncias máximas
     for cada v em V(G) do
         max_dist[v] ← -∞
         pred[v] ← nulo
     end for

     # Distância do vértice inicial para ele mesmo é 0
     max_dist[s] ← 0

     # Processar vértices na ordem topológica
     for cada u em topo_order do
        # Se a distância máxima para o vértice u for -∞, não há necessidade de processá-lo
        # (ou seja, não há caminho para u a partir de s)
        if max_dist[u] = -∞ then
            continue
        end if

        # Relaxar as arestas
        for cada (v, peso) em Arestas de u do
            if max_dist[v] < max_dist[u] + peso then
                max_dist[v] ← max_dist[u] + peso
                pred[v] ← u
            end if
        end for
     end for

     caminho ← []
     atual ← t

    # Reconstruir o caminho máximo
    while atual ≠ nulo do
        caminho ← caminho ∪ {atual}
        atual ← pred[atual]
    end while

    # Inverter o caminho para a ordem correta
    inverter(caminho)

    # Se a distância máxima para o vértice t for -∞, não há caminho de s a t
    # (ou seja, não há caminho simples entre s e t)
    if max_dist[t] = -∞ then
        return caminho, -1
    else
        return caminho, max_dist[t]
    end if
end procedure
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


def longest_path_dag(graph, s, t):
    # Passo 1: Realizar ordenação topológica
    topo_order = topological_sort(graph)

    # Passo 2: Inicializar distâncias máximas
    max_dist = [-float("inf")] * len(graph)
    # ou max_dist = {v: float('-inf') for v in grafo}

    max_dist[s] = 0  # Distância do vértice inicial para ele mesmo é 0

    pred = [None] * len(graph)  # Para armazenar o predecessor de cada vértice
    # ou {v: None for v in grafo}

    # Passo 3: Processar vértices na ordem topológica
    for u in topo_order:
        # Se a distância máxima para o vértice u for -inf, não há necessidade de processá-lo
        if max_dist[u] == -float("inf"):
            continue

        # Relaxar as arestas
        for v, weight in graph[u]:
            # Se a distância máxima para o vértice v pode ser aumentada
            # (ou seja, se o caminho u -> v é maior que o caminho atual para v)
            if max_dist[v] < max_dist[u] + weight:
                max_dist[v] = max_dist[u] + weight  # Atualiza a distância máxima
                pred[v] = u  # Atualiza o predecessor

    # Passo 4: Reconstruir o caminho máximo
    caminho = []
    current = t
    while current is not None:
        caminho.append(current)
        current = pred[current]

    caminho.reverse()  # Inverte o caminho para a ordem correta

    # Retorna o caminho máximo e a distância máxima
    return caminho, max_dist[t] if max_dist[t] != -float("inf") else -1


# Exemplo de uso:
graph = [
    [(1, 2), (2, 3)],  # Vértice 0 tem arestas para 1 e 2 com pesos 2 e 3
    [(3, 6)],  # Vértice 1 tem aresta para 3 com peso 6
    [(3, 4)],  # Vértice 2 tem aresta para 3 com peso 4
    [],  # Vértice 3 não tem arestas
]
start_vertex = 0
end_vertex = 3

caminho, max_dist = longest_path_dag(graph, start_vertex, end_vertex)
print(
    f"Caminho máximo de {start_vertex} a {end_vertex}: {caminho}, Distância: {max_dist}"
)
# Saída esperada: Caminho máximo de 0 a 3: [0, 1, 3], Distância: 8
