"""
QUESTÃO 4:
Projete um algoritmo eficiente para encontrar o comprimento do caminho mais longo em um DAG.

(Este problema é importante como um protótipo de muitos outros aplicativos de programação dinâmica, pois determina o tempo mínimo necessário para concluir um projeto que compreende tarefas de precedência restrita.)
"""

""" 
função CaminhoMaisLongoDag(G):
    # Passo 1: Realizar ordenação topológica
    ordemTopologica = OrdenacaoTopologica(G)

    # Passo 2: Inicializar array para armazenar comprimentos dos caminhos
    distancia = [0] * (número de vértices em G)

    # Passo 3: Processar vértices na ordem topológica
    para cada vértice v em ordemTopologica:
        para cada vizinho u adjacente a v:
            se distancia[u] < distancia[v] + peso(v, u):
                distancia[u] = distancia[v] + peso(v, u)

    # Passo 4: Encontrar o valor máximo no array distancia
    caminhoMaisLongo = max(distancia)

    retornar caminhoMaisLongo

"""


# Função auxiliar para realizar a ordenação topológica
# Basicamente, uma DFS (busca em profundidade) que
# armazena os vértices na pilha após visitar todos os seus vizinhos
def topological_sort_util(v, visited, stack):
    visited[v] = True
    for neighbor, _ in graph[v]:
        if not visited[neighbor]:
            topological_sort_util(neighbor, visited, stack)
    stack.append(v)


# Função para calcular o comprimento do caminho mais longo em um DAG (grafo acíclico dirigido)
def dag_longest_path(graph):
    """
    graph: lista de adjacência, onde:
        - graph[i] é uma lista de tuplas (vizinhos, peso)
    """
    V = len(graph)

    # Passo 1: Realizar ordenação topológica
    visited = [False] * V
    stack = []

    for i in range(V):
        if not visited[i]:
            topological_sort_util(i, visited, stack)

    # Passo 2: Inicializar array para armazenar comprimentos dos caminhos
    distance = [float("-inf")] * V
    distance[stack[-1]] = 0  # O comprimento do caminho para o último vértice é 0

    # Passo 3: Processar vértices na ordem topológica
    while stack:
        u = stack.pop()
        if distance[u] != float("-inf"):
            for neighbor, weight in graph[u]:
                if distance[neighbor] < distance[u] + weight:
                    distance[neighbor] = distance[u] + weight

    # Passo 4: Encontrar o valor máximo no array distance
    longest_path = max(distance)

    return (
        longest_path if longest_path != float("-inf") else 0
    )  # Retorna 0 se não houver caminho


# Exemplo de uso
graph = [
    [(1, 3), (2, 6)],  # Vértice 0: arestas para 1 (peso 3) e 2 (peso 6)
    [(3, 2)],  # Vértice 1: aresta para 3 (peso 2)
    [(3, 1)],  # Vértice 2: aresta para 3 (peso 1)
    [],  # Vértice 3: sem arestas
]

longest_path_length = dag_longest_path(graph)
print("O comprimento do caminho mais longo no DAG é:", longest_path_length)
# Saída esperada: O comprimento do caminho mais longo no DAG é: 8
