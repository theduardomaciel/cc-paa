"""
QUESTÃO 2:

Algumas moedas são espalhadas nas células de um tabuleiro $$n \times m$$, uma moeda por célula.
Um robô, localizado na célula superior esquerda do tabuleiro, precisa coletar o máximo de moedas possível e trazê-las para a célula inferior direita.
Em cada etapa, o robô pode mover uma célula para a direita ou uma célula para baixo de sua localização atual.
Quando o robô visita uma célula com uma moeda, ele pega amoeda.
Elabore um algoritmo para encontrar o número máximo de moedas que o robô pode coletar e um caminho que ele precisa seguir para fazer isso.
"""

# Tabuleiro n x m com moedas espalhadas
# Um robô começa na célula (0, 0) e deve terminar na célula (n - 1, m - 1).
# O robô pode se mover para a direita ou para baixo.
# O objetivo é encontrar o caminho que maximiza o número de moedas coletadas.

# Exemplo:
# 0 1 0 0
# 1 0 1 0
# 0 1 0 1
# 0 0 1 0
# O robô começa na célula (0, 0) e termina na célula (n - 1, m - 1) = (3, 3).
# O caminho máximo de moedas é 1 -> 1 -> 1 -> 1, totalizando 4 moedas.

# 1. Caracterizar a Sub-estrutura ótima:
# O número máximo de moedas coletadas até a célula (i, j)
# Para cada célula (i, j), como o robô só anda para baixo ou para direita,
# ele só pode vir da célula de cima (i - 1, j) ou da esquerda (i, j - 1).
# i = linha, j = coluna.
# Assim, a soma máxima de moedas até a célula (i, j) é a soma máxima de moedas
# até a célula (i - 1, j) ou (i, j - 1), mais o valor na posição (i, j).

# 2. Definir recursivamente o valor de uma solução ótima:
# Assim, a sub-estrutura ótima é:
# dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
# Onde grid[i][j] é 1 se houver uma moeda na célula (i, j) e 0 caso contrário.

""" 
function EncontrarCaminhoMáximoDeMoedas(tabuleiro[n][m]):
    // Inicializar matriz DP
    DP[n][m] = 0

    // Inicializar matriz para rastrear o caminho
    caminho[n][m] = ""

    // Preencher a primeira célula
    DP[0][0] = tabuleiro[0][0]

    // Preencher a primeira linha
    for j ← 1 → m-1:
        DP[0][j] = DP[0][j-1] + tabuleiro[0][j]
        caminho[0][j] = "direita"

    // Preencher a primeira coluna
    for i ← 1 → n-1:
        DP[i][0] = DP[i-1][0] + tabuleiro[i][0]
        caminho[i][0] = "baixo"

    // Preencher o resto da matriz
    for i ← 1 → n-1:
        for j ← 1 → m-1:
            if DP[i-1][j] > DP[i][j-1]:
                DP[i][j] = DP[i-1][j] + tabuleiro[i][j]
                caminho[i][j] = "baixo"
            else:
                DP[i][j] = DP[i][j-1] + tabuleiro[i][j]
                caminho[i][j] = "direita"

    // Reconstruir o caminho
    resultado = []
    i = n-1, j = m-1

    while i > 0 ou j > 0:
        if caminho[i][j] == "baixo":
            resultado.inserir_no_início("baixo")
            i = i-1
        else:
            resultado.inserir_no_início("direita")
            j = j-1

    return (DP[n-1][m-1], resultado)
"""


def max_coins_path(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [
        [0] * m for _ in range(n)
    ]  # Matriz DP para armazenar o número máximo de moedas
    path = [[""] * m for _ in range(n)]  # Matriz para rastrear o caminho

    # Preencher a primeira célula
    dp[0][0] = grid[0][0]

    # Preencher a primeira linha
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        path[0][j] = "direita"

    # Preencher a primeira coluna
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        path[i][0] = "baixo"

    # Preencher o resto da matriz DP
    for i in range(1, n):
        for j in range(1, m):
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
                path[i][j] = "baixo"
            else:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
                path[i][j] = "direita"

    # Reconstruir o caminho
    result_path = []
    i, j = n - 1, m - 1

    while i > 0 or j > 0:
        if path[i][j] == "baixo":
            result_path.insert(0, "baixo")
            i -= 1
        else:
            result_path.insert(0, "direita")
            j -= 1

    return (dp[n - 1][m - 1], result_path)


# Teste da função
if __name__ == "__main__":
    # fmt: off
    grid = [[0, 1, 1, 0], 
            [1, 0, 1, 0], 
            [0, 1, 0, 1], 
            [0, 0, 0, 0]]
    # fmt: on

    max_coins, path = max_coins_path(grid)
    print("Número máximo de moedas:", max_coins)
    print("Caminho:", path)

    # Saída esperada:
    # Número máximo de moedas: 4
    # Possível caminho: ['direita', 'baixo', 'baixo', 'direita']
    # O robô começa na célula (0, 0) e termina na célula (3, 3).
