#include <iostream>
#include <vector>

using namespace std;

/*
    Função ContaSubsequenciasCrescentes(A[0..n])
    {
        // Inicializa contador de subsequências
        contador ← 1

        // Inicializa tamanho da subsequência atual
        tamanho ← 1

        // Loop para cada elemento do vetor
        Para i de 1 até n faça:
            // Se o elemento atual é maior que o anterior
            Se A[i] > A[i - 1] então:
                // Incrementa o tamanho da subsequência
                tamanho ← tamanho + 1
            Senão:
                // Incrementa o contador com o número de subsequências possíveis
                contador ← contador + 1

                // Reseta o tamanho da subsequência
                tamanho ← 1

        Retorna contador
    }
*/

// Algoritmo que calcula a quantidade de subsequências de números crescentes no vetor
void algorithm(const std::vector<int> &A)
{
    // Inicializa contador de subsequências
    int count = 1;

    // Inicializa tamanho da subsequência atual
    int size = 1;

    // Loop para cada elemento do vetor
    for (int i = 1; i < A.size(); i++)
    {
        // Se o elemento atual é maior que o anterior
        if (A[i] > A[i - 1])
        {
            // Incrementa o tamanho da subsequência
            size++;
        }
        else
        {
            // Incrementa o contador com o número de subsequências possíveis
            count += 1;

            // Reseta o tamanho da subsequência
            size = 1;
        }
    }

    // Exibe o resultado
    std::cout << "Quantidade de subsequências crescentes: " << count << std::endl;
}

int main()
{
    std::vector<int> example_vector = {1, 2, 2, 3, 4, 1};

    algorithm(example_vector);

    return 0;
}