"""
QUESTÃO 10:
Leia o artigo da wikipedia sobre o puzzle Kakuro
https://en.wikipedia.org/wiki/Kakuro e modele exemplo dado utilizando Programação por Restrição.
"""

# Utilizando programação por restrição, podemos modelar o exemplo do Kakuro da seguinte forma:
#
# 1. Definimos as variáveis de decisão:
#    - Cada célula vazia no Kakuro é uma variável que pode assumir valores de 1 a 9.
#    - As variáveis são representadas por uma lista de listas, onde cada sublista representa uma linha do Kakuro.
#
# 2. Definimos os domínios das variáveis:
#    - O domínio de cada variável é o conjunto {1, 2, 3, 4, 5, 6, 7, 8, 9}.
#    - Isso significa que cada célula vazia pode assumir qualquer valor entre 1 e 9.
#
# 3. Definimos as restrições:
#    - As somas das células preenchidas devem ser iguais aos valores indicados nas células de soma.
#    - As células preenchidas não podem ter valores repetidos em uma mesma linha ou coluna.
#
# 4. Definimos a função de restrição:
#   - A função de restrição verifica se as somas das células preenchidas são iguais aos valores indicados nas células de soma.
#   - A função também verifica se não há valores repetidos em uma mesma linha ou coluna.

from constraint import Problem, AllDifferentConstraint

# 1) REPRESENTAÇÃO DO TABULEIRO
# --------------------------------------------------
# None     = bloco preto sem pista
# (h, v)   = bloco preto com pista horizontal 'h' e/ou vertical 'v'
# 0        = célula branca a preencher

# fmt: off
grid = [
    #    0            1           2           3           4           5           6           7
    [None,      (None,23),      (None,30),  None,       None,   (None,27),  (None,12),  (None,16)],
    [(16,None),         0,          0,      None,    (24,17),           0,          0,          0],
    [(17,None),         0,          0,   (29,15),           0,          0,          0,          0],
    [(35,None),         0,          0,          0,          0,          0,  (None,12),       None],
    [None,       (7,None),          0,          0,      (8,7),          0,          0,   (None,7)],
    [None,      (None,11),    (16,10),          0,          0,          0,          0,          0],
    [(21,None),         0,          0,          0,          0,   (5,None),          0,          0],
    [(6,None),          0,          0,          0,       None,   (3,None),          0,          0],
]
# fmt: on

# 2) EXTRAIR AUTOMATICAMENTE OS BLOCOS
# --------------------------------------------------
rows = len(grid)
cols = len(grid[0])
horiz_blocks = []
vert_blocks = []

for r in range(rows):
    for c in range(cols):
        # Obtemos a célula, se for um bloco preto, não faz nada
        cell = grid[r][c]

        # Se tivermos uma pista (tupla), verificamos se é horizontal ou vertical
        if isinstance(cell, tuple):
            h_sum, v_sum = cell

            # Se tivermos uma pista horizontal, seguimos para a direita
            if h_sum is not None:
                vars_h = []
                cc = c + 1  # começamos a partir da célula seguinte

                # enquanto a célula for branca (0), adicionamos a variável
                # e seguimos para a direita
                # se a célula for um bloco preto, não adicionamos a variável
                while cc < cols and grid[r][cc] == 0:
                    vars_h.append(f"{r}_{cc}")
                    cc += 1

                horiz_blocks.append((h_sum, vars_h))

            # Se tivermos uma pista vertical, seguimos para baixo
            if v_sum is not None:
                vars_v = []
                rr = r + 1  # começamos a partir da célula seguinte

                # enquanto a célula for branca (0), adicionamos a variável
                # e seguimos para baixo
                # se a célula for um bloco preto, não adicionamos a variável
                while rr < rows and grid[rr][c] == 0:
                    vars_v.append(f"{rr}_{c}")
                    rr += 1
                vert_blocks.append((v_sum, vars_v))

# 3) MONTAR E RESOLVER O PROBLEMA
# --------------------------------------------------
problem = Problem()

# Adicionamos todas as variáveis
all_vars = {v for _, blk in horiz_blocks + vert_blocks for v in blk}
for v in all_vars:
    problem.addVariable(v, range(1, 10))  # valores de 1 a 9

# Adicionamos as restrições de soma e de unicidade (sem repetição)
# para cada bloco horizontal e vertical
for soma, blk in horiz_blocks + vert_blocks:
    problem.addConstraint(AllDifferentConstraint(), blk)
    problem.addConstraint(lambda *vals, soma=soma: sum(vals) == soma, blk)

sol = problem.getSolution()

# 4) IMPRIMIR
if not sol:
    print("⚠️ Sem solução — reveja o grid ou as pistas.")
else:
    for r in range(rows):
        row = []
        for c in range(cols):
            if grid[r][c] == 0:
                # Obtemos a variável correspondente
                row.append(str(sol[f"{r}_{c}"]))
            else:
                row.append("■")
        print(" ".join(row))
