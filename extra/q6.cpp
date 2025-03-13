#include <iostream>
#include <vector>

using namespace std;

// O algoritmo sempre retorna no primeiro loop, pois o return está dentro do loop
/*
    procedure FUNC(inteiro n)
        c ← 0
        for i ← 1 → n do
            j ← 2
            while j < n do
                j ← j * j // j ao quadrado
                c ← c + 1
            end while
            return c
        end for
    end procedure
*/

// Algoritmo que
int algorithm(int n)
{
    int counter = 0;

    for (int i = 1; i <= n; i++)
    {
        int j = 2;

        while (j < n)
        {
            j = j * j;
            counter++;
        }

        return counter;
    }
}

int main()
{
    int n = 5;
    int result = algorithm(n);

    cout << "Resultado: " << result << endl;

    return 0;
}