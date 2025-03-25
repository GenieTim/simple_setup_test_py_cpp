cmake_minimum_required(VERSION 3.15.0)

# Fix behavior of CMAKE_CXX_STANDARD when targeting macOS.
if (POLICY CMP0025)
  cmake_policy(SET CMP0025 NEW)
endif ()

# start project
project(simple_setup_test_py VERSION "0.1.0")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g")

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3")

if(CMAKE_COMPILER_IS_GNUCXX)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall -Wextra -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Woverloaded-virtual -Wredundant-decls -Wstrict-overflow=5 -Wswitch-default -Wundef -Wno-unused")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_LINKER_FLAGS "${CMAKE_LINKER_FLAGS} -fPIC")
set(CMAKE_LINK_FLAGS "${CMAKE_LINK_FLAGS} -fPIC")
endif()

include(${CMAKE_CURRENT_SOURCE_DIR}/vendor/CMakeLists.txt)

# prepare python bindings
add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/extern/pybind11)

message("Using toolchain file ${CMAKE_TOOLCHAIN_FILE}")

# add sources & targets
add_subdirectory(src/simple_setup_test_py_cpp)

pybind11_add_module(simple_setup_test_py_cpp MODULE 
  src/simple_setup_test_py_cpp/pybind11/calculations.cpp
  src/simple_setup_test_py_cpp/pybind11/simple_setup_test_py_cpp.cpp
)

# link
target_link_libraries(simple_setup_test_py_cpp 
  PUBLIC 
    simple_setup_test_py
)

if(CMAKE_CXX_COMPILER_ID IN_LIST "Intel;GNU")
  target_link_libraries(simple_setup_test_py_cpp 
    PUBLIC 
      stdc++fs
  )
endif()

# compile & install
target_compile_definitions(simple_setup_test_py_cpp PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS simple_setup_test_py_cpp LIBRARY DESTINATION .)
