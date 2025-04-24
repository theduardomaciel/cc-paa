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


# Algoritmo:
# - Visita todos os vértices em profundidade
# - Quando um vértice termina (ou seja, não tem mais vizinhos a visitar), ele é adicionado ao fim de uma pilha
# - A pilha é invertida para obter a ordem topológica
# Ou seja, se estivéssemos usando uma lista, deveríamos inserir sempre no início
def topological_sort(graph):
    visited = set()
    stack = []

    # Função auxiliar para realizar DFS e preencher a pilha
    # com a ordem topológica
    def dfs(v):
        visited.add(v)

        # Visita todos os vizinhos do vértice v
        # (vizinhos são representados como tuplas (vizinhos, peso))
        for u, _ in graph[v]:
            if u not in visited:
                dfs(u)

        # Adiciona o vértice v à pilha após visitar todos os vizinhos
        stack.append(v)
        print("Pilha:", stack)

    # Loop para visitar todos os vértices do grafo
    # (mesmo que o grafo não seja conectado)
    for v in range(len(graph)):
        if v not in visited:
            dfs(v)

    return stack[::-1]  # Retorna a ordem reversa


# Função para calcular o comprimento do caminho mais longo em um DAG (grafo acíclico dirigido)
def dag_longest_path(graph):
    """
    graph: lista de adjacência, onde:
        - graph[i] é uma lista de tuplas (vizinhos, peso)
    """
    V = len(graph)

    # Passo 1: Realizar ordenação topológica
    order = topological_sort(graph)
    print("Ordem topológica:", order)

    # Passo 2: Inicializar array para armazenar comprimentos dos caminhos
    distance = [0] * V  # Inicializa com 0 para todos os vértices

    # Passo 3: Processar vértices na ordem topológica
    for u in order:
        for neighbor, weight in graph[u]:
            # Se a distância do vizinho for menor que a distância do vértice atual mais o peso da aresta
            if distance[neighbor] < distance[u] + weight:
                # Atualiza a distância do vizinho para o comprimento do caminho mais longo
                # até o vértice atual mais o peso da aresta
                distance[neighbor] = distance[u] + weight

    # Passo 4: Encontrar o valor máximo no array distance
    longest_path = max(distance)
    return longest_path


# Exemplo de uso
graph = [
    [(1, 3), (2, 6)],  # Vértice 0: arestas para 1 (peso 3) e 2 (peso 6)
    [(3, 2)],  # Vértice 1: aresta para 3 (peso 2)
    [(1, 4), (3, 1)],  # Vértice 2: arestas para 1 (peso 4) e 3 (peso 1)
    [],  # Vértice 3: sem arestas
]

longest_path_length = dag_longest_path(graph)
print("O comprimento do caminho mais longo no DAG é:", longest_path_length)
# Saída esperada: O comprimento do caminho mais longo no DAG é: 12
# 0 -> 2 -> 1 -> 3 = 6 + 4 + 2 = 12
# Outros caminhos são:
# 0 -> 2 -> 3 = 6 + 1 = 7
# 0 -> 1 -> 3 = 3 + 2 = 5
# Portanto, o caminho mais longo é 12.
