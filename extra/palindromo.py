"""
1: procedure SUBSEQUÊNCIA_PALINDRÔMICA_MAIS_LONGA(s)
2:   n ← comprimento de s
3:
4:   // Inicializa a matriz DP com zeros
5:   dp ← matriz n × n inicializada com zeros
6:
7:   // Cada caractere por si só é um palíndromo de tamanho 1
8:   for i ← 0 to n-1 do
9:     dp[i][i] ← 1
10:  end for
11:
12:  // Preencher a matriz DP
13:  // Começamos com subcadeias de tamanho 2 e vamos aumentando
14:  for cl ← 2 to n do
15:    for i ← 0 to n-cl do
16:      j ← i + cl - 1  // Índice final da subcadeia
17:
18:      // Se os dois caracteres nas extremidades são iguais
19:      if s[i] = s[j] and cl = 2 then
20:        dp[i][j] ← 2
21:      else if s[i] = s[j] then
22:        dp[i][j] ← dp[i+1][j-1] + 2
23:      else
24:        dp[i][j] ← max(dp[i][j-1], dp[i+1][j])
25:      end if
26:    end for
27:  end for
28:
29:  // Reconstruir a subsequência palindrômica mais longa
30:  return RECONSTRUIR_PALÍNDROMO(s, dp, 0, n-1)
31: end procedure
32:
33: procedure RECONSTRUIR_PALÍNDROMO(s, dp, i, j)
34:   // Se só temos um caractere
35:   if i = j then
36:     return s[i]
37:   end if
38:
39:   // Se temos dois caracteres iguais
40:   if i+1 = j and s[i] = s[j] then
41:     return s[i] + s[j]
42:   end if
43:
44:   // Se os caracteres nas extremidades são iguais
45:   if s[i] = s[j] then
46:     return s[i] + RECONSTRUIR_PALÍNDROMO(s, dp, i+1, j-1) + s[j]
47:   end if
48:
49:   // Se o caractere da esquerda dá o melhor resultado
50:   if dp[i][j-1] > dp[i+1][j] then
51:     return RECONSTRUIR_PALÍNDROMO(s, dp, i, j-1)
52:   else
53:     return RECONSTRUIR_PALÍNDROMO(s, dp, i+1, j)
54:   end if
55: end procedure
"""


def longest_palindromic_subsequence(s):
    n = len(s)

    # Inicializa a matriz DP com zeros
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Cada caractere por si só é um palíndromo de tamanho 1
    for i in range(n):
        dp[i][i] = 1

    # Preencher a matriz DP
    # Começamos com subcadeias de tamanho 2 e vamos aumentando
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1  # Índice final da subcadeia

            # Se os dois caracteres nas extremidades são iguais
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # Reconstruir a subsequência palindrômica mais longa
    result = reconstruct_palindrome(s, dp, 0, n - 1)

    return result


def reconstruct_palindrome(s, dp, i, j):
    # Se só temos um caractere
    if i == j:
        return s[i]

    # Se temos dois caracteres iguais
    if i + 1 == j and s[i] == s[j]:
        return s[i] + s[j]

    # Se os caracteres nas extremidades são iguais
    if s[i] == s[j]:
        return s[i] + reconstruct_palindrome(s, dp, i + 1, j - 1) + s[j]

    # Se o caractere da esquerda dá o melhor resultado
    if dp[i][j - 1] > dp[i + 1][j]:
        return reconstruct_palindrome(s, dp, i, j - 1)
    else:
        return reconstruct_palindrome(s, dp, i + 1, j)


# Exemplo de uso
s = "character"
print(longest_palindromic_subsequence(s))  # Saída: carac
