cmake_minimum_required(VERSION 3.29)
project(Matrix)

set(CMAKE_CXX_STANDARD 26)


set(INCLUDE
        include
        include/exs)

# ENABLE WHICH EXERCISE YOU WANT HERE
set(SRC
        src/main.cpp
 #       src/exs/ex1.cpp
#        src/exs/ex2.cpp
#        src/exs/ex3.cpp
#        src/exs/ex4.cpp
#        src/exs/ex5.cpp
         src/exs/ex6.cpp
)

add_executable(Matrix ${SRC})
target_include_directories(Matrix PRIVATE ${INCLUDE})


