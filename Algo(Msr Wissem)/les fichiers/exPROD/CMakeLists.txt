cmake_minimum_required(VERSION 3.29)
project(exPROD)

set(CMAKE_CXX_STANDARD 26)
find_package(Boost REQUIRED COMPONENTS serialization)

add_executable(exPROD main.cpp
        objects.h)

target_link_libraries(exPROD PRIVATE Boost::serialization)
