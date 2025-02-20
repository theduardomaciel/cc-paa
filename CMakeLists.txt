cmake_minimum_required(VERSION 3.29)
project(cc_paa)

set(CMAKE_CXX_STANDARD 14)

include_directories(impl)

add_executable(cc_paa
        impl/question10.cpp
        impl/question10.h)
