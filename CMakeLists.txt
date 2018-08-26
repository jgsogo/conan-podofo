cmake_minimum_required(VERSION 2.8)
project(cmake_wrapper)

include(conanbuildinfo.cmake)
conan_basic_setup()

message("Conan CMake Wrapper for ${SOURCE_FOLDER}")
add_subdirectory(${SOURCE_FOLDER})
