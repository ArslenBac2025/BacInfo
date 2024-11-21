//
// Created by aziz on 10/29/24.
//

#include "ex4.h"
void run() {
    int matrix[4][4];

    int offset = 0;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            matrix[i][j] = i + j + offset + 1;
        }
        offset += 3;
    }

    auto display = [&]() {
        std::for_each(std::begin(matrix), std::end(matrix), [](const auto& row) {
        std::for_each(std::begin(row), std::end(row), [](int el) {
                std::cout << el << ' ';
        });
         std::cout << '\n';
     });
    };
    auto getsum = [&]() -> int {
        int res = 0;
        std::for_each(std::begin(matrix), std::end(matrix), [&res](const int (&row)[4]) {
            std::for_each(std::begin(row), std::end(row), [&res](int el) {
                res += el;
            });
        });
        return res;
    };
    auto diagonalsum = [&]() -> int {
        int res = 0;
        for(int i = 0; i < 4; i++) {
            res += matrix[i][i];
            res += matrix[i][4 - i - 1];
        }
        return res;
    };
    auto rowsum = [&]() -> void {
        for(int i = 0; i < 4; i++) {
            int temp = 0;
            for(int j = 0; j < 4; j++) {
                temp += matrix[i][j];
            }
            std::cout << temp << '\n';
            temp = 0;
        }
    };
    auto colsum = [&]() -> void {
        for(int i = 0; i < 4; i++) {
            int temp = 0;
            for(int j = 0; j < 4; j++) {
                temp += matrix[j][i];
            }
            std::cout << temp << '\n';
            temp = 0;
        }
    };
    auto maxval = [](int (&matrix)[4][4]) {
        int max = matrix[0][0];
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                max = std::max(max, matrix[i][j]);
            }
        }
        return max;
    };
}