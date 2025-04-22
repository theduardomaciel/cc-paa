#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
function hasPerfectMatching(tree):
    if tree has odd number of nodes:
        return false

    Create a queue Q to store leaf nodes
    Initialize matching M as empty

    Add all leaf nodes to Q

    while Q is not empty:
        Remove a leaf node u from Q
        Let v be the only neighbor of u

        Add edge (u, v) to matching M
        Remove nodes u and v from tree

        For each neighbor w of v (except u):
            Decrease degree of w by 1
            If degree of w becomes 1:
                Add w to Q

    If all nodes are removed:
        return true
    else:
        return false
*/

// Union-Find data structure for cycle detection
class UnionFind
{
private:
    vector<int> parent, rank;

public:
    UnionFind(int n)
    {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++)
        {
            parent[i] = i;
        }
    }

    int find(int x)
    {
        if (parent[x] != x)
        {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool unionSets(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY)
        {
            return false; // Would create a cycle
        }

        if (rank[rootX] < rank[rootY])
        {
            parent[rootX] = rootY;
        }
        else if (rank[rootX] > rank[rootY])
        {
            parent[rootY] = rootX;
        }
        else
        {
            parent[rootY] = rootX;
            rank[rootX]++;
        }

        return true;
    }
};

// Edge structure
struct Edge
{
    int u, v;
    int weight;

    Edge(int _u, int _v, int _w) : u(_u), v(_v), weight(_w) {}

    bool operator<(const Edge &other) const
    {
        return weight > other.weight; // Sort in descending order
    }
};

// Function to find minimum weight feedback edge set
vector<Edge> minimumWeightFeedbackEdgeSet(int n, vector<Edge> &edges)
{
    // Sort edges in descending order of weight
    sort(edges.begin(), edges.end());

    UnionFind uf(n);
    vector<bool> inSpanningForest(edges.size(), false);

    // Build maximum weight spanning forest
    for (int i = 0; i < edges.size(); i++)
    {
        int u = edges[i].u;
        int v = edges[i].v;

        if (uf.unionSets(u, v))
        {
            inSpanningForest[i] = true;
        }
    }

    // Collect edges not in the spanning forest
    vector<Edge> feedbackEdgeSet;
    for (int i = 0; i < edges.size(); i++)
    {
        if (!inSpanningForest[i])
        {
            feedbackEdgeSet.push_back(edges[i]);
        }
    }

    return feedbackEdgeSet;
}

int main()
{
    // Example graph
    int n = 5; // Number of vertices
    vector<Edge> edges = {
        Edge(0, 1, 1),
        Edge(1, 2, 2),
        Edge(2, 3, 3),
        Edge(3, 0, 4),
        Edge(0, 2, 5)};

    vector<Edge> feedbackEdgeSet = minimumWeightFeedbackEdgeSet(n, edges);

    cout << "Minimum Weight Feedback Edge Set:" << endl;
    int totalWeight = 0;
    for (const Edge &e : feedbackEdgeSet)
    {
        cout << "Edge (" << e.u << ", " << e.v << ") with weight " << e.weight << endl;
        totalWeight += e.weight;
    }
    cout << "Total weight: " << totalWeight << endl;

    return 0;
}