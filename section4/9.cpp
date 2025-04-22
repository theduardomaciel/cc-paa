#include <iostream>
#include <vector>
#include <algorithm>

/*
Função MINIMUM_WEIGHT_FEEDBACK_EDGE_SET(V, E):
    // Inverte os pesos de todas as arestas
    Para cada aresta em E:
        aresta.peso = -aresta.peso

    // Executa o algoritmo de Kruskal com os pesos invertidos
    // O Kruskal vai utilizar as arestas de menor peso que, por serem previamente negadas,
    // construirá uma AGM com as arestas de maior peso
    arvoreExpansaoMinima = KRUSKAL(V, E)

    // Inicializa a solução com todas as arestas
    solucao = E

    // Remove da solução as arestas presentes na árvore de expansão mínima
    Para cada aresta em arvoreExpansaoMinima:
        solucao.remove(aresta)

    // Retorna o conjunto feedback de peso mínimo
    // (complemento da AGM, cujos pesos das arestas são os máximos)
    Retorna solucao
*/

struct Edge
{
    int u, v;
    int weight;

    Edge(int _u, int _v, int _weight) : u(_u), v(_v), weight(_weight) {}

    bool operator<(const Edge &other) const
    {
        return weight < other.weight;
    }
};

class DisjointSet
{
private:
    std::vector<int> parent, rank;

public:
    DisjointSet(int n)
    {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x)
    {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY)
            return;

        if (rank[rootX] < rank[rootY])
            parent[rootX] = rootY;
        else
        {
            parent[rootY] = rootX;
            if (rank[rootX] == rank[rootY])
                rank[rootX]++;
        }
    }
};

std::vector<Edge> kruskal(int V, std::vector<Edge> &edges)
{
    std::sort(edges.begin(), edges.end());

    DisjointSet ds(V);
    std::vector<Edge> mst;

    for (const Edge &edge : edges)
    {
        int u = edge.u;
        int v = edge.v;

        int rootU = ds.find(u);
        int rootV = ds.find(v);

        if (rootU != rootV)
        {
            mst.push_back(edge);
            ds.unite(u, v);
        }
    }

    return mst;
}

std::vector<Edge> minimum_weight_feedback_edge_set(int V, std::vector<Edge> &edges)
{
    // Inverte os pesos das arestas
    for (Edge &edge : edges)
    {
        edge.weight = -edge.weight;
    }

    // Executa o algoritmo de Kruskal com os pesos invertidos
    std::vector<Edge> minSpanTree = kruskal(V, edges);

    // Restaura os pesos originais das arestas
    for (Edge &edge : edges)
    {
        edge.weight = -edge.weight;
    }
    for (Edge &edge : minSpanTree)
    {
        edge.weight = -edge.weight;
    }

    // Cria uma cópia de todas as arestas
    std::vector<Edge> solution = edges;

    // Remove da solução as arestas contidas na árvore de expansão mínima
    for (const Edge &mstEdge : minSpanTree)
    {
        solution.erase(
            std::remove_if(solution.begin(), solution.end(),
                           [&mstEdge](const Edge &e)
                           {
                               return (e.u == mstEdge.u && e.v == mstEdge.v) ||
                                      (e.u == mstEdge.v && e.v == mstEdge.u);
                           }),
            solution.end());
    }

    return solution;
}

// Exemplo de uso
int main()
{
    int V = 4; // Número de vértices
    std::vector<Edge> edges = {
        Edge(0, 1, 1),
        Edge(1, 2, 2),
        Edge(2, 3, 3),
        Edge(3, 0, 4),
        Edge(0, 2, 5)};

    std::vector<Edge> result = minimum_weight_feedback_edge_set(V, edges);

    std::cout << "Conjunto feedback de arestas de peso mínimo:" << std::endl;
    for (const Edge &edge : result)
    {
        std::cout << "(" << edge.u << ", " << edge.v << ") com peso " << edge.weight << std::endl;
    }

    return 0;
}