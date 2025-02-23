#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int a;
    cout << "a: ";
    cin >> a;

    // Vetor para armazenar os valores gerados pelo algoritmo
    // Com ele podemos verificar se a sequência 4, 2, 1 foi gerada
    vector<int> seq;
    seq.push_back(a);

    // Roda enquanto os três últimos valores não forem 4, 2, 1.
    while (seq.size() < 3 || !(seq[seq.size() - 3] == 4 && seq[seq.size() - 2] == 2 && seq[seq.size() - 1] == 1))
    {
        int x = seq.back(); // Valor atual

        // Se x for par, divide por 2; se for ímpar, aplica 3x+1
        if (x % 2 == 0)
        {
            x = x / 2;
        }
        else
        {
            x = 3 * x + 1;
        }

        seq.push_back(x); // Armazena o novo valor na sequência
    }

    cout << "Sequência gerada: ";
    for (int num : seq)
    {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
