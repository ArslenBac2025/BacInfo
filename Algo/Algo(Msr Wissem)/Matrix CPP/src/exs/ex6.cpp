//
// Created by aziz on 10/29/24.
//
#include "ex6.h"

void run() {
    const int SIZE = 4;
    int matrix1[SIZE][SIZE] = {
        {1, 2, 3, 1},
        {5, 1, 1, 8},
        {9, 1, 1, 12},
        {1, 14, 15, 1}
    };

    int matrix2[SIZE][SIZE] = {
        {1, 2, 3, 4},
        {5, 1, 7, 8},
        {9, 10, 1, 12},
        {13, 14, 15, 2} // Different value on the bottom-right to test non-identical diagonal
    };

    auto identic_matrix = [](const auto& matrix) -> bool {
        bool cond = true;
        int init_val = matrix[0][0];

        int i = 0; int j = 0;
        while(cond) {
            if(i == std::size(matrix) || j == std::size(matrix[i])) break;
            else if(matrix[i][j] != init_val) cond = false;
            else{
                i++;
                j++;
            }
        }

        i = 0;
        j = std::size(matrix[i]) - 1;
        while(cond) {
            if(i >= std::size(matrix) || j < 0) break;
            else if(matrix[i][j] != init_val) cond = false;
            else{
                i++;
                j--;
            }

        }
        return cond;
    };

    std::cout << identic_matrix(matrix1) << std::endl;
    std::cout << identic_matrix(matrix2) << std::endl;
}
