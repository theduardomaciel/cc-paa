"""
QUESTÃO 7:
A companhia de produtos caninos oferece duas comidas para cachorro: Viralata’s e Ração do Sucesso,
que são feitas de uma mistura de cereais e carne.

Um pacote de Viralata’s requer 1 quilo de cereal e 1,5 quilo de carne, e é vendido por $7.
Um pacote de Ração do Sucesso usa 2 quilos de cereal e 1 quilo de carne, e é vendido por $6.

O cereal bruto custa $1 por quilo e a carne bruta, $2 por quilo.

Há também o custo de $1,40 para empacotar o Viralata’s e $0,60 para o Ração do Sucesso.
Um total de 240.000 quilos de cereal e 180.000 quilos de carne estão disponíveis a cada mês.
O único gargalo de produção está no fato de a fábrica poder empacotar apenas 110.000 pacotes de Viralata’s por mês.

Desnecessário dizer, a gerência gostaria de maximizar o lucro.

1. Formule o problema como um programa linear em duas variáveis.
2. Desenhe a região factível, dê as coordenadas de cada vértice, e circule o vértice que maximiza o lucro. Qual o lucro máximo possível?
"""

"""
Solução teórica:
- x = número de pacotes de Viralata's produzidos por mês
- y = número de pacotes de Ração do Sucesso produzidos por mês

Viralata's (x):
- Uso de cereal: 1 kg/pacote
- Uso de carne: 1,5 kg/pacote
- Preço de venda: $7/pacote
- Custo de matéria-prima: $1/kg (cereal) + $2/kg (carne) = $1 + $3 = $4/pacote
- Custo de empacotamento: $1,40/pacote
- Lucro por pacote: $7 - $4 - $1,40 = $1,60/pacote

Ração do Sucesso (y):
- Uso de cereal: 2 kg/pacote
- Uso de carne: 1 kg/pacote
- Preço de venda: $6/pacote
- Custo de matéria-prima: $1/kg (cereal) + $2/kg (carne) = $2 + $2 = $4/pacote
- Custo de empacotamento: $0,60/pacote
- Lucro por pacote: $6 - $4 - $0,60 = $1,40/pacote

Função objetivo: (maximizar lucro)
Z = 1,60x + 1,40y

Restrições:
- Cereal disponível: 1x + 2y ≤ 240.000 kg
- Carne disponível: 1,5x + 1y ≤ 180.000 kg
- Limite de capacidade de empacotamento do: x ≤ 110.000 pacotes
- Não-negatividade: x, y ≥ 0 (não pode produzir pacotes negativos)

Portanto, o problema de programação linear é:
Maximizar Z = 1,60x + 1,40y
Sujeito a:
- 1x + 2y ≤ 240.000
- 1,5x + 1y ≤ 180.000
- x ≤ 110.000
- x, y ≥ 0

Análise das restrições:

Restrição 1: 1x + 2y ≤ 240.000
- Se x = 0, então 2y ≤ 240.000 → y ≤ 120.000
- Se y = 0, então x ≤ 240.000 (violação da restrição de capacidade x ≤ 110.000)
- A linha 1x + 2y = 240.000 passa pelo ponto (0, 120.000) [vértice A]

Restrição 2: 1,5x + 1y ≤ 180.000 
- Se x = 0, então y ≤ 180.000 (violação da restrição do cereal, 1.(0) + 2.(180.000) = 360.000 > 240.000)
- Se y = 0, então 1,5x ≤ 180.000 → x ≤ 120.000 (violação da restrição de capacidade x ≤ 110.000)

Restrição 3: x ≤ 110.000
- Isto é uma linha vertical em x = 110.000
- Se y = 0, então x ≤ 110.000
- A linha x = 110.000 passa pelo ponto (110.000, 0) [vértice B]

Restrições 4 e 5: x ≥ 0, y ≥ 0
- Estamos no primeiro quadrante do plano cartesiano

Intersecção entre a restrição 1 e a restrição 2:
- 1x + 2y = 240.000
- 1,5x + 1y = 180.000

- Resolvendo o sistema de equações:
# 1x + 2y = 240.000
# 1,5x + 1y = 180.000
# Multiplicando a segunda equação por 2:
# 3x + 2y = 360.000
# Subtraindo a primeira equação da segunda:
# 3x + 2y - 1x - 2y = 360.000 - 240.000
# 2x = 120.000
# x = 60.000
# Substituindo x = 60.000 na primeira equação:
# 1(60.000) + 2y = 240.000
# 60.000 + 2y = 240.000
# 2y = 240.000 - 60.000
# 2y = 180.000
# y = 90.000
# Verificando se a solução é viável:
# 1(60.000) + 2(90.000) = 60.000 + 180.000 = 240.000 (satisfaz a restrição de cereal)
# 1,5(60.000) + 1(90.000) = 90.000 + 90.000 = 180.000 (satisfaz a restrição de carne)
# Portanto, a solução é viável e é um vértice da região factível.
# Temos a interseção (60.000, 90.000) [vértice C]

Interseção entre a restrição 1 e a restrição 3:
# 1x + 2y = 240.000
# x = 110.000
# Substituindo x = 110.000 na primeira equação:
# 1(110.000) + 2y = 240.000
# 110.000 + 2y = 240.000
# 2y = 240.000 - 110.000
# 2y = 130.000
# y = 65.000
# Verificando se a solução é viável:
# 1(110.000) + 2(65.000) = 110.000 + 130.000 = 240.000 (satisfaz a restrição de cereal)
# 1,5(110.000) + 1(65.000) = 165.000 + 65.000 = 230.000 (viola a restrição de carne, 230.000 > 180.000)
# Portanto, a solução não é viável.

Interseção entre a restrição 2 e a restrição 3:
# 1,5x + 1y = 180.000
# x = 110.000
# Substituindo x = 110.000 na primeira equação:
# 1,5(110.000) + 1y = 180.000
# 165.000 + 1y = 180.000
# 1y = 180.000 - 165.000
# 1y = 15.000
# y = 15.000
# Verificando se a solução é viável:
# 1(110.000) + 2(15.000) = 110.000 + 30.000 = 140.000 (satisfaz a restrição de cereal)
# 1,5(110.000) + 1(15.000) = 165.000 + 15.000 = 180.000 (satisfaz a restrição de carne)
# Portanto, a solução é viável e é um vértice da região factível.
# Temos a interseção (110.000, 15.000) [vértice D]

Os vértices da região factível são encontrados nas interseções das restrições:
- (0, 0): origem
- (110.000, 0): restrições x ≤ 110.000 e y = 0
- (110.000, 15.000): interseção das linhas x = 110.000 e 1,5x + 1y = 180.000
- (60.000, 90.000): interseção das linhas 1x + 2y = 240.000 e 1,5x + 1y = 180.000
- (0, 120.000): restrições x = 0 e 1x + 2y = 240.000

Para encontrar o valor máximo da função objetivo 1,60x + 1,40y, podemos avaliar cada vértice:

- Em (0,0): 1,60(0) + 1,40(0) = 0
- Em (110.000,0): 1,60(110.000) + 1,40(0) = 176.000
- Em (110.000,15.000): 1,60(110.000) + 1,40(15.000) = 176.000 + 21.000 = 197.000
- Em (60.000,90.000): 1,60(60.000) + 1,40(90.000) = 96.000 + 126.000 = 222.000
- Em (0,120.000): 1,60(0) + 1,40(120.000) = 168.000

O valor máximo da função objetivo é 222.000, alcançado no ponto (60.000, 90.000).
Portanto, a solução ótima é:
- x = 60.000 pacotes de Viralata's
- y = 90.000 pacotes de Ração do Sucesso
- Lucro máximo = $222.000
"""

