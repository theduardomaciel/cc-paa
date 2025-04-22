#include <iostream>
#include <vector>

using namespace std;

bool searchMatrix(const vector<vector<int>> &matrix, int n, int k, int row, int col)
{
    // Se sair dos limites da matriz, retorna falso
    if (row < 0 || col >= n)
        return false;

    // Se encontrou o elemento, retorna verdadeiro
    if (matrix[row][col] == k)
        return true;

    // Se o elemento atual for maior que k, move para cima
    if (matrix[row][col] > k)
        return searchMatrix(matrix, n, k, row - 1, col);

    // Se o elemento atual for menor que k, move para a direita
    return searchMatrix(matrix, n, k, row, col + 1);
}

bool findElement(const vector<vector<int>> &matrix, int n, int k)
{
    return searchMatrix(matrix, n, k, n - 1, 0); // Começa do canto inferior esquerdo
}

int main()
{
    vector<vector<int>> matrix = {
        {10, 20, 30, 40},
        {15, 25, 35, 45},
        {27, 29, 37, 48},
        {32, 33, 39, 50}};

    int n = matrix.size();
    int key = 29;

    if (findElement(matrix, n, key))
        cout << "Elemento encontrado!" << endl;
    else
        cout << "Elemento não encontrado." << endl;

    return 0;
}