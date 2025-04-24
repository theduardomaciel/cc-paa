"""
QUESTÃO 9:
PROBLEMA DE FREQUÊNCIA.

Quando o raio de duas antenas se interceptam, haverá interferências caso as antenas utilizem a mesma frequência.
Estabeleça frequências para a antenas de modo que não haja interferência e que o número de frequências utilizadas seja minimizada.

Transforme-o em um problema de grafos.
"""

""" 
Podemos modelar o problema da seguinte forma:
1. Cada antena é representada por um vértice no grafo.
2. Duas antenas (vértices) serão conectadas por uma aresta se seus raios de cobertura se interceptam.
3. O problema de atribuir frequências às antenas sem interferência é equivalente a colorir o grafo, onde cada cor representa uma frequência diferente.
4. A restrição de que duas antenas não podem ter a mesma frequência se traduz na condição de que dois vértices adjacentes não podem ter a mesma cor.

Assim, nosso problema se torna um problema de coloração de grafos, onde o objetivo é minimizar o número de cores (frequências) usadas para colorir o grafo, respeitando a condição de que vértices adjacentes não podem ter a mesma cor.

Obs.: O problema de coloração de grafos é NP-difícil, o que significa que não existe um algoritmo eficiente conhecido para resolvê-lo em todos os casos
"""

# Abaixo está um exemplo de implementação de um algoritmo guloso para coloração de grafos.
# Este algoritmo não garante a solução ótima, mas é uma aproximação razoável


def greedy_coloring(graph):
    # Inicializa a lista de cores para cada vértice
    colors = [-1] * len(graph)

    # A primeira cor é atribuída ao primeiro vértice
    colors[0] = 0

    # Atribui cores aos outros vértices
    for u in range(1, len(graph)):
        # Cria um conjunto de cores adjacentes
        adjacent_colors = set()
        for v in graph[u]:
            if colors[v] != -1:
                adjacent_colors.add(colors[v])

        # Atribui a menor cor disponível ao vértice u
        color = 0
        while color in adjacent_colors:
            color += 1
        colors[u] = color

    return colors


# Teste do algoritmo de coloração gulosa
if __name__ == "__main__":
    # Grafo de exemplo (representado como uma lista de adjacência)
    graph = [
        [1, 2],  # Vértice 0 está conectado a 1 e 2
        [0, 2, 3],  # Vértice 1 está conectado a 0, 2 e 3
        [0, 1],  # Vértice 2 está conectado a 0 e 1
        [1],  # Vértice 3 está conectado a 1
    ]

    colors = greedy_coloring(graph)
    print("Cores atribuídas:", colors)
    # Saída esperada: Cores atribuídas: [0, 1, 2, 0]

    # Outro exemplo
    graph = [
        [1, 3, 4],  # Vértice 0 está conectado a 1, 3 e 4
        [0, 2],  # Vértice 1 está conectado a 0 e 2
        [1, 4],  # Vértice 2 está conectado a 1 e 4
        [0],  # Vértice 3 está conectado a 0
        [0, 2],  # Vértice 4 está conectado a 0 e 2
    ]

    colors = greedy_coloring(graph)
    print("Cores atribuídas:", colors)
    # Saída esperada: Cores atribuídas: [0, 1, 0, 1]
