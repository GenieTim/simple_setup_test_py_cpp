# simple_setup_test_py_cpp

<!--[![Test Coverage of Python Code](https://github.com/GenieTim/simple_setup_test_py_cpp/blob/main/.github/coverage.svg?raw=true)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml)
[![Test Coverage of C++ Code](https://github.com/GenieTim/simple_setup_test_py_cpp/blob/main/.github/cpp-coverage.svg?raw=true)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml)-->

[![Total Code Test Coverage](https://codecov.io/gh/GenieTim/simple_setup_test_py_cpp/branch/main/graph/badge.svg?token=5ZE1VSDXJQ)](https://codecov.io/gh/GenieTim/simple_setup_test_py_cpp)
[![Run Tests](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml/badge.svg)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml)
[![Publish Documentation](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/publish-documentation-html.yml/badge.svg)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/publish-documentation-html.yml)[![PyPI version](https://badge.fury.io/py/simple_setup_test_py_cpp.svg)](https://badge.fury.io/py/simple_setup_test_py_cpp)
[![PyPI download month](https://img.shields.io/pypi/dm/simple_setup_test_py_cpp.svg)](https://pypi.python.org/pypi/simple_setup_test_py_cpp/)
[![PyPI license](https://img.shields.io/pypi/l/simple_setup_test_py_cpp.svg)](https://pypi.python.org/pypi/simple_setup_test_py_cpp/)

A sample setup of Pybind11 with Catch2 and Python tests.
In particular, it's used as a playground to test and experiment and fix,
such as

- getting coverage for separate header and non-header tests

The following belongs to the bootstrap, I would not recommend to actually install this package (it has more use if you use it as a template for your pybind11 package project).

## Installation

Use pip:

`pip install simple_setup_test_py_cpp`

## Usage

**NOTE**: currently, this release's API is _unstable_ and subject to change.

See the [documentation](https://genietim.github.io/simple_setup_test_py_cpp) for a current list of all available functions.

### Example

Example usage can be found in the [documentation](https://genietim.github.io/simple_setup_test_py_cpp), the [tests](https://github.com/GenieTim/simple_setup_test_py_cpp/tree/main/tests),
the [CLI application](https://github.com/GenieTim/simple_setup_test_py_cpp/tree/main//src/simple_setup_test_py/simple_setup_test_py.py) or in the following code snippet:

```python
from simple_setup_test_py_cpp import SampleClass

sample = SampleClass()

sample.set_value(12)
assert sample.get_value() == 12
```
