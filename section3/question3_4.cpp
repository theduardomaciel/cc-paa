#include <iostream>

/*
    Escreva um algoritmo de divisão-e-conquista $O(log n)$ para computar $a^n$, em que n é um inteiro positivo.

    1: procedure POTENCIA_RAPIDA(a, n)
    2:      if n = 0 then
    3:          return 1
    4:      end if
    5:      metade ← POTENCIA_RAPIDA(a, ⌊n/2⌋)
    6:      if n mod 2 = 0 then
    7:          return metade × metade
    8:      else
    9:          return a × metade × metade
    10:     end if
    11: end procedure
*/

/**
 * Calcula a^n usando o algoritmo de divisão-e-conquista em O(log n).
 *
 * @param a base
 * @param n n (inteiro positivo)
 * @return a^n
 */
long long potencia_rapida(long long a, int n)
{
    // Caso base
    if (n == 0)
    {
        return 1;
    }

    // Divisão: calcular a^(n/2)
    long long half = potencia_rapida(a, n / 2);

    // Conquista: combinar o resultado
    if (n % 2 == 0)
    {
        // Se n é par, a^n = (a^(n/2))^2
        return half * half;
    }
    else
    {
        // Se n é ímpar, a^n = a * (a^(n/2))^2
        return a * half * half;
    }
}

// Função principal para demonstração
int main()
{
    long long a;
    int n;

    std::cout << "Digite a base: ";
    std::cin >> a;

    std::cout << "Digite o expoente (inteiro positivo): ";
    std::cin >> n;

    if (n < 0)
    {
        std::cout << "O n deve ser positivo." << std::endl;
        return 1;
    }

    std::cout << a << "^" << n << " = " << potencia_rapida(a, n) << std::endl;

    return 0;
}