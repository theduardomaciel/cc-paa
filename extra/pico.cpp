#include <iostream>
#include <vector>

/*
função encontrarPicoRec(A, low, high):
    se low == high então:
        retorne low

    mid ← ⌊(low + high) / 2⌋

    se A[mid] < A[mid + 1] então:
        retorne encontrarPicoRec(A, mid + 1, high)
    senão:
        retorne encontrarPicoRec(A, low, mid)

função encontrarPico(A, n):
    retorne encontrarPicoRec(A, 1, n)

*/

using namespace std;

int encontrarPicoRec(const vector<int> &A, int inicio, int fim)
{
    if (inicio == fim)
        return inicio; // Caso base: um único elemento é o pico

    int mid = (inicio + fim) / 2;

    if (A[mid] < A[mid + 1])
    {
        // O pico está à direita
        return encontrarPicoRec(A, mid + 1, fim);
    }
    else
    {
        // O pico está à esquerda ou é o próprio mid
        return encontrarPicoRec(A, inicio, mid);
    }
}

int encontrarPico(const vector<int> &A)
{
    return encontrarPicoRec(A, 0, A.size() - 1);
}

int main()
{
    vector<int> A = {1, 3, 7, 12, 14, 10, 6, 2};
    int indicePico = encontrarPico(A);
    cout << "O índice do pico é: " << indicePico << " e o valor é " << A[indicePico] << endl;
    return 0;
}
