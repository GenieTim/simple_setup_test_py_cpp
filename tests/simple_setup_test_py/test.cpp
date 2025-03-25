#define CATCH_CONFIG_MAIN
#include "../../src/simple_setup_test_py_cpp/calc/SampleClass.h"
#include <catch2/catch_test_macros.hpp>
#include <unordered_map>
#include <vector>

TEST_CASE("TESTS ARE RUN", "[general]")
{
  REQUIRE(1 == 2 - 1);
}

TEST_CASE("std::map behaves as expected", "[general]")
{
  std::unordered_map<size_t, size_t> testMap;
  std::vector<size_t> zeros = { 0, 0, 0, 0, 0 };
  CHECK(testMap.emplace(0, 100).second == true);
  for (size_t i = 0; i < zeros.size(); ++i) {
    CHECK(testMap.emplace(zeros[i], i).second == false);
  }
}

TEST_CASE("SampleClass behaves as expected", "[SampleClass]")
{
  simple_setup_test_py::calc::SampleClass sampleClass =
    simple_setup_test_py::calc::SampleClass();
  CHECK_NOTHROW(sampleClass.setValue(10));
  REQUIRE(sampleClass.getValue() == 10);
  REQUIRE(sampleClass.getValue() != 11);
}
