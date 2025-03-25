#include "../../src/simple_setup_test_py_cpp/calc/SampleClass.h"
#include <catch2/catch_test_macros.hpp>

TEST_CASE("SampleClass behaves as expected", "[SampleClass]")
{
  simple_setup_test_py::calc::SampleClass sampleClass =
    simple_setup_test_py::calc::SampleClass();
  CHECK_NOTHROW(sampleClass.setValue(10));
  REQUIRE(sampleClass.getValue() == 10);
  REQUIRE(sampleClass.getValue() != 11);
}
