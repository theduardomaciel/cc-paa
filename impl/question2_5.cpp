#include <iostream>
#include <vector>
#include <chrono>

#include <cmath>
#include <matplot/matplot.h>

using namespace std;
using namespace std::chrono;

// Fibonacci Recursivo
// Complexidade Exponencial -> O(2^n)
unsigned long long recursive_fibonacci(int n)
{
    if (n < 2)
    {
        return n;
    }

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
}

// Fibonacci Iterativo
// Complexidade Linear -> O(n)
unsigned long long iterative_fibonacci(int n)
{
    if (n <= 1)
        return n;
    unsigned long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main()
{
    // Vetores pra armazenar os valores de n e seus respectivos tempos de execução (t)
    vector<double> n_recursive, t_recursive;
    vector<double> n_iterative, t_iterative;

    // Benchmark the recursive Fibonacci function.
    // Loop until a call takes 60 seconds or more.
    for (int n = 1;; n++)
    {
        auto start = steady_clock::now();
        recursive_fibonacci(n);
        auto end = steady_clock::now();
        double elapsed = duration_cast<duration<double>>(end - start).count();

        // If execution time is 60 seconds or more, stop the loop.
        if (elapsed >= 5.0)
            break;

        n_recursive.push_back(n);
        t_recursive.push_back(elapsed);
        cout << "Recursive: n = " << n << " took " << elapsed << " seconds." << endl;
    }

    cout << "Recursive: n = " << n_recursive.size() << " values benchmarked." << endl;

    // Benchmark the iterative Fibonacci function.
    // Although this function is fast, we put an upper limit to avoid an endless loop.
    const int max_iterative_n = 100000000; // adjust this limit if needed
    for (int n = 1; n <= max_iterative_n; n++)
    {
        auto start = steady_clock::now();
        iterative_fibonacci(n);
        auto end = steady_clock::now();
        double elapsed = duration_cast<duration<double>>(end - start).count();

        // If execution time is 60 seconds or more, stop the loop.
        if (elapsed >= 5.0)
            break;

        n_iterative.push_back(n);
        t_iterative.push_back(elapsed);

        // Optional: print progress every 1,000,000 iterations
        if (n % 1000000 == 0)
            cout << "Iterative: n = " << n << " took " << elapsed << " seconds." << endl;
    }

    cout << "Iterative: n = " << n_iterative.size() << " values benchmarked." << endl;

    // Plotando os resultados
    matplot::figure();
    matplot::plot(n_recursive, t_recursive, "r-");
    matplot::xlabel("n");
    matplot::ylabel("Tempo (s)");
    matplot::title("Fibonacci Recursivo");

    matplot::figure();
    matplot::plot(n_iterative, t_iterative, "b-");
    matplot::xlabel("n");
    matplot::ylabel("Tempo (s)");
    matplot::title("Fibonacci Iterativo");

    matplot::show();

    // Esperamos pelo input do usuário pra manter o programa rodando
    std::cin.get();

    return 0;
}