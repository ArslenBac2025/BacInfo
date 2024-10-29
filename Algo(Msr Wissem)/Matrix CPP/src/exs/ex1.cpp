//
// Created by aziz on 10/29/24.
//
#include "ex1.h"

void run() {
    char matrix[4][4];

    //Assign valid values
    for(std::size_t i {0}; i < 4; ++i) {
        for(std::size_t j {0}; j < 4; ++j) {
            matrix[i][j] = ' ';
        }
    }

    //part 1
    /*for(std::size_t i{0}; i < 4; ++i) {
        for(std::size_t j{0}; j <= i; j++) {
            matrix[i][j] = '*';
        }
    }*/

    //part 2
    /*for(int i{0}; i < 4; i++) {
        for(int j {3 - i}; j >= 0; j--) {
            matrix[i][j] = '*';
        }
    }*/

    //part 3
    /*for(int i {0}; i < 4; i++) {
        for(int j { 0 + i }; j < 4; j++) {
            matrix[i][j] = '*';
        }
    }*/

    //part 4
    /*for(int i {0}; i < 4; i++) {
        for(int j {3 - i}; j < 4; j++) {
            matrix[i][j] = '*';
        }
    }*/

    //Display
    for(std::size_t i {0}; i < 4; i++) {
        for(std::size_t j {0}; j < 4; j++) {
            std::cout << matrix[i][j] ;
        }
        std::cout << '\n';
    }

}