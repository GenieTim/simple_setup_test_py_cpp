add_library(simple_setup_test_py_bindings)

set_target_properties(simple_setup_test_py_bindings PROPERTIES LINKER_LANGUAGE CXX)

# add dependencies

include(${CMAKE_CURRENT_SOURCE_DIR}/../../../vendor/CMakeLists.txt)

target_include_directories(simple_setup_test_py_bindings
	PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
)
