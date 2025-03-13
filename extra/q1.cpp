#include <iostream>
#include <vector>

using namespace std;

/*
    Função ContaElementosUnicos(A, max_valor):
        // Inicializa vetor de frequência com zeros
        Frequencia[0...max_valor] ← 0

        // Primeiro loop: conta frequência de cada elemento
        Para cada elemento em A faça:
            Frequencia[elemento] ← Frequencia[elemento] + 1

        // Inicializa contador
        contador ← 0

        // Segundo loop: conta elementos que aparecem uma única vez
        Para i de 0 até max_valor faça:
            Se Frequencia[i] = 1 então:
                contador ← contador + 1

        Retorna contador
*/

// Algoritmo que calcula a quantidade de elementos que aparecem apenas uma vez
void algorithm(const std::vector<int> &A, int max_value)
{
    // Cria um vetor de frequência com o tamanho máximo
    std::vector<int> frequency(max_value + 1, 0);

    // Preenche o vetor de frequência
    for (int num : A)
    {
        frequency[num]++;
    }

    // Contador de elementos que aparecem apenas uma vez
    int count = 0;

    // Itera sobre o vetor de frequência
    for (int i = 0; i < frequency.size(); i++)
    {
        // Se o elemento aparece apenas uma vez, incrementa o contador
        if (frequency[i] == 1)
        {
            count++;
        }
    }

    // Exibe o resultado
    std::cout << "Quantidade de elementos que aparecem apenas uma vez: " << count << std::endl;
}

int main()
{
    std::vector<int> example_vector = {1, 2, 3, 2, 4, 5, 6, 5};
    int d = 6;

    algorithm(example_vector, d);

    return 0;
}