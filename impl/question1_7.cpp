#include <iostream>
#include <vector>

/*
procedure CONVERSOR D-B (inteiro n)
    t ← n
    k ← 0
    zere todos os bits de b
    while t > 0 do
        k ← k + 1
        b[k] ← t mod 2
        t ← t ÷ 2
    end while
    return b
end procedure
*/

std::vector<int> conversorDB(int n)
{
    int t = n;
    int k = 0;
    std::vector<int> b;

    while (t > 0)
    {
        b.push_back(t % 2);
        t /= 2;
    }

    return b;
}

int main()
{
    int n;
    std::cout << "Digite um número inteiro: ";
    std::cin >> n;

    std::vector<int> binario = conversorDB(n);

    std::cout << "Representação binária (invertida): ";
    for (int bit : binario)
    {
        std::cout << bit;
    }
    std::cout << std::endl;

    // Para exibir na ordem correta
    std::cout << "Representação binária correta: ";
    for (auto it = binario.rbegin(); it != binario.rend(); ++it)
    {
        std::cout << *it;
    }
    std::cout << std::endl;

    return 0;
}
