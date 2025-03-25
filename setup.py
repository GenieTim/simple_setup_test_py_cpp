import os
import platform
import re
import shutil
import subprocess
import sys
import warnings
from pathlib import Path

from setuptools import Extension, find_namespace_packages, setup
from setuptools.command.build_ext import build_ext

VERSION = "0.1.1"

# "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON",
cmake_args = [
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-Dvendor_suffix=-skbuild-{}".format(platform.system()),
]
if os.environ.get("CMAKE_ARGS"):
    cmake_args.extend(os.environ.get("CMAKE_ARGS").split())

if os.getenv("VCPKG_ROOT"):
    toolchain_file = os.path.join(
        os.getenv("VCPKG_ROOT"), "scripts", "buildsystems", "vcpkg.cmake"
    )
    if os.path.isfile(toolchain_file):
        cmake_args.append(
            "-DCMAKE_TOOLCHAIN_FILE={}".format(toolchain_file.replace("\\", "/"))
        )
        # cmake_args.append("-DVCPKG_TARGET_TRIPLET=x86-windows-static")
        print('Using toolchain "{}"'.format(toolchain_file))
    else:
        warnings.warn(
            "Detected VCPKG_ROOT. Did not find toolchain file {} though.".format(
                toolchain_file
            )
        )
else:
    print("VCPKG_ROOT not set. Not using vcpk dependencies.")

# skbuildCaches = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), '_skbuild'))
# if (os.path.exists(skbuildCaches)):
#     try:
#         shutil.rmtree(skbuildCaches)
#     except:
#         warnings.warn(
#             "Could not delete directory {}. Errors incoming.".format(skbuildCaches))

with open("README.md", "r") as file:
    readme_content = file.read()


# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


# A CMakeExtension needs a sourcedir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
# If you need multiple extensions, see scikit-build.
class CMakeExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    def build_extension(self, ext: CMakeExtension) -> None:
        # Must be in this form due to bug in .resolve() only fixed in Python
        # 3.10+
        ext_fullpath = Path.cwd() / self.get_ext_fullpath(ext.name)
        extdir = ext_fullpath.parent.resolve()

        # Using this requires trailing slash for auto-detection & inclusion of
        # auxiliary "native" libs

        debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
        cfg = "Debug" if debug else "RelWithDebInfo"  # "Release"

        # The CMake build process is done in a temporary directory,
        # so we have to create it here.
        build_temp = Path(self.build_temp) / ext.name
        if not build_temp.exists():
            build_temp.mkdir(parents=True)
        print("Building in {}".format(build_temp))

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        global cmake_args
        cmake_args.extend(
            [
                f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}{os.sep}",
                f"-DPYTHON_EXECUTABLE={sys.executable}",
                f"-DCMAKE_BUILD_TYPE={cfg}",  # not used on MSVC, but no harm
            ]
        )
        build_args = []
        # Adding CMake arguments set as environment variable
        # (needed e.g. to build for ARM OSx on conda-forge)
        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        # In this example, we pass in the version to C++. You might not need
        # to.
        cmake_args += [f"-DVERSION_NR={self.distribution.get_version()}"]

        if self.compiler.compiler_type != "msvc":
            # Using Ninja-build since it a) is available as a wheel and b)
            # multithreads automatically. MSVC would require all variables be
            # exported for Ninja to pick it up, which is a little tricky to do.
            # Users can override the generator with CMAKE_GENERATOR in CMake
            # 3.15+.
            if not cmake_generator or cmake_generator == "Ninja":
                # import ninja
                # ninja_executable_path = Path(ninja.BIN_DIR) / "ninja"
                import shutil

                ninja_executable_path = shutil.which("ninja")

                if ninja_executable_path:
                    try:
                        print(
                            "Checking whether ninja can be run at {}".format(
                                ninja_executable_path
                            )
                        )
                        subprocess.run(
                            [ninja_executable_path, "--version"],
                            check=True,
                            timeout=5.0,
                            cwd=build_temp,
                        )
                        cmake_args += [
                            "-GNinja",
                            f"-DCMAKE_MAKE_PROGRAM:FILEPATH={ninja_executable_path}",
                        ]
                    except (
                        ImportError,
                        subprocess.CalledProcessError,
                        PermissionError,
                        subprocess.TimeoutExpired,
                    ):
                        warnings.warn(
                            "Ninja check did not pass, using default generator."
                        )
                        pass

        else:
            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in {"NMake", "Ninja"})

            # CMake allows an arch-in-generator style for backward
            # compatibility
            contains_arch = any(x in cmake_generator for x in {"ARM", "Win64"})

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                cmake_args += [
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"
                ]
                build_args += ["--config", cfg]

        if sys.platform.startswith("darwin"):
            # Cross-compile support for macOS - respect ARCHFLAGS if set
            archs = re.findall(r"-arch (\S+)", os.environ.get("ARCHFLAGS", ""))
            if archs:
                cmake_args += ["-DCMAKE_OSX_ARCHITECTURES={}".format(";".join(archs))]

        # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
        # across all generators.
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel is a Python 3 only way to set parallel jobs by hand
            # using -j in the build_ext call, not supported by pip or
            # PyPA-build.
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ only.
                build_args += [f"-j{self.parallel}"]

        subprocess.run(
            ["cmake", ext.sourcedir, *cmake_args], cwd=build_temp, check=True
        )
        subprocess.run(
            ["cmake", "--build", ".", *build_args], cwd=build_temp, check=True
        )


setup(
    name="simple_setup_test_py",
    version=VERSION,
    description="A test setup for C++ with Python and libraries",
    long_description_content_type="text/markdown",
    long_description=readme_content,
    keywords=["Test", "Science"],
    author="Tim Bernhard",
    author_email="tim@bernhard.dev",
    url="https://github.com/GenieTim/simple_setup_test_py",
    packages=find_namespace_packages(where="src", exclude=("tests",)),
    package_dir={"": "src"},
    include_package_data=True,
    extras_require={"test": ["unittest"]},
    python_requires=">=3.8",
    ext_modules=[CMakeExtension("pylimer_tools_cpp")],
    cmdclass={"build_ext": CMakeBuild},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
