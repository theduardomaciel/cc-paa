cmake_minimum_required(VERSION 3.10.0)
project(cc-paa VERSION 0.1.0 LANGUAGES C CXX)

add_subdirectory(matplotplusplus)

add_executable(cc-paa impl/question2_5.cpp)
target_link_libraries(cc-paa PUBLIC matplot)