# Implementação da solução com Python e verificação usando scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


# Plotar a região factível
def plot_constraint(x, expr, label):
    plt.plot(x, expr, label=label)


# Configuração do gráfico
plt.figure(figsize=(12, 9))
plt.grid(True)
plt.axhline(y=0, color="k", linestyle="-", alpha=0.3)
plt.axvline(x=0, color="k", linestyle="-", alpha=0.3)

# Para melhorar a visualização, usaremos unidades de milhares
units_scale = 1000
x_label = "Pacotes de Viralata's (em milhares)"
y_label = "Pacotes de Ração do Sucesso (em milhares)"

# Definir limites para melhor visualização
x_range = np.linspace(0, 120, 1000) / units_scale

# Plotando as restrições
plot_constraint(
    x_range,
    (240000 - x_range * units_scale) / (2 * units_scale),
    "1x + 2y ≤ 240.000 (Cereal)",
)
plot_constraint(
    x_range,
    (180000 - 1.5 * x_range * units_scale) / units_scale,
    "1,5x + 1y ≤ 180.000 (Carne)",
)
plt.axvline(
    x=110 / units_scale, color="r", linestyle="-", label="x ≤ 110.000 (Capacidade)"
)
plt.axhline(y=0, color="g", linestyle="-", label="y ≥ 0")

# Os vértices identificados no problema (em unidades de milhares para o gráfico)
vertices = [
    (0, 0),  # Origem
    (110 / units_scale, 0),  # Restrições x ≤ 110.000 e y = 0
    (110 / units_scale, 15 / units_scale),  # x = 110.000 e 1,5x + 1y = 180.000
    (60 / units_scale, 90 / units_scale),  # 1x + 2y = 240.000 e 1,5x + 1y = 180.000
    (0, 120 / units_scale),  # x = 0 e 1x + 2y = 240.000
]

