import math

""" 
QUESTÃO 1:
Inteiros positivos são arranjados em um triângulo equilátero com n números em sua base, como o mostrado na figura abaixo para $$n = 4.$$ 

# Exemplo:
#     2
#    5 4
#   3 4 7
#  1 6 9 6
# A soma mínima do caminho é 2 + 4 + 4 + 1 = 11, e o caminho é [2, 4, 4, 1].

O problema é encontrar a menor soma em uma descida do ápice do triângulo até sua base por meio de uma sequência de números adjacentes (mostrados na figura pelos círculos). 

Projete um algoritmo de programação dinâmica para este problema.
"""

# Precisamos encontrar o caminho de soma mínima do topo até a base do triângulo.
# Só podemos descer para números adjacentes na linha abaixo.
# Em cada nível i, um número na posição j pode descer para o número na posição j ou j+1 na linha i+1.
# Então, basicamente, i = linha, j = coluna.
# Para resolver isso, podemos usar programação dinâmica.

# 1. Caracterizar a sub-estrutura ótima:
# A soma mínima do caminho até a linha i e coluna j é igual à soma mínima do caminho até
# a linha i-1 e coluna j ou coluna j-1, mais o valor na posição (i, j).

# 2. Definir recursivamente o valor de uma solução ótima
# A soma mínima do caminho até a linha i e coluna j é:
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

""" 
função MinimumPathSum(triangle):
    n ← número de níveis do triângulo
    dp ← matriz n × n inicializada com infinito

    dp[0][0] ← triangle[0][0]  // Ápice do triângulo

    # 3. Calcular o valor de uma solução ótima
    Para i de 1 até n-1:
        Para j de 0 até i:
            // Verificar elemento à esquerda superior (se existir)
            se j > 0:
                dp[i][j] ← min(dp[i][j], dp[i-1][j-1] + triangle[i][j])

            // Verificar elemento à direita superior (se existir)
            se j < i:
                dp[i][j] ← min(dp[i][j], dp[i-1][j] + triangle[i][j])

    // 4. Construir uma solução ótima com as informações calculadas
    // A última linha contém os menores caminhos até a base do triângulo
    resultado ← infinito
    Para j de 0 até n-1:
        resultado ← min(resultado, dp[n-1][j])

    Retornar resultado
"""


def minimum_path_sum(triangle):
    n = len(triangle)
    dp = [[math.inf] * n for _ in range(n)]  # Matriz n x n inicializada com infinito

    dp[0][0] = triangle[0][0]  # O ápice do triângulo é a primeira célula

    # Percorremos as linhas do triângulo (começando da segunda linha - índice 1)
    # A primeira linha já está preenchida (o ápice - triangle[0][0])
    for i in range(1, n):
        # Para cada linha, percorremos as colunas
        # A linha i tem i + 1 elementos (de 0 a i)
        for j in range(i + 1):
            # Verificamos o elemento à esquerda superior (se existir)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])
            # Verificamos o elemento à direita superior (se existir)
            if j < i:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + triangle[i][j])

    # Encontrar o menor valor na última linha
    # A última linha contém os menores caminhos até a base do triângulo
    result = math.inf
    for j in range(n):
        result = min(result, dp[n - 1][j])

    return result


def minimum_path_sum_with_path(triangle):
    n = len(triangle)
    dp = [[float("inf")] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]  # Guarda de onde veio o caminho

    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i):
            # Da esquerda superior
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                parent[i][j] = (i - 1, j - 1)

            # Da direita superior
            if j < i:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
                parent[i][j] = (i - 1, j)

    # Achar a posição do menor valor na base
    min_val = float("inf")
    min_index = -1
    for j in range(n):
        if dp[n - 1][j] < min_val:
            min_val = dp[n - 1][j]
            min_index = j

    # Reconstruir caminho
    path = []
    i, j = n - 1, min_index
    while i is not None and j is not None:
        path.append(triangle[i][j])
        if parent[i][j] is None:
            break
        i, j = parent[i][j]

    path.reverse()  # Caminho do topo até a base

    return min_val, path


# Exemplo de uso
# fmt: off
triangle = [[2], 
            [5, 4], 
            [3, 4, 7], 
            [1, 6, 9, 6]]
# fmt: on
result = minimum_path_sum(triangle)

print(f"A soma mínima do caminho é: {result}")

result_with_path = minimum_path_sum_with_path(triangle)
print(f"A soma mínima do caminho é: {result_with_path[0]}")
print(f"O caminho é: {result_with_path[1]}")
