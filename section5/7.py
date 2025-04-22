"""
QUESTÃO 7:
Forneça um algoritmo de programação dinâmica (note que será pseudo-polinomial) para o problema SUBSET SUM.

Entrada: Um conjunto A com valores inteiros positivos, e um inteiro t.
Questão: Existe um subconjunto A' ⊆ A cuja soma dos valores seja exatamente t?

Extra:
Dada uma solução positiva da questão anterior,
forneça um algoritmo para determinar os elementos utilizados na soma.
"""

# 1. Caracterizar a sub-estrutura ótima:
# Se a soma de um subconjunto A' é igual a t, então podemos considerar dois casos:
# 1) O elemento x está incluído no subconjunto A', então a soma dos outros elementos deve ser t - x.
# 2) O elemento x não está incluído no subconjunto A', então a soma dos outros elementos deve ser t.

# 2. Definir recursivamente o valor de uma solução ótima:
# dp[i][j] = True se existe um subconjunto de A[0...i] cuja soma é j, caso contrário False.
# dp[i][j] = dp[i-1][j] (não inclui o elemento i) ou dp[i-1][j - A[i]] (inclui o elemento i)
# dp[i][j] = 0, se i = 0 ou j = 0 (caso base)
# dp[i][j] = 1, se A[i] = j (caso base)

""" 
SubsetSum(A, t):
    n = tamanho de A

    // Inicializa tabela DP[0...n][0...t]
    DP = matriz de tamanho (n+1) × (t+1) inicializada com False

    // Base: é possível formar a soma 0 sem usar nenhum elemento
    Para i de 0 até n:
        DP[i][0] = True

    3. Calcular o valor de uma solução ótima
    // Preenche a tabela DP
    Para i de 1 até n:
        Para j de 1 até t:
            // Caso 1: Não incluímos o elemento A[i-1]
            DP[i][j] = DP[i-1][j]

            // Caso 2: Incluímos o elemento A[i-1] se ele não exceder j
            Se j >= A[i-1]:
                DP[i][j] = DP[i][j] OU DP[i-1][j-A[i-1]]

    4. Construir uma solução ótima com as informações calculadas
    // A resposta está em DP[n][t]
    Retorna DP[n][t]
"""


def subset_sum(A, t):
    n = len(A)
    # Inicializa tabela DP[0...n][0...t]
    dp = [[False] * (t + 1) for _ in range(n + 1)]

    # Base: é possível formar a soma 0 sem usar nenhum elemento
    for i in range(n + 1):
        dp[i][0] = True

    # Preenche a tabela DP
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            # Caso 1: Não incluímos o elemento A[i-1]
            dp[i][j] = dp[i - 1][j]

            # Caso 2: Incluímos o elemento A[i-1] se ele não exceder j
            if j >= A[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]

    return (dp[n][t], dp)  # Retorna se existe um subconjunto e a tabela DP


# Testando a função
A = [3, 34, 4, 12, 5, 2]
t = 9
result, dp = subset_sum(A, t)
print(
    f"Existe um subconjunto que soma {t}: {result}"
)  # Saída: True (subconjunto {4, 5} tem soma 9)

# Extra: determinando os elementos utilizados na soma

""" 
RecuperaSubconjunto(A, t, DP):
    n = tamanho de A
    resultado = []
    i = n
    j = t

    // Se não existe solução, retorna conjunto vazio
    Se DP[n][t] == False:
        Retorna []

    // Rastreia os elementos incluídos
    Enquanto i > 0 e j > 0:
        // Se o valor mudou ao incluir o elemento i
        Se j >= A[i-1] e DP[i-1][j-A[i-1]] == True:
            // Incluímos o elemento A[i-1] na solução
            resultado.adiciona(A[i-1])
            j = j - A[i-1]
        i = i - 1

    Retorna resultado
"""


def find_subset(A, t, dp):
    n = len(A)

    # Se não existe solução, retorna conjunto vazio
    if not dp[n][t]:
        return []

    # Reconstruindo o subconjunto
    subset = []
    i, j = n, t
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:  # O elemento A[i-1] foi incluído
            subset.append(A[i - 1])
            j -= A[i - 1]  # Reduz a soma restante
        i -= 1

    return subset[::-1]  # Retorna o subconjunto na ordem original


# Testando a função para encontrar os elementos utilizados na soma
subset = find_subset(A, t, dp)
print(f"Subconjunto que soma {t}: {subset}")  # Saída: [4, 5]
# (ou outra combinação que some 9, dependendo da ordem dos elementos em A)
