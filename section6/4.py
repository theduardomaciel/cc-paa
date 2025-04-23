"""
QUESTÃO 4:
Várias famílias saem para jantar juntas.
Para aumentar sua interação social, eles gostariam de sentar-se à mesa, de modo que dois membros da mesma família não estivessem na mesma mesa.

Mostre como encontrar uma disposição dos assentos que atenda a esse objetivo (ou prove que não existe tal disposição) usando o problema de fluxo máximo.
Suponha que o jantar tenha $$p$$ famílias e que a $$i$$-ésima família tenha $$a_i$$ membros.
Suponha que $$q$$ mesas são disponíveis e que a mesa $$j$$-ésima mesa possui capacidade $$b_j$$.
"""

# Podemos resolver esse problema transformando-o em um problema de fluxo máximo em um grafo bipartido.
# O grafo pode ser construído da seguinte maneira:
# - Crie um vértice fonte $$S$$ e um vértice sumidouro $$T$$.
# - Para cada família $$i$$, crie um vértice $$F_i$$ (total de $$p$$ vértices)
# - Para cada mesa $$j$$, crie um vértice $$M_j$$  (total de $$q$$ vértices)
# - Adicione arestas direcionadas com as seguintes capacidades:
#   - De $$S$$ para cada vértice de família $$F_i$$: capacidade = $$a_i$$ (número de membros da família).
#   - De cada vértice de família $$F_i$$ para cada mesa $$M_j$$: capacidade = 1 (no máximo, um membro da família pode sentar-se em uma mesa).
#   - De cada mesa $$M_j$$ para o vértice sumidouro $$T$$: capacidade = $$b_j$$ (capacidade da mesa).

# Assim, podemos interpretar o fluxo que sai do vértice fonte $$S$$ como o número total de membros das famílias que estão sentados à mesa, e o fluxo que entra no vértice sumidouro $$T$$ como o número total de lugares disponíveis nas mesas.
# Se o fluxo máximo for igual à soma das capacidades das mesas, então é possível acomodar todos os membros das famílias sem que dois membros da mesma família se sentem na mesma mesa.

# Vamos implementar isso em Python.
# Para simplificar, usaremos o algoritmo de Ford-Fulkerson para encontrar o fluxo máximo em um grafo.
# Também poderíamos utilizar o algoritmo de Edmonds-Karp.

# Para isso, precisamos de uma representação do grafo e de funções para adicionar arestas e encontrar o fluxo máximo.
from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = defaultdict(
            list
        )  # Grafo representado como um dicionário de listas
        self.source = 0  # Vértice fonte
        self.sink = 1  # Vértice sumidouro

    def add_edge(self, u, v, w):
        # Adiciona uma aresta ao grafo com capacidade w
        self.graph[u].append((v, w))
        self.graph[v].append((u, 0))  # Adiciona a aresta reversa com capacidade 0

    def bfs(self, parent):
        visited = [False] * self.V
        queue = deque([self.source])
        visited[self.source] = True

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u]:
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == self.sink:
                        return True

        return False

    def ford_fulkerson(self):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(parent):
            path_flow = float("Inf")
            s = self.sink

            while s != self.source:
                for v, capacity in self.graph[parent[s]]:
                    if v == s:
                        path_flow = min(path_flow, capacity)
                s = parent[s]

            max_flow += path_flow
            v = self.sink

            while v != self.source:
                u = parent[v]
                for i, (vertex, capacity) in enumerate(self.graph[u]):
                    if vertex == v:
                        self.graph[u][i] = (vertex, capacity - path_flow)
                for i, (vertex, capacity) in enumerate(self.graph[v]):
                    if vertex == u:
                        self.graph[v][i] = (vertex, capacity + path_flow)
                v = parent[v]

        return max_flow

    def edmonds_karp(self):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(parent):
            path_flow = float("Inf")
            s = self.sink

            while s != self.source:
                for v, capacity in self.graph[parent[s]]:
                    if v == s:
                        path_flow = min(path_flow, capacity)
                s = parent[s]

            max_flow += path_flow
            v = self.sink

            while v != self.source:
                u = parent[v]
                for i, (vertex, capacity) in enumerate(self.graph[u]):
                    if vertex == v:
                        self.graph[u][i] = (vertex, capacity - path_flow)
                for i, (vertex, capacity) in enumerate(self.graph[v]):
                    if vertex == u:
                        self.graph[v][i] = (vertex, capacity + path_flow)
                v = parent[v]

        return max_flow


# Função para criar o grafo a partir das famílias e mesas
def create_graph(families, tables):
    total_members = sum(families)  # Total de membros das famílias
    total_capacity = sum(tables)  # Total de capacidade das mesas

    # Criar o grafo com o número de vértices igual ao número de famílias + número de mesas + 2 (fonte e sumidouro)
    g = Graph(len(families) + len(tables) + 2)

    # Adicionar arestas da fonte para as famílias
    for i, members in enumerate(families):
        g.add_edge(g.source, i + 2, members)  # Aresta da fonte para a família i

    # Adicionar arestas das mesas para o sumidouro
    for j, capacity in enumerate(tables):
        # Aresta da mesa j para o sumidouro
        g.add_edge(j + len(families) + 2, g.sink, capacity)

    # Adicionar arestas entre as famílias e as mesas
    for i in range(len(families)):
        for j in range(len(tables)):
            # Aresta da família i para a mesa j
            g.add_edge(i + 2, j + len(families) + 2, 1)

    return g, total_members, total_capacity


# Função principal para verificar se é possível acomodar todos os membros das famílias
def can_accommodate(families, tables):
    g, total_members, total_capacity = create_graph(families, tables)

    # Verifica se o fluxo máximo é igual à soma das capacidades das mesas
    max_flow = g.ford_fulkerson()

    print(
        f"Fluxo máximo: {max_flow}, Total de membros: {total_members}, Total de capacidade: {total_capacity}"
    )

    # max_flow = total_capacity -> verifica se a regra de que dois membros da mesma família não podem sentar-se na mesma mesa é respeitada
    # max_flow == total_members -> verifica se todos os membros das famílias foram acomodados
    if max_flow == total_capacity and max_flow == total_members:
        return "É possível acomodar todos os membros das famílias"
    else:
        return "Não é possível acomodar todos os membros das famílias"


# Teste da função
if __name__ == "__main__":
    families = [3, 2, 4]  # Número de membros de cada família
    tables = [4, 3]  # Capacidade de cada mesa

    result = can_accommodate(families, tables)
    print(result)  # Saída: "Não é possível acomodar todos os membros das famílias"

    # Teste com outro exemplo
    families = [2, 2, 3]  # Número de membros de cada família
    tables = [2, 3, 2]  # Capacidade de cada mesa
    result = can_accommodate(families, tables)
    print(result)  # Saída: "É possível acomodar todos os membros das famílias"
