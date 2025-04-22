"""
QUESTÃO 5:

Uma subsequência contígua de uma lista S é uma subsequência feita de elementos consecutivos de S.

Por exemplo, se S é
$$
5, 15, −30, 10, −5, 40, 10,
$$
então 15, −30, 10 é uma subsequência contígua, mas 5, 15, 40 não é.

Forneça um algoritmo de tempo linear para a seguinte tarefa:
Entrada: Uma lista de números $$a_1$$, $$a_2$$, . . . , $$a_n$$ .
Saída: A subsequência contígua de soma máxima (a subsequência de tamanho zero tem soma zero).

Para o exemplo anterior, a resposta seria $$10, −5, 40, 10$$, com uma soma de $$55$$.
(Dica: Para cada  $$j ∈ \{{1, 2, . . . , n}\}$$ considere subsequências contíguas terminando exatamente na posição $$j$$.)
"""

# 1. Caracterizar a sub-estrutura ótima:
# A soma máxima de uma subsequência contígua até o índice j é
# igual à soma máxima da subsequência contígua até o índice j-1,
# mais o elemento na posição j, ou apenas o elemento na posição j (se a soma anterior for negativa).

# 2. Definir recursivamente o valor de uma solução ótima:
# A soma máxima da subsequência contígua até o índice j é:
# maxAtual[j] = max(maxAtual[j-1] + A[j], A[j])

""" 
SUBSEQUÊNCIA-CONTÍGUA-SOMA-MÁXIMA(A):
    n ← comprimento(A)
    maxAtual ← 0
    maxGlobal ← 0
    inicioAtual ← 0
    inicioMaximo ← 0
    fimMaximo ← 0

    # 3. Calcular o valor de uma solução ótima
    para j ← 1 até n faça:
        // Se maxAtual se tornou negativo, começamos uma nova subsequência
        se maxAtual ≤ 0 então:
            maxAtual ← A[j]
            inicioAtual ← j
        senão:
            maxAtual ← maxAtual + A[j]

        // Atualizamos o máximo global se necessário
        se maxAtual > maxGlobal então:
            maxGlobal ← maxAtual
            inicioMaximo ← inicioAtual
            fimMaximo ← j

    4. Construir uma solução ótima com as informações calculadas
    // A subsequência contígua de soma máxima é a que vai do índice inicioMaximo até fimMaximo    
        
    // Se o maxGlobal continuar sendo 0, significa que todos os elementos eram negativos
    // Neste caso, retornamos a subsequência vazia conforme o enunciado
    se maxGlobal = 0 então:
        retorne "subsequência vazia"
    senão:
        retorne subsequência de A do índice inicioMaximo até fimMaximo
"""


def max_subarray_sum(arr):
    n = len(arr)
    max_current = 0
    max_global = 0
    start_current = 0
    start_max = 0
    end_max = 0

    for j in range(n):
        # Se max_current se tornou negativo, começamos uma nova subsequência
        if max_current <= 0:
            max_current = arr[j]
            start_current = j
        else:
            max_current += arr[j]

        # Atualizamos o máximo global se necessário
        if max_current > max_global:
            max_global = max_current
            start_max = start_current
            end_max = j

    # Se o max_global continuar sendo 0, significa que todos os elementos eram negativos
    # Neste caso, retornamos a subsequência vazia conforme o enunciado
    if max_global == 0:
        return "subsequência vazia"
    else:
        return arr[start_max : end_max + 1]


# Testando a função com o exemplo fornecido
arr = [5, 15, -30, 10, -5, 40, 10]
result = max_subarray_sum(arr)
print("Subsequência contígua de soma máxima:", result)
print("Soma máxima:", sum(result) if isinstance(result, list) else result)
# Saída esperada:
# Subsequência contígua de soma máxima: [10, -5, 40, 10]
# Soma máxima: 55
