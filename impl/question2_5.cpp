#include <iostream>

#include <cmath>

// Complexidade: O(2^n) - Exponencial
int recursive_fibonacci(int n)
{
    if (n < 2)
    {
        return n;
    }

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
}

// Complexidade: O(n) - Linear
int iterative_fibonacci(int n)
{
    if (n < 2)
    {
        return n;
    }

    int prev = 0, curr = 1;
    for (int i = 2; i <= n; ++i)
    {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }

    return curr;
}

int main()
{
    int n;
    std::cout << "Insira a posição da sequência de Fibonnaci: ";
    std::cin >> n;

    int result = iterative_fibonacci(n);
    std::cout << "Nº de Fibonacci na posição " << n << " é " << result << std::endl;

    return 0;
}