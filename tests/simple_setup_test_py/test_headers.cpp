
#define CATCH_CONFIG_MAIN

#include <catch2/catch_approx.hpp>
#include <catch2/catch_test_macros.hpp>
#include <filesystem>
#include <iostream>
#include <string>
extern "C"
{
#include <igraph/igraph.h>
}


TEST_CASE("TESTS ARE RUN", "[general]")
{
  REQUIRE(1 == 2 - 1);
}