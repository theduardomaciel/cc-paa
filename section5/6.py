"""
QUESTÃO 6:
Dadas duas strings $$x=x_1x_2...x_n$$ e $$y=y_1y_2...y_m$$, desejamos encontrar o comprimento da maior *substring* comum delas, isto é, o maior $$k$$ para o qual existem índices $$i$$ e $$j$$ com $$x=x_ix_{i+1}...x_{i+k-1}=y_jy_{j+1}...y_{j+k-1}$$

Mostre como fazer isso em tempo $$O(m.n)$$.
"""

# 1. Caracterizar a sub-estrutura ótima:
# Se os últimos caracteres forem iguais, o ótimo será igual a 1 + o ótimo do restante,
# sendo o "restante" o subproblema sem os últimos caracteres (ou seja, x[0...n-2] e y[0...m-2]).
# Caso contrário, podemos descartar um dos dois últimos caracteres e continuar a busca.

# 2. Definir recursivamente o valor de uma solução ótima:
# dp[i][j] = comprimento da substring ótima de A[1..i] e B[1..j]
# dp[i][j] = 0, se i = 0 ou j = 0 (caso base)
# dp[i][j] = 1 + dp[i-1][j-1], se A[i] = B[j]
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]), se A[i] != B[j]

""" 
(solução para substrings não contínuas)	
função MaiorSubstringComum(x, y):
    n = comprimento(x)
    m = comprimento(y)

    // Criar matriz DP de tamanho (n+1) × (m+1) inicializada com zeros
    DP[0...n][0...m] = 0

    3. Calcular o valor de uma solução ótima
    para i de 1 até n:
        para j de 1 até m:
            se x[i-1] = y[j-1]:  // índices ajustados para base 0
                DP[i][j] = 1 + DP[i-1][j-1]
            senão:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    4. Construir uma solução ótima com as informações calculadas
    // A maior substring comum é o valor na posição DP[n][m]
    retornar DP[n][m]
"""


def longest_common_substring(x, y):
    n = len(x)
    m = len(y)

    # Criar matriz DP de tamanho (n+1) x (m+1) inicializada com zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Preencher a matriz DP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:  # Ajustando os índices para base 0
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


# Testando a função
x = "zxyxyz"
y = "xyyzx"
print(longest_common_substring(x, y))  # Saída: 2 (a substring comum é "xyyz")

"""
versão alternativa: (solução para substrings contínuas)
se x[i] = y[j]: dp[i][j] = 1 + dp[i-1][j-1]
senão: dp[i][j] = 0

O comprimento da maior substring comum é o maior valor na matriz dp.

função MaiorSubstringComum(x, y):
    n = comprimento(x)
    m = comprimento(y)

    // Criar matriz DP de tamanho (n+1) × (m+1) inicializada com zeros
    DP[0...n][0...m] = 0

    maior_comprimento = 0

    3. Calcular o valor de uma solução ótima
    para i de 1 até n:
        para j de 1 até m:
            se x[i-1] = y[j-1]:  // índices ajustados para base 0
                DP[i][j] = 1 + DP[i-1][j-1]
                maior_comprimento = max(maior_comprimento, DP[i][j])
            senão:
                DP[i][j] = 0

    4. Construir uma solução ótima com as informações calculadas
    // A maior substring comum é o maior valor na matriz DP
    retornar maior_comprimento
"""


def longest_common_substring_alt(x, y):
    n = len(x)
    m = len(y)

    # Criar matriz DP de tamanho (n+1) x (m+1) inicializada com zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    longest_length = 0

    # Preencher a matriz DP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:  # Ajustando os índices para base 0
                dp[i][j] = dp[i - 1][j - 1] + 1
                longest_length = max(longest_length, dp[i][j])
            else:
                dp[i][j] = 0

    return longest_length


# Testando a função
x = "zxyxyz"
y = "xyyzx"
print(longest_common_substring_alt(x, y))  # Saída: 2 (a substring comum é "xy")
