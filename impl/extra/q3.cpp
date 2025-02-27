#include <iostream>
#include <vector>

// Implementação do Algoritmo X
int algoritmoX(const std::vector<int> &A, int inicio, int fim)
{
    // Caso base 1: se início é igual ao fim, retorna o elemento
    if (inicio == fim)
    {
        return A[inicio];
    }

    // Caso base 2: se início é maior que fim, retorna 0
    if (inicio > fim)
    {
        return 0;
    }

    // Cálculo do ponto médio (evitando overflow)
    int meio = inicio + (fim - inicio) / 2;

    // Chamadas recursivas para as duas metades
    int a = algoritmoX(A, inicio, meio);
    int b = algoritmoX(A, meio + 1, fim);

    // Retorna a soma dos resultados
    return a + b;
}

int main()
{
    std::vector<int> vetor = {5, 2, 8, 3, 1, 7, 4};

    // Exibe o vetor original
    std::cout << "Vetor: ";
    for (int num : vetor)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Chama o algoritmo com o vetor completo (índices 0 a n-1)
    int resultado = algoritmoX(vetor, 0, vetor.size() - 1);

    // Exibe o resultado
    std::cout << "Resultado do Algoritmo X: " << resultado << std::endl;

    // Verificação: cálculo da soma diretamente
    int soma = 0;
    for (int num : vetor)
    {
        soma += num;
    }
    std::cout << "Soma dos elementos: " << soma << std::endl;

    return 0;
}