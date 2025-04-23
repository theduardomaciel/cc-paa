"""
QUESTÃO 2:
O Rei Arthur espera $$n$$ cavaleiros para um jantar anual em Camelot.
Infelizmente, alguns dos cavaleiros brigam entre si, e Arthur sabe quem briga com quem.

Arthur quer sentar seus convidados ao redor de uma mesa para que dois cavaleiros briguentos não se sentem próximos um do outro.

Qual problema pode ser usado para modelar a tarefa do Rei Arthur?
"""

# Podemos modelar essa questão como um problema de Ciclo Hamiltoniano em um grafo complementar.
# Podemos estabelecer:
# - Cada cavaleiro é representado por um vértice no grafo
# - Uma aresta entre dois vértices indica que os dois cavaleiros correspondentes podem sentar-se adjacentes (ou seja, não brigam entre si)
# - O problema pede um arranjo circular onde cavaleiros adjacentes não brigam

""" 
    Para resolver isso, primeiro construímos um grafo onde cada vértice é um cavaleiro, e colocamos uma aresta entre dois cavaleiros se eles brigam. Este é o "grafo de conflitos".

    Em seguida, tomamos o complemento deste grafo, onde dois cavaleiros estão conectados se e somente se eles NÃO brigam. Neste grafo complementar, precisamos encontrar um ciclo hamiltoniano - um caminho que visita cada vértice exatamente uma vez e retorna ao início.

    Se um ciclo hamiltoniano existir no grafo complementar, então temos uma disposição válida para a mesa. Se não existir, não é possível organizar os cavaleiros da forma desejada.
"""

""" 
PSEUDO-CÓDIGO:
1. Criar um grafo G onde cada vértice representa um cavaleiro
2. Adicionar
    arestas entre os vértices que representam cavaleiros que brigam
3. Criar o grafo complementar G' onde as arestas representam cavaleiros que não brigam
4. Verificar se existe um ciclo hamiltoniano em G'
5. Se existir, retornar "É possível organizar os cavaleiros na mesa"
6. Se não existir, retornar "Não é possível organizar os cavaleiros na mesa"
7. Fim

procedure organizar_cavaleiros(n, brigas)
    grafo G ← criar_grafo(n)
    for (cavaleiro1, cavaleiro2) in brigas:
        adicionar_aresta(G, cavaleiro1, cavaleiro2)
    
    grafo G' ← complementar(G)
    
    if existe_ciclo_hamiltoniano(G') then
        return "É possível organizar os cavaleiros na mesa"
    else
        return "Não é possível organizar os cavaleiros na mesa"
"""


def create_graph(n):
    # Cria um grafo com n vértices
    return {i: set() for i in range(n)}


def add_edge(graph, v1, v2):
    # Adiciona uma aresta entre v1 e v2 no grafo
    graph[v1].add(v2)
    graph[v2].add(v1)


def complement(graph):
    # Cria o grafo complementar
    n = len(graph)
    complement_graph = create_graph(n)

    for v1 in graph:
        for v2 in range(n):
            if v1 != v2 and v2 not in graph[v1]:
                add_edge(complement_graph, v1, v2)

    return complement_graph


def has_hamiltonian_cycle(graph):
    # Verifica se existe um ciclo hamiltoniano no grafo
    n = len(graph)
    visited = [False] * n

    def dfs(v, count, start):
        if count == n and start in graph[v]:
            return True

        visited[v] = True

        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, count + 1, start):
                    return True

        visited[v] = False
        return False

    for i in range(n):
        if dfs(i, 1, i):
            return True

    return False


# Teste da função
if __name__ == "__main__":
    n = 5  # Número de cavaleiros
    brigas = [(0, 1), (0, 3), (1, 2), (2, 3)]  # Lista de pares de cavaleiros que brigam

    grafo = create_graph(n)
    for cavaleiro1, cavaleiro2 in brigas:
        add_edge(grafo, cavaleiro1, cavaleiro2)

    grafo_complementar = complement(grafo)

    if has_hamiltonian_cycle(grafo_complementar):
        print("É possível organizar os cavaleiros na mesa")
    else:
        print("Não é possível organizar os cavaleiros na mesa")
