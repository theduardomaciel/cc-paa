#include <iostream>
#include <vector>

using namespace std;

/*
    Imprime uma régua de ordem n no intervalo [0..2n ].
    O “traço” no ponto médio da régua deve ter comprimento n,
    os traços nos pontos médios dos subintervalos superior e inferior
    devem ter comprimento n − 1, e assim por diante.
*/

/*
    0 .
    1 . -
    2 . --
    3 . -
    4 . ---
    5 . -
    6 . --
    7 . -
    8 . ----
    9 . -
    10 . --
    11 . -
    12 . ---
    13 . -
    14 . --
    15 . -
    16 .
*/

void printRuler(int n)
{
    if (n == 0)
    {
        return;
    }
    printRuler(n - 1); // imprime a régua de ordem n-1

    cout << ". "; // imprime o ponto que antecede as réguas
    for (int i = 0; i < n; i++)
    {
        cout << "-";
    }
    cout << endl;
    /* cout << string(n, '-') << endl; // imprime o traço do meio */

    printRuler(n - 1); // imprime a régua de ordem n-1
}

int main()
{
    int n = 2;
    cout << "Régua de tamanho " << n << endl;
    cout << "." << endl;
    printRuler(n);
    cout << "." << endl;
    return 0;
}