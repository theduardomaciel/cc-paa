#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>
#include <matplot/matplot.h>
using namespace std;
using namespace std::chrono;

// Fibonacci Recursivo - Complexidade Exponencial -> O(2^n)
unsigned long long recursive_fibonacci(int n)
{
    if (n < 2)
    {
        return n;
    }
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
}

// Fibonacci Iterativo - Complexidade Linear -> O(n)
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
    cout << "Executando benchmark Fibonacci recursivo..." << endl;
    for (int n = 1;; n++)
    {
        auto start = steady_clock::now();
        recursive_fibonacci(n);
        auto end = steady_clock::now();
        double elapsed = duration_cast<duration<double>>(end - start).count();

        // Se o tempo de execução for 60 segundos ou mais, interrompe o loop.
        if (elapsed >= 60.0)
            break;

        n_recursive.push_back(n);
        t_recursive.push_back(elapsed);
        cout << "Recursivo: n = " << n << " levou " << elapsed << " segundos." << endl;
    }
    cout << "Recursivo: n = " << n_recursive.size() << " valores avaliados." << endl;

    // Realiza o benchmark da função Fibonacci iterativa.
    cout << "\nExecutando benchmark Fibonacci iterativo..." << endl;
    const int max_iterative_n = 1000000;
    auto total_start = steady_clock::now();
    for (int n = 1; n <= max_iterative_n; n++)
    {
        auto start = steady_clock::now();
        iterative_fibonacci(n);
        auto end = steady_clock::now();
        double elapsed = duration_cast<duration<double>>(end - start).count();
        double total_elapsed = duration_cast<duration<double>>(end - total_start).count();

        // Se o tempo de execução total for 60 segundos ou mais, interrompe o loop.
        if (total_elapsed >= 60.0)
            break;

        n_iterative.push_back(n);
        t_iterative.push_back(elapsed);

        // Opcional: imprime progresso a cada 10000 iterações
        if (n % 10000 == 0)
            cout << "Iterativo: n = " << n << " levou " << elapsed << " segundos." << endl;
    }
    cout << "Iterativo: n = " << n_iterative.size() << " valores avaliados." << endl;

    // Plotando os resultados em um único gráfico com duas subplots
    matplot::figure();

    // Configurando layout com um gráfico principal e subplots secundários
    matplot::subplot(1, 1, 0);

    // Plot ambos os algoritmos no mesmo gráfico
    matplot::hold(matplot::on);
    matplot::plot(n_recursive, t_recursive, "r-")->line_width(2);
    matplot::plot(n_iterative, t_iterative, "b-")->line_width(2);

    // Adicionando legenda
    matplot::legend({"Recursivo", "Iterativo"});

    // Melhorando a visualização com grid
    matplot::grid(matplot::on);

    // Adicionando títulos e labels
    matplot::xlabel("n (tamanho da entrada)");
    matplot::ylabel("Tempo de execução (segundos)");
    matplot::title("Comparação: Fibonacci Recursivo vs Iterativo");

    // Exibindo o gráfico
    matplot::show();

    // Criando um segundo gráfico para mostrar diferença de comportamento
    matplot::figure();
    matplot::tiledlayout(2, 1);

    // Primeira parte: Fibonacci recursivo
    matplot::nexttile();
    matplot::plot(n_recursive, t_recursive, "r-")->line_width(2);
    matplot::title("Fibonacci Recursivo - Crescimento Exponencial O(2^n)");
    matplot::xlabel("n");
    matplot::ylabel("Tempo (s)");
    matplot::grid(matplot::on);

    // Segunda parte: Fibonacci iterativo
    matplot::nexttile();
    matplot::plot(n_iterative, t_iterative, "b-")->line_width(2);
    matplot::title("Fibonacci Iterativo - Crescimento Linear O(n)");
    matplot::xlabel("n");
    matplot::ylabel("Tempo (s)");
    matplot::grid(matplot::on);

    matplot::show();

    std::cin.get();
    return 0;
}