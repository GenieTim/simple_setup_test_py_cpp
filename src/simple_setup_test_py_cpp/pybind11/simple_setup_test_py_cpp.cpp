
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

    A setup to test.

    .. autosummary::
        :toctree: _generate

    )pbdoc";

  init_setup_test_bound_calc(m);
}
