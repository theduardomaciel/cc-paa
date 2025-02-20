#include <iostream>
#include <chrono>
#include "question10.h"

static int computeSequenceLength(unsigned short a) {
    unsigned long x = a;
    int length = 1;
    while (x != 1) {
        if (x % 2 == 0) {
            x /= 2;
        } else {
            x = 3 * x + 1;
        }
        length++;
    }
    return length;
}

void runExhaustiveTest() {
    auto start = std::chrono::steady_clock::now();

    int largestSequenceSize = 0;
    unsigned short valueWithLargest = 0;
    long long sumLengths = 0;

    for (unsigned short i = 1; i <= 65535; i++) {
        int length = computeSequenceLength(i);
        sumLengths += length;
        if (length > largestSequenceSize) {
            largestSequenceSize = length;
            valueWithLargest = i;
        }
    }
    double avgLength = static_cast<double>(sumLengths) / 65535.0;

    auto end = std::chrono::steady_clock::now();
    auto elapsedMs = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    std::cout << "Largest sequence size: " << largestSequenceSize << std::endl;
    std::cout << "Value with largest sequence: " << valueWithLargest << std::endl;
    std::cout << "Average size: " << avgLength << std::endl;
    std::cout << "Execution time (ms): " << elapsedMs << std::endl;
}

int main() {
    runExhaustiveTest();
    return 0;
}