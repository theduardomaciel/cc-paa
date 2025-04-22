#include <iostream>
#include <vector>

/*
1: procedure FIXED_POINT(A, low, high)
2:   if low > high then
3:       return false
4:   mid ← floor((low + high) / 2)
5:   if A[mid] = mid then
6:       return true
7:   else if A[mid] < mid then
8:       return FIXED_POINT(A, mid + 1, high)
9:   else
10:      return FIXED_POINT(A, low, mid - 1)
11:  end if
12: end procedure
*/

bool fixed_point(const std::vector<int> &A, int low, int high)
{
    if (low > high)
    {
        return false;
    }

    int mid = (low + high) / 2;

    if (A[mid] == mid)
    {
        return true;
    }
    else if (A[mid] < mid)
    {
        return fixed_point(A, mid + 1, high);
    }
    else
    {
        return fixed_point(A, low, mid - 1);
    }
}

// Função auxiliar para chamar o algoritmo inicial
bool has_fixed_point(const std::vector<int> &A)
{
    return fixed_point(A, 0, A.size() - 1);
}

int main()
{
    // Exemplo 1: Vetor com ponto fixo
    std::vector<int> A1 = {-3, -1, 1, 3, 5, 7};
    std::cout << "Exemplo 1: " << (has_fixed_point(A1) ? "Tem ponto fixo" : "Não tem ponto fixo") << std::endl;

    // Exemplo 2: Vetor sem ponto fixo
    std::vector<int> A2 = {-2, 0, 1, 4, 6, 8};
    std::cout << "Exemplo 2: " << (has_fixed_point(A2) ? "Tem ponto fixo" : "Não tem ponto fixo") << std::endl;

    // Exemplo 3: Vetor com ponto fixo
    std::vector<int> A3 = {-1, 0, 1, 2, 4, 10};
    std::cout << "Exemplo 3: " << (has_fixed_point(A3) ? "Tem ponto fixo" : "Não tem ponto fixo") << std::endl;

    return 0;
}