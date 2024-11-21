#include "ex5.h"

void run() {
    //first part
    /*{
        const int size = 4;
        std::string matrix[size][size];

        auto fill_matrix = [](int size, std::string (*matrix)[4]) {
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    matrix[i][j] = '0';
                }
            }


        };
        auto pascal = [](int size, std::string matrix[4][4]) {
            for (int i = 0; i < size; i++) {
                if(i <= 1) {
                    for (int j = 0; j <= i; j++) {
                        matrix[i][j] = '1';
                    }
                }
                else {
                    for(int j = 0; j <= i; j++) {
                        if(j == 0 || j == i) matrix[i][j] = '1';
                        else matrix[i][j] = std::to_string(std::stoi(matrix[i - 1][j - 1]) + std::stoi(matrix[i - 1][j]));
                    }
                }
            }
        };
        auto display_matrix = [](int size, std::string matrix[4][4]) {
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    std::cout << matrix[i][j] << ' ';
                }
                std::cout << '\n';
            }
        };

        fill_matrix(size, matrix);
        pascal(size, matrix);
        display_matrix(size, matrix);
    }*/

    //second part
    {
        const int size = 8;
        std::string matrix[size][size];

        //fill matrix
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                matrix[i][j] = "0";
            }
        }

        auto weird_pascal = [](int size, auto& matrix) {
            for (int i = 0; i < size; i++) {
                if(i <= 1) {
                    for (int j = size - i - 1; j < size; j++) {
                        matrix[i][j] = "1";
                    }
                }
                else {
                    for(int j = size - i - 1; j < size; j++) {
                        if(j == size - i - 1 || j == size - 1) matrix[i][j] = "1";
                        else if(j == size - 2){
                            matrix[i][j] = std::to_string(std::stoi(matrix[i][j - 1]) + stoi(matrix[i - 1][j]) + stoi(matrix[i - 1][j+1]));
                        }
                        else {
                            matrix[i][j] = matrix[i - 1][j + 1];
                        }
                    }
                }
            }

        };

        weird_pascal(size, matrix);
        //display
        std::for_each(std::begin(matrix), std::end(matrix), [](const std::string (&row)[8]) {
            std::for_each(std::begin(row), std::end(row), [](const auto& el) {
                std::cout << el << ' ';
            });
            std::cout << '\n';
        });
    }

}
