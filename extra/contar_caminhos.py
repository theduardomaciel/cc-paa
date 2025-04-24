"""
Vamos definir DP[i][j] como o número de caminhos da posição [0,0] até a posição [i,j].
Se houver um obstáculo em [i,j], então DP[i][j] = 0 (não podemos chegar lá).
Caso contrário:
- Para a posição inicial [0,0], se não há obstáculo, DP[0][0] = 1
- Para a primeira linha (i=0), DP[0][j] = DP[0][j-1] se não há obstáculo em [0,j]
- Para a primeira coluna (j=0), DP[i][0] = DP[i-1][0] se não há obstáculo em [i,0]
- Para qualquer outra célula, DP[i][j] = DP[i-1][j] + DP[i][j-1] se não há obstáculo em [i,j]

A lógica básica é: o número de maneiras de chegar a uma célula é a soma do número de maneiras de chegar à célula acima e à célula à esquerda
"""

"""
1: procedure CONTAR_CAMINHOS(B)
2:   n ← número de linhas de B
3:   m ← número de colunas de B
4:
5:   if B[0][0] = true or B[n-1][m-1] = true then
6:      return 0  // Se o início ou fim tem obstáculo, não há caminho
7:   end if
8:
9:   dp ← matriz n × m inicializada com zeros
10:  dp[0][0] ← 1  // Existe um caminho para a posição inicial
11:
12:  // Preenche a primeira coluna
13:  for i ← 1 to n-1 do
14:     if B[i][0] = false then
15:        dp[i][0] ← dp[i-1][0]
16:     end if
17:  end for
18:
19:  // Preenche a primeira linha
20:  for j ← 1 to m-1 do
21:     if B[0][j] = false then
22:        dp[0][j] ← dp[0][j-1]
23:     end if
24:  end for
25:
26:  // Preenche o resto da matriz
27:  for i ← 1 to n-1 do
28:     for j ← 1 to m-1 do
29:        if B[i][j] = false then
30:           dp[i][j] ← dp[i-1][j] + dp[i][j-1]
31:        end if
32:     end for
33:  end for
34:
35:  return dp[n-1][m-1]
36: end procedure
"""


def contar_caminhos(B):
    """
    Função que calcula o número de caminhos possíveis do canto superior esquerdo
    até o canto inferior direito de uma matriz, evitando obstáculos.

    Args:
        B: Matriz booleana onde True representa um obstáculo

    Returns:
        Número de caminhos possíveis
    """
    if not B or len(B) == 0 or len(B[0]) == 0:
        return 0

    n = len(B)
    m = len(B[0])

    # Se o ponto inicial ou final tiver obstáculo, não há caminho possível
    if B[0][0] or B[n - 1][m - 1]:
        return 0

    # Matriz para armazenar o número de caminhos para cada posição
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Inicializa a posição inicial
    dp[0][0] = 1

    # Preenche a primeira coluna
    for i in range(1, n):
        if not B[i][0]:
            dp[i][0] = dp[i - 1][0]

    # Preenche a primeira linha
    for j in range(1, m):
        if not B[0][j]:
            dp[0][j] = dp[0][j - 1]

    # Preenche o resto da matriz
    for i in range(1, n):
        for j in range(1, m):
            if not B[i][j]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]


# Exemplo de uso:
if __name__ == "__main__":
    # Exemplo 1: Matriz 3x3 sem obstáculos
    # fmt: off
    matriz1 = [[False, False, False], 
               [False, False, False], 
               [False, False, False]]
    # fmt: on
    print(
        f"Matriz 3x3 sem obstáculos: {contar_caminhos(matriz1)} caminhos"
    )  # Deve ser 6

    # Exemplo 2: Matriz 3x3 com um obstáculo
    # fmt: off
    matriz2 = [[False, False, False], 
               [False, True, False], 
               [False, False, False]]
    # fmt: on
    print(
        f"Matriz 3x3 com um obstáculo: {contar_caminhos(matriz2)} caminhos"
    )  # Deve ser 2

    # Exemplo 3: Matriz 3x4 com múltiplos obstáculos
    # fmt: off
    matriz3 = [
        [False, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
    ]
    # fmt: on
    print(
        f"Matriz 3x4 com múltiplos obstáculos: {contar_caminhos(matriz3)} caminhos"
    )  # Deve ser 1
