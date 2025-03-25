
#define CATCH_CONFIG_MAIN

#include "../../src/simple_setup_test_py_cpp/calc/TopologyCalc.h"
#include <catch2/catch_approx.hpp>
#include <catch2/catch_test_macros.hpp>
#include <filesystem>
#include <iostream>
#include <string>

TEST_CASE("HEADER: TESTS ARE RUN", "[general]")
{
  REQUIRE(1 == 2 - 1);
}

TEST_CASE("Eigen Vectors are constructed", "[TopologyCalc]")
{
  Eigen::Vector3d vertex1;
  vertex1 << -1.0, -1.0, 0.0;
  Eigen::Vector3d vertex2;
  vertex2 << 1.0, -1.0, 0.0;
  Eigen::Vector3d vertex3;
  vertex3 << 1.0, 1.0, 0.0;

  CHECK(vertex1.isApprox(Eigen::Vector3d(-1.0, -1.0, 0.0)));
  CHECK(vertex1.isApprox(
    simple_setup_test_py::calc::pointsToVector3d(-1.0, -1.0, 0.0)));
  CHECK(vertex2.isApprox(Eigen::Vector3d(1.0, -1.0, 0.0)));
  CHECK(vertex2.isApprox(
    simple_setup_test_py::calc::pointsToVector3d(1.0, -1.0, 0.0)));
  CHECK(vertex3.isApprox(Eigen::Vector3d(1.0, 1.0, 0.0)));
  CHECK(vertex3.isApprox(
    simple_setup_test_py::calc::pointsToVector3d(1.0, 1.0, 0.0)));
}
