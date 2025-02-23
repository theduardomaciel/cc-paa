#include <iostream>
#include <chrono>
#include "question10.h"

void ulamAlgorithm(unsigned int a) {
    int x = a;
    // while the three last values from x are not 4, 2, 1 do

}

void runExhaustiveTest() {
    auto start = std::chrono::steady_clock::now();

    std::cout << "Running exhaustive test..." << std::endl;

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

        std::cout << "Value: " << i << ", Length: " << length << std::endl;
    }

    std::cout << "Exhaustive test completed." << std::endl;

    double avgLength = static_cast<double>(sumLengths) / 65535.0;

    std::cout << "Largest sequence size: " << largestSequenceSize << std::endl;
    std::cout << "Value with largest sequence: " << valueWithLargest << std::endl;
    std::cout << "Average size: " << avgLength << std::endl;
    
    auto end = std::chrono::steady_clock::now();
    auto elapsedMs = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    std::cout << "Execution time (ms): " << elapsedMs << std::endl;
}

int main() {
    runExhaustiveTest();
    return 0;
}