# Sombreando a região factível
# Primeiro precisamos determinar o polígono que representa a região factível
x_vertices = [v[0] for v in vertices]
y_vertices = [v[1] for v in vertices]
plt.fill(x_vertices, y_vertices, alpha=0.2, color="blue")

# Marcando os vértices
plt.scatter(x_vertices, y_vertices, c="red", s=100, zorder=5)

# Adicionando os valores da função objetivo para cada vértice
for i, v in enumerate(vertices):
    obj_value = 1.60 * v[0] * units_scale + 1.40 * v[1] * units_scale
    label = f"({int(v[0]*units_scale)}, {int(v[1]*units_scale)})\nf={obj_value:.1f}"
    plt.annotate(
        label,
        (v[0], v[1]),
        xytext=(10, 10),
        textcoords="offset points",
    )

# Plotando alguns contornos da função objetivo
for z in [0, 50000, 100000, 150000, 200000]:
    # 1,60x + 1,40y = z => y = (z - 1,60x)/1,40
    y_obj = (z - 1.60 * x_range * units_scale) / (1.40 * units_scale)
    plt.plot(x_range, y_obj, "k--", alpha=0.5)
    plt.annotate(
        f"f = {z}", (x_range[-1], y_obj[-1]), xytext=(10, 0), textcoords="offset points"
    )

# Solução usando scipy.optimize.linprog
# Forma padrão para linprog (minimização): min c^T x sujeito a A_ub x <= b_ub e A_eq x = b_eq
# Como queremos maximizar 1,60x + 1,40y, vamos minimizar -1,60x - 1,40y
c = [-1.60, -1.40]  # Coeficientes da função objetivo (negativo para maximização)

# Restrições de desigualdade na forma A_ub x <= b_ub
A_ub = [
    [1, 2],  # 1x + 2y <= 240.000 (restrição de cereal)
    [1.5, 1],  # 1,5x + 1y <= 180.000 (restrição de carne)
    [1, 0],  # x <= 110.000 (restrição de capacidade)
]
b_ub = [240000, 180000, 110000]

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
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend(loc="upper right")
plt.xlim(-5 / units_scale, 120 / units_scale)
plt.ylim(-5 / units_scale, 130 / units_scale)
plt.tight_layout()

# Destacar a solução ótima
plt.scatter(
    [optimal_x[0] / units_scale],
    [optimal_x[1] / units_scale],
    c="green",
    s=200,
    marker="*",
    zorder=6,
)
plt.annotate(
    "Solução Ótima",
    (optimal_x[0] / units_scale, optimal_x[1] / units_scale),
    xytext=(20, 20),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->"),
)

plt.savefig("programacao_linear_q7.png")
plt.show()

# Gráfico 3D da função objetivo
from mpl_toolkits.mplot3d import Axes3D

# Intervalo para x e y em milhares
x_vals = np.linspace(0, 120, 200)  # 0 a 120 mil
y_vals = np.linspace(0, 130, 200)
X, Y = np.meshgrid(x_vals, y_vals)

# Avaliar as restrições
cereal_limit = X + 2 * Y <= 240  # x + 2y <= 240.000
carne_limit = 1.5 * X + Y <= 180  # 1.5x + y <= 180.000
capacity_limit = X <= 110  # x <= 110.000
valid_region = cereal_limit & carne_limit & capacity_limit

# Z = lucro (em milhares de reais)
Z = np.where(valid_region, 1.60 * X + 1.40 * Y, np.nan)

# Plotando
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

# Superfície válida
ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="k", alpha=0.8)

# Destacar o ponto ótimo
ax.scatter(
    optimal_x[0] / units_scale,
    optimal_x[1] / units_scale,
    optimal_value / units_scale,
    color="red",
    s=100,
    label="Solução Ótima",
)

# Configurações dos eixos
ax.set_xlabel("Viralata's (mil)")
ax.set_ylabel("Ração do Sucesso (mil)")
ax.set_zlabel("Lucro (mil R$)")
ax.set_title("Superfície de Lucro Z = 1.60x + 1.40y")
ax.legend()
plt.tight_layout()
plt.savefig("lucro_superficie_3d.png")
plt.show()

# Exibir o resultado
print("Solução teórica:")
print("Vértice ótimo: (60.000, 90.000)")
print("Valor ótimo: 222.000")
print("\nSolução computacional:")
print(f"Vértice ótimo: ({optimal_x[0]:.6f}, {optimal_x[1]:.6f})")
print(f"Valor ótimo: {optimal_value:.6f}")
