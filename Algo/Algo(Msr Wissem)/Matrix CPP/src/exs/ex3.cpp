//
// Created by aziz on 10/29/24.
//
#include "ex3.h"

void run() {
    int matrix[4][3];

    //part 1
    /*int offset = 0;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 3; j++) {
            matrix[i][j] = j + i + offset + 1;
        }
        offset+=2;
    }*/

    //part 2
    /*int offset = 0;
    for(int j = 0; j < 3; j++) {
        for(int i = 0; i < 4; i++) {
            matrix[i][j] = j + i + offset + 1;
        }
        offset += 3;
    }*/

    //part 3
    /*
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 3; j++) {
            if(i == 0 || i == 3)
                matrix[i][j] = 1;
            else if(j != 0 && j != 2)
                matrix[i][j] = 0;
            else
                matrix[i][j] = 1;
        }
    }
    */

    //part 4
    //don't care
    /*int offset = 0;
    int rel = 0;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 3; j++) {
            rel++;
            matrix[i][j] = i + j + offset + rel + 1;
        }
        offset += 2;
    }*/

    //part 5
    /*int offset = 0;
    bool reverse = false;
    for(int i = 0; i < 4; i++) {
        if(reverse) {
            int k = 2;
            for(int j = 2; j >= 0; j--) {
                matrix[i][k - j] = i + j + offset + 1;
            }
            reverse = false;
        }
        else {
            for(int j = 0; j < 3; j++) {
                matrix[i][j] = i + j + offset + 1;
            }
            reverse = true;
        }
        offset += 2;
    }*/


    //display
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 3; j++) {
            std::cout << matrix[i][j] << ' ';
        }
        std::cout << '\n';
    }
}
