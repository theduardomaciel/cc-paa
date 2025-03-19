#include <iostream>
using namespace std;

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
    12:         end if
    13:         i ← min(m, ⌊k/2⌋)
    14:         j ← min(n, ⌊k/2⌋)
    15:         if A[i-1] > B[j-1] then
    16:         return FIND_KTH_ELEMENT(A, B[j:n], k-j)
    17:         else
    18:         return FIND_KTH_ELEMENT(A[i:m], B, k-i)
    19:     end if
    20: end procedure
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Função para encontrar o k-ésimo elemento da união de duas listas ordenadas
int findKthElement(vector<int> &A, int startA, int m,
                   vector<int> &B, int startB, int n, int k)
{
    // Se a primeira lista está vazia, retorna o k-ésimo elemento da segunda lista
    if (m == 0)
        return B[startB + k - 1];

    // Se a segunda lista está vazia, retorna o k-ésimo elemento da primeira lista
    if (n == 0)
        return A[startA + k - 1];

    // Se k = 1, retorna o menor elemento entre os primeiros elementos das duas listas
    if (k == 1)
        return min(A[startA], B[startB]);

    // Determina o número de elementos a serem descartados em cada lista
    int i = min(m, k / 2);
    int j = min(n, k / 2);

    // Compara os elementos no meio das sublistas
    if (A[startA + i - 1] > B[startB + j - 1])
    {
        // Descarta os j menores elementos da lista B
        return findKthElement(A, startA, m, B, startB + j, n - j, k - j);
    }
    else
    {
        // Descarta os i menores elementos da lista A
        return findKthElement(A, startA + i, m - i, B, startB, n, k - i);
    }
}

// Função wrapper para simplificar a chamada inicial
int findKthElement(vector<int> &A, vector<int> &B, int k)
{
    int m = A.size();
    int n = B.size();

    // Garante que A é a menor lista para otimizar
    if (m > n)
        return findKthElement(B, 0, n, A, 0, m, k);

    return findKthElement(A, 0, m, B, 0, n, k);
}

/*
1  →  2
  ↖ ↙ ↓
3  ←  4
*/

// Helper function that uses indices to represent the current subarray
int findKthElement(const vector<int> &A, int startA, const vector<int> &B, int startB, int k)
{
    int m = A.size() - startA;
    int n = B.size() - startB;

    // Ensure that A is the smaller array
    if (m > n)
        return findKthElement(B, startB, A, startA, k);

    // If A is empty, return kth element from B
    if (m == 0)
        return B[startB + k - 1];

    // If k is 1, return the minimum of the first elements of the subarrays
    if (k == 1)
        return min(A[startA], B[startB]);

    // Determine the number of elements to compare in A and B respectively
    int i = min(m, k / 2);
    int j = min(n, k / 2);

    // Discard i or j elements based on the comparison
    if (A[startA + i - 1] > B[startB + j - 1])
        // B's first j elements are too small
        return findKthElement(A, startA, B, startB + j, k - j);
    else
        // A's first i elements are too small
        return findKthElement(A, startA + i, B, startB, k - i);
}

// Overloaded function for easier usage without initial indices
int findKthElement(const vector<int> &A, const vector<int> &B, int k)
{
    return findKthElement(A, 0, B, 0, k);
}

int main()
{
    // Exemplo de uso
    vector<int> A = {2, 3, 6, 7, 9};
    vector<int> B = {1, 4, 8, 10};
    int k = 5;

    cout << "O " << k << "-ésimo menor elemento é: " << findKthElement(A, B, k) << endl;

    return 0;
}
