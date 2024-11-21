//
// Created by aziz on 10/29/24.
//
#include "ex2.h"

void run() {
    char matrix[MAX_SIZE][MAX_SIZE];
    for(std::size_t i{0}; i < MAX_SIZE; i++) {
        for(std::size_t j{0}; j < MAX_SIZE; j++) {
            matrix[i][j] = ' ';
        }
    }

    //part 1
    /*for(int i = 0; i < MAX_SIZE; i++) {
        for(int j = 0; j <= i; j++) {
            matrix[i][j] = j + '0';
        }
    }*/

    //part 2
    /*for(int i = 0; i < MAX_SIZE; i++) {
        for(int j = i; j < MAX_SIZE; j++) {
            matrix[i][j] = j + '0';
        }
    }*/

    //part 3
    /*
    for(int i = 0; i < MAX_SIZE; i++) {
        for(int j = 0; j < MAX_SIZE - i; j++) {
            matrix[i][j] = j + '0';
        }
    }
    */

    //part 4
    /*
    for(int i = 0; i < MAX_SIZE; i++) {
        for(int j = MAX_SIZE - 1; j >= MAX_SIZE - i - 1; j--) {
            matrix[i][j] = j + '0';
        }
    }
    */

    //Part 5
    /*
    for(int i = 0; i < MAX_SIZE; i++) {
        for(int j = 0; j < MAX_SIZE; j++) {
            if(i == j) {
                matrix[i][j] = '0';
            }
            else if(i < j) {
                matrix[i][j] = '2';
            }
            else {
                matrix[i][j] = '1';
            }
        }
    }
    */

    std::for_each(std::begin(matrix), std::end(matrix), [](const char (&row)[MAX_SIZE]) {
        std::for_each(std::begin(row), std::end(row), [](char c) {
            std::cout << c << ' ';
        });
        std::cout << '\n';
    });
}