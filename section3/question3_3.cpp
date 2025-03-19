#include <iostream>
#include <vector>
#include <unordered_set>
#include <utility>
#include <algorithm>

using namespace std;

/*
    1: procedure TOURNAMENT_SEQUENCE(teams, results)
    2:     if teams.size() <= 1 then
    3:         return teams
    4:     end if
    5:
    6:     pivot ← teams[0]
    7:     winners ← []
    8:     losers ← []
    9:
    10:     for i ← 1 → teams.size() - 1 do
    11:         team ← teams[i]
    12:         if BEATS(team, pivot, results) then
    13:             winners.append(team)
    14:         else
    15:             losers.append(team)
    16:         end if
    17:     end for
    18:
    19:     winners_ordering ← TOURNAMENT_SEQUENCE(winners, results)
    20:     losers_ordering ← TOURNAMENT_SEQUENCE(losers, results)
    21:
    22:     return winners_ordering + [pivot] + losers_ordering
    23: end procedure
    24:
    25: procedure BEATS(team1, team2, results)
    26:     for each result in results do
    27:         if result.first = team1 AND result.second = team2 then
    28:             return true
    29:         end if
    30:     end for
    31:     return false
    32: end procedure
*/

// Função para verificar se o time1 vence o time2 com base nos resultados
bool beats(int team1, int team2, const vector<pair<int, int>> &results)
{
    for (const auto &result : results)
    {
        if (result.first == team1 && result.second == team2)
        {
            return true;
        }
    }
    return false;
}

// Função de divisão e conquista para encontrar a ordem do torneio
vector<int> tournament_sequence(const vector<int> &teams, const vector<pair<int, int>> &results)
{
    // Base case
    if (teams.size() <= 1)
    {
        return teams;
    }

    // Escolhemos o primeiro time como pivô (a1)
    int pivot = teams[0];
    vector<int> winners;
    vector<int> losers;

    // Dividimos os times em vencedores (que venceram o pivô) e perdedores (que perderam para o pivô)
    for (size_t i = 1; i < teams.size(); i++)
    {
        int team = teams[i];
        if (beats(team, pivot, results))
        {
            winners.push_back(team);
        }
        else
        {
            losers.push_back(team);
        }
    }

    // Resolvemos recursivamente para vencedores e perdedores
    vector<int> winners_ordering = tournament_sequence(winners, results);
    vector<int> losers_ordering = tournament_sequence(losers, results);

    // Combinamos os resultados
    vector<int> ordering;
    ordering.insert(ordering.end(), winners_ordering.begin(), winners_ordering.end());
    ordering.push_back(pivot);
    ordering.insert(ordering.end(), losers_ordering.begin(), losers_ordering.end());

    return ordering;
}

int main()
{
    // Input de exemplo
    vector<pair<int, int>> results = {
        {1, 2}, {2, 4}, {2, 3}, {3, 1}, {4, 3}, {4, 1}};

    // Extrai os times únicos do conjunto de resultados para obter a lista de times
    unordered_set<int> team_set;
    for (const auto &result : results)
    {
        team_set.insert(result.first);
        team_set.insert(result.second);
    }
    vector<int> teams(team_set.begin(), team_set.end());

    // Obtemos a ordem do torneio
    vector<int> ordering = tournament_sequence(teams, results);

    // Resultado
    cout << "Ordenação do Torneio: ";
    for (size_t i = 0; i < ordering.size(); i++)
    {
        cout << ordering[i];
        if (i < ordering.size() - 1)
        {
            cout << " -> ";
        }
    }
    cout << endl;

    // Verifica se a sequência é possível
    bool valid = true;
    for (size_t i = 0; i < ordering.size() - 1; i++)
    {
        if (!beats(ordering[i], ordering[i + 1], results))
        {
            valid = false;
            cout << "Sequência inválida: " << ordering[i] << " não bate com " << ordering[i + 1] << endl;
        }
    }

    if (valid)
    {
        cout << "A sequência fornecida é válida!" << endl;
    }

    return 0;
}