# simple_setup_test_py_cpp

<!--[![Test Coverage of Python Code](https://github.com/GenieTim/simple_setup_test_py_cpp/blob/main/.github/coverage.svg?raw=true)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml)
[![Test Coverage of C++ Code](https://github.com/GenieTim/simple_setup_test_py_cpp/blob/main/.github/cpp-coverage.svg?raw=true)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml)-->
[![Total Code Test Coverage](https://codecov.io/gh/GenieTim/simple_setup_test_py_cpp/branch/main/graph/badge.svg?token=5ZE1VSDXJQ)](https://codecov.io/gh/GenieTim/simple_setup_test_py_cpp)
[![Run Tests](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml/badge.svg)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/run-tests.yml)
[![Publish Documentation](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/publish-documentation-html.yml/badge.svg)](https://github.com/GenieTim/simple_setup_test_py_cpp/actions/workflows/publish-documentation-html.yml)[![PyPI version](https://badge.fury.io/py/simple_setup_test_py_cpp.svg)](https://badge.fury.io/py/simple_setup_test_py_cpp)
[![PyPI download month](https://img.shields.io/pypi/dm/simple_setup_test_py_cpp.svg)](https://pypi.python.org/pypi/simple_setup_test_py_cpp/)
[![PyPI license](https://img.shields.io/pypi/l/simple_setup_test_py_cpp.svg)](https://pypi.python.org/pypi/simple_setup_test_py_cpp/)

A collection of utility python functions for handling LAMMPS output and polymers in Python.

This toolbox provides means to read LAMMPS output: be it data, dump or thermodynamic data files.
Additionally, it provides various methods to calculate with the read data, such as computing the
radius of gyration, mean end to end distance, or simply splitting a polymer network back up into its chains.

## Installation

Use pip:

`pip install simple_setup_test_py_cpp`

## Usage

**NOTE**: currently, this release's API is _unstable_ and subject to change.

See the [documentation](https://genietim.github.io/simple_setup_test_py_cpp) for a current list of all available functions.

### Example

Example useage can be found in the [documentation](https://genietim.github.io/simple_setup_test_py_cpp), the [tests](https://github.com/GenieTim/simple_setup_test_py_cpp/tree/main/tests),
the [CLI application](https://github.com/GenieTim/simple_setup_test_py_cpp/tree/main//src/simple_setup_test_py/simple_setup_test_py.py) or in the following code snippet:

```python
import numpy as np

from simple_setup_test_py_cpp import UniverseSequence

filePath = "some_lammps_output_file.dat"
universeSequence = UniverseSequence()
universeSequence.initializeFromDataSequence([filePath])
universe = universeSequence.atIndex(0)
print("Size: {}. Volume: {} u^3".format(
    universe.getSize(), universe.getVolume()))
print("Mean bond length: {} u".format(
    np.mean([m.computeBondLengths().mean() for m in universe])))
print("Mean end to end distance: {} u".format(
    np.mean([m.computeEndToEndDistance() for m in universe])))
```
