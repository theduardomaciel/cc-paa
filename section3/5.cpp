#include <iostream>
#include <vector>
#include <algorithm>

/*
    São dadas duas listas ordenadas de tamanho m e n.
    Dê um algoritmo de tempo $O(log m + log n)$ para computar o k-ésimo menor elemento da união das duas listas.

    1: procedure FIND_KTH_ELEMENT(A, B, k)
    2:      m ← tamanho de A
    3:      n ← tamanho de B
    4:      if m > n then
    5:          return FIND_KTH_ELEMENT(B, A, k)
    6:      end if
    7:      if m = 0 then
    8:          return B[k-1]
    9:      end if
    10:     if k = 1 then
    11:         return min(A[0], B[0])
    12:     end if
    13:     i ← min(m, ⌊k/2⌋)
    14:     j ← min(n, ⌊k/2⌋)
    15:     if A[i-1] > B[j-1] then
    16:         return FIND_KTH_ELEMENT(A, B[j:n], k-j)
    17:     else
    18:         return FIND_KTH_ELEMENT(A[i:m], B, k-i)
    19:     end if
    20: end procedure
*/

// Função para encontrar o k-ésimo elemento menor na união de duas listas ordenadas
// Complexidade: O(log m + log n)
int findKthElement(const std::vector<int> &A, const std::vector<int> &B, int k)
{
    // Garante que A é a menor lista para simplificar o algoritmo
    if (A.size() > B.size())
    {
        return findKthElement(B, A, k);
    }

    // Caso base: se A está vazia, o k-ésimo elemento está em B
    if (A.empty())
    {
        return B[k - 1];
    }

    // Caso base: se k=1, retorne o menor elemento entre os primeiros elementos
    if (k == 1)
    {
        return std::min(A[0], B[0]);
    }

    // Escolha i elementos de A e j elementos de B
    int i = std::min(static_cast<int>(A.size()), k / 2);
    int j = std::min(static_cast<int>(B.size()), k / 2);

    // Se A[i-1] > B[j-1], então B[j-1] não pode ser o k-ésimo elemento
    // Podemos descartar os primeiros j elementos de B
    if (A[i - 1] > B[j - 1])
    {
        // Cria um novo vetor B começando do índice j
        std::vector<int> newB(B.begin() + j, B.end());
        return findKthElement(A, newB, k - j);
    }
    // Caso contrário, A[i-1] não pode ser o k-ésimo elemento
    else
    {
        // Cria um novo vetor A começando do índice i
        std::vector<int> newA(A.begin() + i, A.end());
        return findKthElement(newA, B, k - i);
    }
}

// Versão otimizada que não cria novos vetores a cada chamada recursiva
int findKthElementOptimized(const std::vector<int> &A, const std::vector<int> &B,
                            int startA, int endA, int startB, int endB, int k)
{
    // Garante que o intervalo A é menor que o intervalo B
    if (endA - startA > endB - startB)
    {
        return findKthElementOptimized(B, A, startB, endB, startA, endA, k);
    }

    // Se A está vazio, retorne o k-ésimo elemento de B
    if (startA >= endA)
    {
        return B[startB + k - 1];
    }

    // Se k=1, retorne o menor elemento
    if (k == 1)
    {
        return std::min(A[startA], B[startB]);
    }

    // Escolha i elementos de A e j elementos de B
    int i = std::min(endA - startA, k / 2);
    int j = std::min(endB - startB, k / 2);

    if (A[startA + i - 1] > B[startB + j - 1])
    {
        // Descarta os primeiros j elementos de B
        return findKthElementOptimized(A, B, startA, endA, startB + j, endB, k - j);
    }
    else
    {
        // Descarta os primeiros i elementos de A
        return findKthElementOptimized(A, B, startA + i, endA, startB, endB, k - i);
    }
}

// Função principal para chamar a versão otimizada
int findKthElementMain(const std::vector<int> &A, const std::vector<int> &B, int k)
{
    return findKthElementOptimized(A, B, 0, A.size(), 0, B.size(), k);
}

int main()
{
    std::vector<int> A = {2, 3, 6, 7, 9};
    std::vector<int> B = {1, 4, 8, 10};
    int k = 5;

    // Encontrando o k-ésimo elemento
    std::cout << "O " << k << "-ésimo elemento é: " << findKthElementMain(A, B, k) << std::endl;

    return 0;
}