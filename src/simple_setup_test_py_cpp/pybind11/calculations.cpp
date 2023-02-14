#ifndef PYBIND_CALC_H
#define PYBIND_CALC_H

#include "../calc/TopologyCalc.h"

#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

using namespace simple_setup_test_py::calc;

void
init_setup_test_bound_calc(py::module_& m)
{
     m.def("pointsToVector3d", &pointsToVector3d, R"pbdoc(
          Some documentation
     )pbdoc", py::arg("x"), py::arg("y"), py::arg("z"));
     m.def("segmentIntersectsTriangle", &segmentIntersectsTriangle, R"pbdoc(
          Möller-Trumbore intersection algorithm, see
          https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithmn
     )pbdoc", py::arg("rayOrigin"), py::arg("rayTarget"), py::arg("vertex0"), py::arg("vertex1"), py::arg("vertex2"),py::arg("EPS") = 1e-6 );
}

#endif /* PYBIND_CALC_H */
