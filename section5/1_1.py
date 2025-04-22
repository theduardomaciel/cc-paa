"""
QUESTÃO 1:
Inteiros positivos são arranjados em um triângulo equilátero com n números em sua base, como o mostrado na figura abaixo para $n = 4.$

# Exemplo:
#     2
#    5 4
#   3 4 7
#  1 6 9 6
# A soma mínima do caminho é 2 + 4 + 4 + 1 = 11, e o caminho é [2, 4, 4, 1].

O problema é encontrar a menor soma em uma descida do ápice do triângulo até sua base por meio de uma sequência de números adjacentes (mostrados na figura pelos círculos).

Projete um algoritmo de programação dinâmica para este problema.
"""

""" 
função MinimumPathSumOtimizado(triangle):
    n ← número de níveis do triângulo
    linha_atual ← array de tamanho n inicializado com infinito
    linha_anterior ← array de tamanho n inicializado com infinito

    linha_anterior[0] ← triangle[0][0]

    Para i de 1 até n-1:
        Para j de 0 até i:
            linha_atual[j] ← infinito

            // Verificar elemento à esquerda superior
            se j > 0:
                linha_atual[j] ← min(linha_atual[j], linha_anterior[j-1] + triangle[i][j])

            // Verificar elemento à direita superior
            se j < i:
                linha_atual[j] ← min(linha_atual[j], linha_anterior[j] + triangle[i][j])

        // Trocar as linhas para a próxima iteração
        linha_anterior, linha_atual ← linha_atual, linha_anterior

    // Encontrar o mínimo na última linha
    resultado ← infinito
    Para j de 0 até n-1:
        resultado ← min(resultado, linha_anterior[j])

    Retornar resultado
"""


def minimum_path_sum_optimized(triangle):
    n = len(triangle)
    current_row = [float("inf")] * n
    previous_row = [float("inf")] * n

    previous_row[0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            current_row[j] = float("inf")

            # Verificar elemento à esquerda superior
            if j > 0:
                current_row[j] = min(
                    current_row[j], previous_row[j - 1] + triangle[i][j]
                )

            # Verificar elemento à direita superior
            if j < i:
                current_row[j] = min(current_row[j], previous_row[j] + triangle[i][j])

        # Trocar as linhas para a próxima iteração
        previous_row, current_row = current_row, previous_row

    # Encontrar o mínimo na última linha
    result = float("inf")
    for j in range(n):
        result = min(result, previous_row[j])

    return result


# Exemplo de uso
triangle = [
    [2],
    [5, 4],
    [3, 4, 7],
    [1, 6, 9, 6],
]

print("Soma mínima do caminho:", minimum_path_sum_optimized(triangle))
# Saída: Soma mínima do caminho: 11
