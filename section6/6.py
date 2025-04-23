"""
QUESTÃO 6:
Considere o seguinte problema de programação linear.
max     5x + 3y
s.a     5x + 2y ≥ 0
x + y ≤ 7
x ≤ 5
x ≥ 0
y ≥ 0

Desenhe a região factível e identifique a solução ótima.
"""

"""
Solução teórica:

Para resolver este problema de programação linear, precisamos:
1. Identificar a região factível (conjunto de pontos que satisfazem todas as restrições)
2. Encontrar o ponto nessa região que maximiza a função objetivo 5x + 3y

Restrições:
- 5x + 2y ≥ 0
- x + y ≤ 7
- x ≤ 5
- x ≥ 0
- y ≥ 0

A função objetivo que queremos maximizar é: 5x + 3y
Para desenhar a região factível, precisamos analisar cada uma dessas restrições no plano cartesiano:

Análise das restrições:

Restrição 1: 5x + 2y ≥ 0
- Se x = 0, então y ≥ 0
- Se y = 0, então x ≥ 0
- Esta é uma semi-plano à direita/acima da linha 5x + 2y = 0

Restrição 2: x + y ≤ 7
- Se x = 0, então y ≤ 7
- Se y = 0, então x ≤ 7
- A linha x + y = 7 passa pelos pontos (0,7) e (7,0)

Restrição 3: x ≤ 5
- Isto é uma linha vertical em x = 5

Restrições 4 e 5: x ≥ 0, y ≥ 0
- Estamos no primeiro quadrante do plano cartesiano

Os vértices da região factível são encontrados nas interseções das restrições:
- (0, 0): origem
- (5, 0): restrições x ≤ 5 e y = 0
- (5, 2): interseção das linhas x = 5 e x + y = 7
- (0, 7): restrições x = 0 e x + y = 7

Para encontrar o valor máximo da função objetivo 5x + 3y, podemos avaliar cada vértice:

- Em (0,0): 5(0) + 3(0) = 0
- Em (5,0): 5(5) + 3(0) = 25
- Em (5,2): 5(5) + 3(2) = 25 + 6 = 31
- Em (0,7): 5(0) + 3(7) = 21

O valor máximo da função objetivo é 31, alcançado no ponto (5,2).
Portanto, a solução ótima é:
- x = 5
- y = 2
- Valor máximo = 31
"""

# Implementação da solução com Python e verificação usando scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


# Plotar a região factível
def plot_constraint(x, expr, label):
    plt.plot(x, expr, label=label)


# Configuração do gráfico
plt.figure(figsize=(10, 8))
plt.grid(True)
plt.axhline(y=0, color="k", linestyle="-", alpha=0.3)
plt.axvline(x=0, color="k", linestyle="-", alpha=0.3)

# Definir limites para melhor visualização
x_range = np.linspace(-1, 6, 1000)

# Plotando as restrições
plot_constraint(x_range, np.maximum(0, -5 * x_range / 2), "5x + 2y ≥ 0 (y ≥ -5x/2)")
plot_constraint(x_range, 7 - x_range, "x + y ≤ 7 (y ≤ 7-x)")
plt.axvline(x=5, color="r", linestyle="-", label="x ≤ 5")
plt.axhline(y=0, color="g", linestyle="-", label="y ≥ 0")

# Sombreando a região factível
x_fill = np.linspace(0, 5, 1000)
y1 = np.maximum(0, np.maximum(0, -5 * x_fill / 2))
y2 = np.minimum(7 - x_fill, np.ones_like(x_fill) * 7)
plt.fill_between(x_fill, y1, y2, alpha=0.2, color="blue")

# Marcando os vértices
vertices = [(0, 0), (5, 0), (5, 2), (0, 7)]
x_vertices, y_vertices = zip(*vertices)
plt.scatter(x_vertices, y_vertices, c="red", s=100, zorder=5)

# Adicionando os valores da função objetivo para cada vértice
for i, v in enumerate(vertices):
    obj_value = 5 * v[0] + 3 * v[1]
    plt.annotate(
        f"({v[0]}, {v[1]})\nf={obj_value}",
        (v[0], v[1]),
        xytext=(10, 10),
        textcoords="offset points",
    )

# Plotando alguns contornos da função objetivo
for z in [0, 10, 20, 30]:
    # 5x + 3y = z => y = (z - 5x)/3
    y_obj = (z - 5 * x_range) / 3
    plt.plot(x_range, y_obj, "k--", alpha=0.5)
    plt.annotate(
        f"f = {z}", (x_range[-1], y_obj[-1]), xytext=(10, 0), textcoords="offset points"
    )

# Solução usando scipy.optimize.linprog
# Forma padrão para linprog (minimização): min c^T x sujeito a A_ub x <= b_ub e A_eq x = b_eq
# Como queremos maximizar 5x + 3y, vamos minimizar -5x - 3y
c = [-5, -3]  # Coeficientes da função objetivo (negativo para maximização)

# Restrições de desigualdade na forma A_ub x <= b_ub
A_ub = [
    [1, 1],  # x + y <= 7
    [1, 0],  # x <= 5
    [-5, -2],  # -5x - 2y <= 0 (equivalente a 5x + 2y >= 0)
]
b_ub = [7, 5, 0]

# Limites para as variáveis
bounds = [(0, None), (0, None)]  # x >= 0, y >= 0

# Resolver o problema de programação linear
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="simplex")

# Exibir o resultado
optimal_x = result.x
optimal_value = -result.fun  # Negativo porque estamos maximizando

# Adicionar texto com resultados da scipy
optimal_text = (
    f"Resultado usando scipy.optimize.linprog:\n"
    f"Solução ótima: x = {optimal_x[0]:.2f}, y = {optimal_x[1]:.2f}\n"
    f"Valor ótimo: {optimal_value:.2f}"
)
plt.annotate(
    optimal_text,
    (0.05, 0.05),
    xycoords="axes fraction",
    bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
)

plt.title("Problema de Programação Linear - Região Factível")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.xlim(-1, 6)
plt.ylim(-1, 8)
plt.tight_layout()

# Destacar a solução ótima
plt.scatter([optimal_x[0]], [optimal_x[1]], c="green", s=200, marker="*", zorder=6)
plt.annotate(
    "Solução Ótima",
    (optimal_x[0], optimal_x[1]),
    xytext=(20, 20),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->"),
)

plt.savefig("programacao_linear_q6.png")
plt.show()

# Exibir o resultado
print("Solução teórica:")
print("Vértice ótimo: (5, 2)")
print("Valor ótimo: 31")
print("\nSolução computacional:")
print(f"Vértice ótimo: ({optimal_x[0]:.6f}, {optimal_x[1]:.6f})")
print(f"Valor ótimo: {optimal_value:.6f}")
