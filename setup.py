import os
import shutil
import string
import sys
import warnings
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict, Iterator, List, Union

from setuptools import find_namespace_packages, find_packages

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise


cmake_args = ["-DCMAKE_BUILD_TYPE=RelWithDebInfo"]
# cmake_args = ["-Digraph_DEBUG=ON", "-DCMAKE_FIND_DEBUG_MODE=ON"]

if (os.getenv('VCPKG_ROOT')):
    toolchainFile = os.path.join(
        os.getenv('VCPKG_ROOT'), "scripts", "buildsystems", "vcpkg.cmake")
    if (os.path.isfile(toolchainFile)):
        cmake_args.append(
            "-DCMAKE_TOOLCHAIN_FILE={}".format(toolchainFile.replace("\\", "/")))
        # cmake_args.append("-DVCPKG_TARGET_TRIPLET=x86-windows-static")
        print("Using toolchain \"{}\"".format(toolchainFile))
    else:
        warnings.warn(
            "Detected VCPKG_ROOT. Did not find toolchain file {} though.".format(toolchainFile))

# delete vendor caches — this is useful if you compile
# this project using CMake (e.g. for tests) as well as skbuild,
# as the two build directories of vendor do not interact well.
vendorFilesToDelete = [
    os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'vendor/igraph/src/igraphLib-build')),
    os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'vendor/nlopt/src/nloptLib-build'))
]
for vendorFile in vendorFilesToDelete:
    if (os.path.exists(vendorFile)):
        try:
            shutil.rmtree(vendorFile)
        except:
            warnings.warn(
                "Could not delete directory {}. Errors incoming.".format(vendorFile))
    else:
        print("No need to delete {}".format(vendorFile))

# skbuildCaches = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), '_skbuild'))
# if (os.path.exists(skbuildCaches)):
#     try:
#         shutil.rmtree(skbuildCaches)
#     except:
#         warnings.warn(
#             "Could not delete directory {}. Errors incoming.".format(skbuildCaches))


setup(
    name="simple_setup_test_py",
    version="0.1.0",
    description="A test setup for C++ with Python and libraries",
    long_description_content_type="text/markdown",
    long_description=Path('README.md').read_text(),
    keywords=["Test", "Science"],
    author="Tim Bernhard",
    author_email="tim@bernhard.dev",
    url="https://github.com/GenieTim/simple_setup_test_py",
    packages=find_namespace_packages(where="src", exclude=("tests",)),
    package_dir={"": "src"},
    cmake_install_dir="src/simple_setup_test_py_cpp",
    cmake_args=cmake_args,
    include_package_data=True,
    extras_require={"test": ["unittest"]},
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent"
    ],

)
