cmake_minimum_required(VERSION 3.29)
project(Main)

set(CMAKE_CXX_STANDARD 26)

add_executable(Main main.cpp
        other/stack.cpp
        other/trees.cpp
        other/linkedlist.cpp
        other/matrix.cpp)
