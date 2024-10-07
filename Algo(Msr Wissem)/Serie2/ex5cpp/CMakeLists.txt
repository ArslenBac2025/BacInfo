cmake_minimum_required(VERSION 3.29)
project(Wissem)

set(CMAKE_CXX_STANDARD 26)

include_directories(${CMAKE_SOURCE_DIR}/ex5)

set(SOURCES main.cpp
        ex5/ex5.cpp)

add_executable(Wissem ${SOURCES})
