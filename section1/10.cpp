#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Função que calcula o tamanho da sequência de Collatz a partir de um valor inicial.
// A sequência termina quando os três últimos valores forem 4, 2 e 1 (nessa ordem).
int getUlamAlgorithmSequenceLength(unsigned short start)
{
    // a_val, b_val e c_val representam os três últimos valores da sequência.
    unsigned int a_val = 0, b_val = 0, c_val = start;
    int length = 1; // representa o tamanho da sequência (contando o valor inicial)

    // Limite de iterações para evitar loops infinitos (segurança, evitar 🧨)
    int iterations = 0;
    const int maxIterations = 10000;

    // Enquanto a sequência não tiver pelo menos 3 elementos ou os últimos três não forem 4, 2, 1:
    while ((length < 3) || !(a_val == 4 && b_val == 2 && c_val == 1))
    {
        unsigned int next;

        // Algoritmo de Ulam:
        // Se c_val for par, divide por 2; se for ímpar, multiplica por 3 e soma 1.
        if (c_val % 2 == 0)
            next = c_val / 2;
        else
            next = 3 * c_val + 1;

        // Atualiza os últimos três valores
        a_val = b_val;
        b_val = c_val;
        c_val = next;

        length++; // Incrementa o tamanho da sequência

        iterations++;
        if (iterations > maxIterations)
        {
            // Se ultrapassar o número máximo de iterações, interrompe.
            std::cerr << "Erro: loop infinito detectado para o valor " << start << endl;
            break;
        }
    }
    return length;
}

int main()
{
    int maxLength = 0;
    unsigned short valueWithMaxLength = 0;
    unsigned long long totalLength = 0;

    // Inicia a medição do tempo de execução (biblioteca "chrono")
    auto startTime = high_resolution_clock::now();

    // Testa todas as entradas de 1 a 65535 (unsigned short int).
    for (unsigned int i = 1; i <= 65535; i++)
    {
        int seqLength = getUlamAlgorithmSequenceLength(static_cast<unsigned short>(i));
        totalLength += seqLength;
        if (seqLength > maxLength)
        {
            maxLength = seqLength;
            valueWithMaxLength = static_cast<unsigned short>(i);
        }
    }

    // Calcula a média dos tamanhos das sequências
    double averageLength = static_cast<double>(totalLength) / 65535;

    // Finaliza a medição do tempo de execução
    auto endTime = high_resolution_clock::now();
    duration<double> execTime = endTime - startTime;

    // Finalmente, exibimos o relatório com os resultados
    cout << "Tamanho da maior sequência encontrada: " << maxLength << endl;
    cout << "Valor que gerou a maior sequência: " << valueWithMaxLength << endl;
    cout << "Média dos tamanhos das sequências: " << averageLength << endl;
    cout << "Tempo de execução: " << execTime.count() << " segundos" << endl;

    return 0;
}
