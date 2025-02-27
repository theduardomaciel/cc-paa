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
    if (n < 2)
    {
        return n;
    }

    unsigned long long prev = 0, curr = 1, next;
    for (int i = 2; i <= n; ++i)
    {
        next = prev + curr;
        prev = curr;
        curr = next;
    }

    return curr;
}

int main()
{
    // Vetores para armazenar os valores de n e seus respectivos tempos de execução (t)
    vector<double> n_recursive, t_recursive;
    vector<double> n_iterative, t_iterative;

    // Realiza o benchmark da função Fibonacci recursiva.
    // Loop até que uma chamada leve 5 segundos ou mais.
    for (int n = 1;; n++)
    {
        auto start = steady_clock::now();
        recursive_fibonacci(n);
        auto end = steady_clock::now();
        double elapsed = duration_cast<duration<double>>(end - start).count();

        // Se o tempo de execução for 5 segundos ou mais, interrompe o loop.
        if (elapsed >= 60.0)
            break;

        n_recursive.push_back(n);
        t_recursive.push_back(elapsed);
        cout << "Recursivo: n = " << n << " levou " << elapsed << " segundos." << endl;
    }

    cout << "Recursivo: n = " << n_recursive.size() << " valores avaliados." << endl;

    // Realiza o benchmark da função Fibonacci iterativa.
    // Embora esta função seja rápida, definimos um limite máximo para evitar um loop infinito.
    const int max_iterative_n = 1000000;
    auto total_start = steady_clock::now();
    for (int n = 1; n <= max_iterative_n; n++)
    {
        auto start = steady_clock::now();

        iterative_fibonacci(n);
        auto end = steady_clock::now();
        double elapsed = duration_cast<duration<double>>(end - start).count();
        double total_elapsed = duration_cast<duration<double>>(end - total_start).count();

        // Se o tempo de execução for 5 segundos ou mais, interrompe o loop.
        if (total_elapsed >= 60.0)
            break;

        n_iterative.push_back(n);
        t_iterative.push_back(elapsed);

        // Opcional: imprime progresso a cada 1.000.000 iterações
        if (n % 10000 == 0)
            cout << "Iterativo: n = " << n << " levou " << elapsed << " segundos." << endl;
    }

    cout << "Iterativo: n = " << n_iterative.size() << " valores avaliados." << endl;

    // Plotando os resultados em um único gráfico
    auto ax = matplot::gca(); // Pega o eixo atual
    matplot::plot(ax, n_recursive, t_recursive, "r-", "LineWidth", 2, "DisplayName", "Recursivo");
    matplot::hold(ax, true); // Mantém o gráfico atual para adicionar o próximo plot
    matplot::plot(ax, n_iterative, t_iterative, "b-", "LineWidth", 2, "DisplayName", "Iterativo");

    matplot::xlabel(ax, "n");
    matplot::ylabel(ax, "Tempo (s)");
    matplot::title(ax, "Benchmark Fibonacci: Recursivo vs Iterativo");
    matplot::legend(ax); // Exibe a legenda para diferenciar as curvas

    matplot::show();

    // Espera pelo input do usuário para manter o programa rodando
    std::cin.get();

    return 0;
}
