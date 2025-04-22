#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

/*
1: procedure ORDENAÇÃO DE PANQUECAS(array P, int n)
2:   if n ≤ 1 then
3:     return  // Caso base: uma única panqueca já está ordenada
4:   end if
5:
6:   // Encontrar a maior panqueca no array
7:   maiorIndice ← 0
8:   for i ← 1 to n-1 do
9:     if P[i] > P[maiorIndice] then
10:       maiorIndice ← i
11:     end if
12:   end for
13:
14:   if maiorIndice = n-1 then
15:     // A maior panqueca já está na posição correta
16:     ORDENAÇÃO DE PANQUECAS(P, n-1)
17:   else
18:     // Mover a maior panqueca para o topo primeiro (se não estiver lá)
19:     if maiorIndice ≠ 0 then
20:       VIRAR(P, maiorIndice+1)
21:     end if
22:
23:     // Virar toda a pilha para mover a maior panqueca para a base
24:     VIRAR(P, n)
25:
26:     // Ordenar recursivamente o resto da pilha
27:     ORDENAÇÃO DE PANQUECAS(P, n-1)
28:   end if
29: end procedure
30:
31: procedure VIRAR(array P, int k)
32:   // Inverte a ordem dos primeiros k elementos do array
33:   for i ← 0 to ⌊(k-1)/2⌋ do
34:     trocar P[i] com P[k-1-i]
35:   end for
36: end procedure
*/

#include <iostream>
#include <vector>
#include <algorithm>

// Função para virar a pilha de panquecas
void flip(std::vector<int> &pancakes, int k)
{
    // Inverte os primeiros k elementos do array
    for (int i = 0; i < k / 2; i++)
    {
        std::swap(pancakes[i], pancakes[k - 1 - i]);
    }
}

int biggerPancake(std::vector<int> &pancakes, int n)
{
    int bigger = 0;
    for (int i = 1; i < n; i++)
    {
        if (pancakes[i] > pancakes[bigger])
        {
            bigger = i;
        }
    }
    return bigger;
}

// Função principal de ordenação de panquecas usando divisão e conquista
void pancakeSorting(std::vector<int> &pancakes, int n)
{
    // Caso base: uma única panqueca já está ordenada
    if (n == 1)
    {
        return;
    }

    // Encontrar a maior panqueca no array atual
    int biggerIndex = biggerPancake(pancakes, n);

    // Se a maior panqueca já estiver na posição correta (no final)
    if (biggerIndex == n - 1)
    {
        // Apenas ordenar o resto da pilha
        pancakeSorting(pancakes, n - 1);
    }
    else
    {
        // Mover a maior panqueca para o topo primeiro (se não estiver lá)
        if (biggerIndex != 0)
        {
            flip(pancakes, biggerIndex + 1);
        }

        // Virar toda a pilha para mover a maior panqueca para o fim (posição correta)
        flip(pancakes, n);

        // Ordenar recursivamente o resto da pilha
        pancakeSorting(pancakes, n - 1);
    }
}

// Função wrapper para chamar a ordenação
void ordenarPanquecas(std::vector<int> &pancakes)
{
    pancakeSorting(pancakes, pancakes.size());
}

// Função para exibir o array de panquecas
void mostrarPanquecas(const std::vector<int> &pancakes)
{
    std::cout << "Pilha de panquecas: ";
    for (int pancake : pancakes)
    {
        std::cout << pancake << " ";
    }
    std::cout << std::endl;
}

int main()
{
    // Exemplo de uso
    std::vector<int> pilha = {2, 3, 1, 6, 4, 5, 7};

    std::cout << "Pilha original: ";
    mostrarPanquecas(pilha);

    ordenarPanquecas(pilha);

    std::cout << "Pilha ordenada: ";
    mostrarPanquecas(pilha);

    return 0;
}