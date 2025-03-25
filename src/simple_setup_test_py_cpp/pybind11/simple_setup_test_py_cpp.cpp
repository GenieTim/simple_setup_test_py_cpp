#include "../calc/SampleClass.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

void
init_setup_test_bound_calc(py::module_&);

PYBIND11_MODULE(simple_setup_test_py_cpp, m)
{
  m.doc() = R"pbdoc(
    Simple Cpp Py Setup Tester
    -----------------

    A setup to test the setup and the tests.

    .. autosummary::
        :toctree: _generate

    )pbdoc";

  init_setup_test_bound_calc(m);

  py::class_<simple_setup_test_py::calc::SampleClass>(
    m, "SampleClass", py::module_local())
    .def(py::init<>())
    .def("set_value", &simple_setup_test_py::calc::SampleClass::setValue)
    .def("get_value", &simple_setup_test_py::calc::SampleClass::getValue);
}
