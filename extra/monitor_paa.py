"""
1: procedure CALCULAR_S_N(n)
2:   // Calcula o número de vetores binários de tamanho n sem zeros consecutivos
3:   if n = 0 then
4:      return 1  // Caso base: vetor vazio
5:   end if
6:   if n = 1 then
7:      return 2  // Caso base: vetores possíveis 0 e 1
8:   end if
9:
10:  // Inicializa o array de programação dinâmica
11:  S ← array de tamanho n + 1 inicializado com zeros
12:  S[0] ← 1  // Convenção para o caso vazio
13:  S[1] ← 2  // Vetores de tamanho 1: 0, 1
14:
15:  // Preenchendo a tabela usando a recorrência $$S_n = S_{n-1} + S_{n-2}$$, se n >= 2
16:  for i ← 2 → n do
17:     S[i] ← S[i-1] + S[i-2]
18:  end for
19:
20:  // Calcula a probabilidade de não ter bug
21:  probabilidade ← S[n] / 2^n
22:
23:  return S[n]
24: end procedure
"""


def calcular_S_n(n):
    """
    Calcula o número de vetores binários de tamanho n sem zeros consecutivos.

    Args:
        n (int): Tamanho do vetor binário

    Returns:
        int: Número de vetores válidos (S_n)
    """
    # Casos base
    if n == 0:
        return 1  # Apenas um vetor vazio
    if n == 1:
        return 2  # Dois vetores possíveis: 0 e 1

    # Inicializa o array de programação dinâmica
    S = [0] * (n + 1)
    S[0] = 1  # Convenção para o caso vazio
    S[1] = 2  # Vetores de tamanho 1: 0, 1

    # Preenchendo a tabela usando a recorrência S_n = S_{n-1} + S_{n-2}
    for i in range(2, n + 1):
        S[i] = S[i - 1] + S[i - 2]

    # Calcula a probabilidade de não ter bug
    probabilidade = S[n] / (2**n)
    print(f"Probabilidade de não ter bug para n={n}: {probabilidade:.6f}")
    print(f"Probabilidade de ter bug para n={n}: {1-probabilidade:.6f}")

    return S[n]


# Exemplo de uso
for i in range(1, 21):
    print(f"S_{i} = {calcular_S_n(i)}")
