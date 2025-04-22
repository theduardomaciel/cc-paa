#include <iostream>
#include <vector>

using namespace std;

// Função para encontrar o número ausente
int find_missing(const vector<int> &A, int n)
{
    int expected_sum = (n * (n + 1)) / 2; // Soma esperada dos primeiros n números
    int actual_sum = 0;

    // Calcula a soma dos elementos do array
    for (int num : A)
    {
        actual_sum += num;
    }

    return expected_sum - actual_sum; // O número ausente
}

int main()
{
    // Exemplo: n = 5, mas o array contém apenas 4 números ordenados
    vector<int> A = {1, 2, 3, 5}; // Número 4 está ausente
    int n = 5;

    int missing_number = find_missing(A, n);
    cout << "O número ausente é: " << missing_number << endl;

    return 0;
}
