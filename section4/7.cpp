#include <iostream>
#include <vector>
#include <utility>

using namespace std;

/*
1: procedure VERIFICAR_RESTRIÇÕES(n, restrições_igualdade, restrições_desigualdade)
2:   UF ← novo UnionFind(n)
3:
4:   for (i, j) in restrições_igualdade do
5:       UF.unir(i, j)
6:   end for
7:
8:   for (i, j) in restrições_desigualdade do
9:       if UF.mesmoConjunto(i, j) then
10:          return FALSO
11:      end if
12:  end for
13:
14:  return VERDADEIRO
15: end procedure
*/

// Estrutura para o algoritmo Union-Find
class UnionFind
{
private:
    vector<int> parent, rank;

public:
    UnionFind(int n)
    {
        parent.resize(n);
        rank.resize(n, 0);

        // Inicialização: cada elemento é seu próprio representante
        for (int i = 0; i < n; i++)
        {
            parent[i] = i;
        }
    }

    // Encontra o representante do conjunto que contém x (com compressão de caminho)
    int find(int x)
    {
        if (parent[x] != x)
        {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Une os conjuntos que contêm x e y (com união por rank)
    void unite(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY)
        {
            return;
        }

        // União por rank: liga a árvore menor à maior
        if (rank[rootX] < rank[rootY])
        {
            parent[rootX] = rootY;
        }
        else
        {
            parent[rootY] = rootX;
            if (rank[rootX] == rank[rootY])
            {
                rank[rootX]++;
            }
        }
    }

    // Verifica se x e y estão no mesmo conjunto
    bool same(int x, int y)
    {
        return find(x) == find(y);
    }
};

// Função principal para verificar se as restrições podem ser satisfeitas
bool checkConstraints(int n,
                      const vector<pair<int, int>> &equalityConstraints,
                      const vector<pair<int, int>> &inequalityConstraints)
{

    UnionFind uf(n);

    // Processo todas as restrições de igualdade
    for (const auto &constraint : equalityConstraints)
    {
        int x = constraint.first;
        int y = constraint.second;
        uf.unite(x, y);
    }

    // Verifico se alguma restrição de desigualdade é violada
    for (const auto &constraint : inequalityConstraints)
    {
        int x = constraint.first;
        int y = constraint.second;

        // Se duas variáveis que deveriam ser diferentes estão no mesmo conjunto,
        // então as restrições não podem ser satisfeitas
        if (uf.same(x, y))
        {
            return false;
        }
    }

    // Se chegamos aqui, todas as restrições podem ser satisfeitas
    return true;
}

int main()
{
    // Exemplo de entrada
    int n = 4; // Número de variáveis: x1, x2, x3, x4

    // Restrições de igualdade (x_i = x_j)
    vector<pair<int, int>> equalityConstraints = {
        {0, 1}, // x1 = x2
        {1, 2}, // x2 = x3
        {2, 3}  // x3 = x4
    };

    // Restrições de desigualdade (x_i ≠ x_j)
    vector<pair<int, int>> inequalityConstraints = {
        {0, 3} // x1 ≠ x4
    };

    // Verificação
    bool result = checkConstraints(n, equalityConstraints, inequalityConstraints);

    if (result)
    {
        cout << "As restrições podem ser satisfeitas." << endl;
    }
    else
    {
        cout << "As restrições não podem ser satisfeitas." << endl;
    }

    return 0;
}