cmake_minimum_required(VERSION 3.10)
cmake_policy(SET CMP0077 NEW)

# set the project name
project(simple_setup_test_py VERSION 1.0)
add_library(simple_setup_test_py simple_setup_test_py.cpp)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# TODO: remove
# set(CMAKE_CXX_FLAGS "-pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-overflow=5 -Wswitch-default -Wundef -Wno-unused -g")

# add libraries
if (DEFINED ADDITIONAL_INCLUDES)
	include_directories(ADDITIONAL_INCLUDES)
endif()

if (DEFINED ADDITIONAL_LIBS)
	link_directories(ADDITIONAL_LIBS)
endif()

# add dependencies
include(${CMAKE_CURRENT_SOURCE_DIR}/../../vendor/CMakeLists.txt)

# add_dependencies(simple_setup_test_py Eigen3::Eigen)

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
# Eigen3::Eigen 

# optional additional dependencies
find_package(OpenMP)
if (OpenMP_FOUND AND OpenMP_INCLUDE_DIRS)
  include_directories(${OpenMP_INCLUDE_DIRS})
	target_link_libraries(simple_setup_test_py PRIVATE ${OpenMP_LIBRARIES})
	add_definitions(-DOPENMP_FOUND=true)
	message(INFO "Found OpenMP")
else()
	message("Did not find OpenMP")
endif()

target_sources(simple_setup_test_py
	PRIVATE
		${CMAKE_CURRENT_LIST_DIR}/calc/SampleClass.cpp
	PUBLIC
		${CMAKE_CURRENT_LIST_DIR}/calc/TopologyCalc.h
		${CMAKE_CURRENT_LIST_DIR}/calc/SampleClass.h
)

set_target_properties(simple_setup_test_py PROPERTIES VERSION ${PROJECT_VERSION})

if (NOT DEFINED CODE_COVERAGE)
option(CODE_COVERAGE "Collect coverage from test library" OFF)
endif()

if(CODE_COVERAGE)
	if (CMAKE_BUILD_TYPE EQUAL "RELEASE")
		message(WARNING "Using coverage reduces build type to debug from release")
	endif()
	set(ENABLE_COVERAGE ON)
	set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../../vendor/CMake-codecov/cmake" ${CMAKE_MODULE_PATH})
	find_package(codecov)

	set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -g -fprofile-arcs -ftest-coverage ")
	set(CMAKE_CXX_FLAGS " ${CMAKE_CXX_FLAGS} -O0 -g -fprofile-arcs -ftest-coverage ")
	target_compile_options(simple_setup_test_py PRIVATE -O0 -g -fprofile-arcs -ftest-coverage )

	if(CMAKE_COMPILER_IS_GNUCXX)
		set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-abs-path")
		set(CMAKE_CXX_FLAGS " ${CMAKE_CXX_FLAGS} -fprofile-abs-path")
		target_compile_options(simple_setup_test_py PRIVATE -fprofile-abs-path)
	endif()

	target_link_libraries(
		simple_setup_test_py
		PRIVATE
		--coverage
	)
	add_coverage(simple_setup_test_py)
else()
	message("Code Coverage is disabled.")
endif()

if (LEAK_ANALYSIS)
	set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-omit-frame-pointer -fsanitize=address")
	set (CMAKE_LINKER_FLAGS "${CMAKE_LINKER_FLAGS} -fno-omit-frame-pointer -fsanitize=address")
	target_link_libraries(simple_setup_test_py 
		PRIVATE
		-fsanitize=address
	)
endif()
