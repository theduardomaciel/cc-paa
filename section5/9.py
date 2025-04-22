"""
QUESTÃO 9:
Dado um DAG $$G(V, E)$$ e dois vértices $$s, t ∈ V$$, projete um algoritmo de programação dinâmica que encontre a quantidade de caminhos simples distintos entre $$s$$ e $$t$$ .
"""

""" 
Algoritmo:
1. Primeiro, realizamos uma ordenação topológica do DAG, garantindo que processamos os vértices na ordem correta
2. Inicializamos `numPaths[v] = 0` para todos os vértices v ∈ V
3. Definimos `numPaths[s] = 1` (existe um caminho do vértice inicial para ele mesmo)
4. Percorremos os vértices na ordem topológica:
    - Para cada vértice v, para cada aresta (v, u), adicionamos `numPaths[v]` a `numPaths[u]`
5. No final, `numPaths[t]` conterá o número de caminhos simples distintos de s a t
"""

# 1. Caracterizamos a sub-estrutura ótima:
# O número de caminhos simples distintos de um vértice s a um vértice t em um DAG pode ser encontrado usando a técnica de programação dinâmica.
# A ideia é que, para cada aresta (v, u) do grafo, se conhecemos o número de caminhos simples distintos até v,
# podemos atualizar o número de caminhos simples distintos até u somando o número de caminhos simples distintos até v.

# 2. Definimos recursivamente o valor de uma solução ótima:
# numPaths[v] = número de caminhos simples distintos até o vértice v
# numPaths[v] = sum(numPaths[u]) para todas as arestas (u, v) do grafo
# numPaths[v] = 0, se v for o vértice de origem (caso base)
# numPaths[v] = 1, se v for o vértice de destino (caso base)

""" 
CONTAGEM-CAMINHOS-DAG(G, s, t):
    topo_order ← ORDENAÇÃO-TOPOLÓGICA(G)

    // Inicialização
    para cada vértice v em G.V:
        numPaths[v] ← 0
    numPaths[s] ← 1

    // Computação dos valores
    para cada vértice v em topo_order:
        para cada aresta (v, u) em G.E:
            numPaths[u] ← numPaths[u] + numPaths[v]

    retornar numPaths[t]
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


def count_paths_dag(graph, s, t):
    # Passo 1: Realizar ordenação topológica
    topo_order = topological_sort(graph)

    # Passo 2: Inicializar contagem de caminhos
    numPaths = [0] * len(graph)
    numPaths[s] = 1  # Há um caminho do vértice inicial para ele mesmo

    # Passo 3: Processar vértices na ordem topológica
    for v in topo_order:
        for u, _ in graph[v]:
            numPaths[u] += numPaths[v]

    # Passo 4: Retornar o número de caminhos simples distintos de s a t
    return numPaths[t]


# Exemplo de uso:
graph = [
    [(1, 1), (2, 1)],  # Arestas de 0 para 1 e 2
    [(3, 1)],  # Aresta de 1 para 3
    [(3, 1)],  # Aresta de 2 para 3
    [],  # Vértice 3 não tem arestas saindo dele
]
start_vertex = 0
end_vertex = 3

num_paths = count_paths_dag(graph, start_vertex, end_vertex)
print(
    f"Número de caminhos simples distintos de {start_vertex} a {end_vertex}: {num_paths}"
)
# Saída esperada: Número de caminhos simples distintos de 0 a 3: 2
# Explicação: Existem dois caminhos simples distintos de 0 a 3: (0 -> 1 -> 3) e (0 -> 2 -> 3)
# Portanto, o resultado é 2.

""" 
    A solução funciona porque, em um DAG, o número de caminhos para um vértice u é 
    a soma dos números de caminhos para todos os seus predecessores diretos. 
    A ordenação topológica garante que quando processamos um vértice, 
    já calculamos os valores para todos os seus predecessores.
"""
