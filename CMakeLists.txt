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
# list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
list(APPEND CMAKE_MODULE_PATH /usr/local/anaconda3/lib/python3.7/site-packages/skbuild/resources/cmake/)
find_package(PythonExtensions REQUIRED)

if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c
            "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()

# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)

message("Using toolchain file ${CMAKE_TOOLCHAIN_FILE}")

# add sources & targets
add_subdirectory(src/simple_setup_test_py_cpp)
add_dependencies(simple_setup_test_py igraphLib)
add_dependencies(simple_setup_test_py nlopt)

pybind11_add_module(simple_setup_test_py_cpp MODULE 
  src/simple_setup_test_py_cpp/pybind11/calculations.cpp
  src/simple_setup_test_py_cpp/pybind11/simple_setup_test_py_cpp.cpp
)

# add other dependencies
include_directories(${igraph_INCLUDE_DIRS})
include_directories(${nlopt_INCLUDE_DIRS})

message("simple_setup_test_py_cpp includes igraph from ${igraph_INCLUDE_DIRS}")

# link
target_link_libraries(simple_setup_test_py_cpp 
  PUBLIC 
    simple_setup_test_py
    ${igraph_LIBRARIES}
    ${nlopt_LIBRARIES}
)


if(CMAKE_COMPILER_IS_GNUCXX)
target_link_libraries(simple_setup_test_py_cpp 
  PUBLIC 
    stdc++fs
)
endif()

# link Eigen libraries. Difficulty due to Windows GitHub Action, somehow.
if (TARGET Eigen3::Eigen)
	message(STATUS "Target Eigen3::Eigen found")
	target_link_libraries(simple_setup_test_py PUBLIC Eigen3::Eigen)
else()
	include_directories(${EIGEN3_INCLUDE_DIRS})
	include_directories(${EIGEN3_INCLUDE_DIRS}/eigen3)
	target_link_libraries(simple_setup_test_py PUBLIC ${EIGEN3_LIBRARIES})
	message(STATUS "Eigen include directories: ${EIGEN3_INCLUDE_DIRS}, libraries ${EIGEN3_LIBRARIES}")
endif()

# compile & install
target_compile_definitions(simple_setup_test_py_cpp PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS simple_setup_test_py_cpp LIBRARY DESTINATION .)
