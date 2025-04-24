"""
QUESTÃO 8:
PROBLEMA DE COBERTURA.

O governo planeja construir escolas de modo a satisfazer a demanda em uma cidade.
Ainda não se sabe quantas escolas são necessárias, mas a lei demanda que todo bairro deve estar próximo a uma escola.

Dado o grafo de proximidade $$G = (V, E)$$ e $$C_v$$ o custo de se instalar a escola no bairro $$j$$.
Em que bairro deve ser construídas escolas de modo a respeitar a lei sem desperdiçar dinheiro publico?

Modelo o problema por Programação Linear Inteira.
"""

# Precisamos decidir em quais bairros construir escolas para que:
# - 1. Todo bairro tenha acesso a pelo menos uma escola (diretamente ou através de um bairro vizinho)
# - 2. O custo total seja minimizados

""" 
Podemos modelar o problema da seguinte forma:
- $$G = (V, E)$$ é o grafo de proximidade, onde $$V$$ são os bairros e $$E$$ são as conexões de proximidade
- $$C_v$$ é o custo de construir uma escola no bairro $$v$$
- Para cada bairro $$j$$, definimos $$N[j]$$ como o conjunto que contém o próprio bairro $$j$$ e todos os seus vizinhos

Variáveis de decisão:
- $$x_j$$: variável binária que indica se uma escola é construída no bairro $$j$$ (1) ou não (0)
Portanto, temos $$x_j \in \{0, 1\}$$ para cada bairro $$j \in V$$
- $$x_j = 1$$ se uma escola é construída no bairro $$j$$, 
- $$x_j = 0$$ caso contrário

Função objetivo:
- Minimizar o custo total de construção das escolas:

$$Minimizar \sum_{j \in V} C_j \cdot x_j$$

Restrições:
Para atender a lei, cada bairro $$i$$ deve ter pelo menos uma escola em sua vizinhança (incluindo ele mesmo):

$$\sum_{j \in N[i]} x_j \geq 1$$ para todo $$i \in V$$

Isso garante que cada bairro $$j$$ tenha acesso a pelo menos uma escola, seja construindo uma escola nele mesmo ou em um de seus vizinhos.

Restrição de variáveis binárias:
- $$x_j \in \{0, 1\}$$ para todo $$j \in V$$

O modelo de Programação Linear Inteira completo está assim definido:
$$
\begin{align*}
\text{Minimizar} & \quad \sum_{j \in V} C_j \cdot x_j \\
\text{Sujeito a} & \quad \sum_{i \in N[j]} x_i \geq 1, \quad \forall j \in V \\
\text{onde} & \quad x_j \in \{0, 1\}, \quad \forall j \in V \\
\end{align*}
$$
"""
