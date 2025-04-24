"""
1: procedure FORMAS_DE_SOMAR_COM_DADOS(n, k)
2:   // Inicializa a matriz DP onde dp[i][j] representa o número de maneiras
3:   // de obter a soma j com i dados
4:   dp ← matriz (n+1) × (k+1) inicializada com zeros
5:
6:   // Caso base: há 1 maneira de obter soma 0 com 0 dados
7:   dp[0][0] ← 1
8:
9:   // Para cada número de dados
10:  for i ← 1 to n do
11:    // Para cada soma possível
12:    for j ← 1 to k do
13:      // Considerar todas as faces possíveis do dado atual (1-6)
14:      for face ← 1 to 6 do
15:        if j - face ≥ 0 then
16:          dp[i][j] += dp[i-1][j-face]
17:        end if
18:      end for
19:    end for
20:  end for
21:
22:  return dp[n][k]
23: end procedure
"""


def print_dp(dp):
    for row in dp:
        print(row)


def formas_de_somar_com_dados(n, k):
    """
    Calcula o número de formas de obter uma soma k com n dados.

    Args:
        n: Quantidade de dados
        k: Soma desejada

    Returns:
        Número de maneiras de obter soma k com n dados
    """
    # Inicializa a matriz DP
    # dp[i][j] = número de maneiras de obter soma j com i dados
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Caso base: há 1 maneira de obter soma 0 com 0 dados
    dp[0][0] = 1

    # Para cada número de dados (linha)
    for i in range(1, n + 1):
        # Para cada soma possível (coluna)
        for j in range(1, k + 1):
            # Considerar todas as faces possíveis do dado atual (1-6)
            for face in range(1, 7):
                if j - face >= 0:
                    dp[i][j] += dp[i - 1][j - face]
                    print_dp(dp)
                    print(" ")

    return dp[n][k]


# Exemplo do enunciado
n = 2
k = 3
resultado = formas_de_somar_com_dados(n, k)
print(f"Número de formas de obter soma {k} com {n} dados: {resultado}")
