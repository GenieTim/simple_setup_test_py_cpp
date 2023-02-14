import os
import sys

# make sure we use the "live" simple_setup_test_py, not the installed one
# but only the Python one, for the cpp one, we need the copiled/installed
import simple_setup_test_py_cpp
simple_setup_test_py_cpp_path = simple_setup_test_py_cpp.__file__
sys.path.insert(0, os.path.dirname(__file__) + "/../../src")
sys.path.insert(0, os.path.dirname(simple_setup_test_py_cpp_path))
# sys.path.insert(0, os.path.dirname(__file__) + "/../../src/simple_setup_test_py/calc")
# sys.path.insert(0, os.path.dirname(__file__) + "/../../src/simple_setup_test_py/io")
# sys.path.insert(0, os.path.dirname(__file__) +
#                 "/../../src/simple_setup_test_py/utils")

sys.path.insert(0, os.path.dirname(__file__))
