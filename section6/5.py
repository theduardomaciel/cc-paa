"""
QUESTÃO 5:
O problema da coloração em grafos é geralmente declarado como o problema da coloração do vértice: atribua o menor número de cores aos vértices de um dado grafo de forma que não haja dois vértices adjacentes da mesma cor.

Considere agora o problema da coloração das arestas: atribua o menor número possível de cores às arestas de um determinado grafo, de modo que duas arestas com o mesmo vértices não tenham a mesma cor.

Explique como o problema de coloração de arestas pode ser reduzido a um problema de coloração de vértices.
"""

# A ideia central é transformar o grafo original G em um novo grafo L(G), onde:
# 1. Cada aresta do grafo original G se torna um vértice no grafo L(G) (grafo de linha)
# 2. Dois vértices em L(G) são conectados por uma aresta se as arestas correspondentes em G compartilham um vértice em comum

# Passo a passo da redução:
# 1. Para um grafo G = (V, E), construímos o grafo L(G) = (V', E')
#     - V' = E (cada vértice em L(G) representa uma aresta de G)
#     - E' = {(e1, e2) | e1, e2 ∈ E e e1, e2 compartilham um vértice em G}
# 2. Uma coloração válida de vértices em L(G) corresponde diretamente a uma coloração válida de arestas em G
# 3. O número cromático de L(G) (mínimo de cores para colorir os vértices) é igual ao índice cromático de G (mínimo de cores para colorir as arestas)

# Exemplo de uso
# G = { A, B ,C }, com arestas {(A, B), (B, C), (A, C)}

from collections import defaultdict

# Grafo original G
# Representado como lista de arestas
G_edges = [("A", "B"), ("B", "C"), ("A", "C")]


# Construir o grafo de linha L(G)
def build_line_graph(edges):
    line_graph = defaultdict(list)

    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            e1, e2 = edges[i], edges[j]
            # Se compartilham um vértice, conectamos e1 e e2 em L(G)
            if set(e1) & set(e2):
                line_graph[e1].append(e2)
                line_graph[e2].append(e1)

    return line_graph


# Algoritmo guloso de coloração de vértices
def greedy_vertex_coloring(graph):
    color = {}
    for vertex in sorted(
        graph, key=lambda x: len(graph[x]), reverse=True
    ):  # ordena por grau
        neighbor_colors = {
            color[neighbor] for neighbor in graph[vertex] if neighbor in color
        }
        for c in range(len(graph) + 1):
            if c not in neighbor_colors:
                color[vertex] = c
                break
    return color


# Executando o processo
line_graph = build_line_graph(G_edges)
coloring = greedy_vertex_coloring(line_graph)

# Mostrar coloração das arestas
print("Coloração de arestas (via grafo de linha):")
for edge in G_edges:
    print(f"Aresta {edge} -> Cor {coloring[edge]}")

# ✅ Saída esperada para o exemplo:
""" 
Coloração de arestas (via grafo de linha):
Aresta ('A', 'B') -> Cor 0
Aresta ('B', 'C') -> Cor 1
Aresta ('A', 'C') -> Cor 2
"""
# Neste caso, usamos 3 cores, que é o índice cromático desse triângulo (grafo completo K₃).
# Esse é o número mínimo possível nesse caso.

# Resumindo:
# Cada aresta de G virou um vértice de L(G)
# Se duas arestas compartilham um vértice, seus vértices em L(G) estão conectados
# Colorimos os vértices de L(G) de modo que adjacentes tenham cores diferentes
# Isso garante que as arestas do grafo original que tocam o mesmo vértice tenham cores diferentes
