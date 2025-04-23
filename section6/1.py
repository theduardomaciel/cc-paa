"""
QUESTÃO 1:
Maria aposta com João que ela pode fazer o seguinte truque.

João recitará $$n − 1$$ números diferentes de $$1$$ a $$n$$ em uma ordem aleatória e ela será capaz de nomear o único número nesse intervalo que ele terá perdido.

Claro, ela terá que realizar a tarefa em sua cabeça, sem fazer anotações.

Como ela deve fazer esse truque? Em outras palavras, projete um algoritmo que descubra o número faltante utilizando $$O(1)$$ de espaço em memória.
"""

# Uma forma de usar somente O(1) de espaço em memória é calcular mantendo somente um acumulador
# que armazena a soma dos números de 1 a n e subtrai os números que foram recitados por João.
# A soma dos números de 1 a n é dada pela fórmula S = n*(n+1)/2, onde n é o maior número da sequência.
# A soma dos números recitados é subtraída da soma total, e o resultado é o número que falta.
# A seguir, apresentamos o pseudocódigo e a implementação em Python.

""" 
// Pseudocódigo
entrada: n
S ← n*(n+1)/2
para i = 1 até n−1:
    leia x
    S ← S − x
// aqui S é o número que não foi recitado
imprima S
"""


def find_missing_number(n, numbers):
    # Calculamos a soma esperada dos números de 1 a n usando a fórmula da soma de uma progressão aritmética
    expected_sum = n * (n + 1) // 2
    # o divisor "//" é usado para garantir que a divisão seja inteira, mesmo que n seja um número ímpar

    # Subtraímos a soma dos números fornecidos da soma esperada
    for number in numbers:
        expected_sum -= number

    # O número que falta é o que resta na soma esperada
    return expected_sum


# Testando a função
n = 5
numbers = [1, 2, 3, 5]  # O número 4 está faltando
missing_number = find_missing_number(n, numbers)
print(f"O número faltando é: {missing_number}")  # Saída esperada: 4
