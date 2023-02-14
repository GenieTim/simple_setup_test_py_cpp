include(ExternalProject)
# include(FetchContent)

# download, compile & install nlopt
# TODO: enable possibility of including externally installed nlopt library
if (NOT DEFINED nlopt_LOADED)
	if (NOT TARGET nloptLib)

		if(WIN32)
			set(LIBRARY_PREFIX "")
			set(LIBRARY_SUFFIX ".lib")
		else()
			set(LIBRARY_PREFIX "lib")
			set(LIBRARY_SUFFIX ".a")
		endif()

		ExternalProject_Add(
				nloptLib
				GIT_REPOSITORY https://github.com/stevengj/nlopt
				GIT_TAG 09b3c2a6da71cabcb98d2c8facc6b83d2321ed71 # 2.7.1
				PREFIX ${CMAKE_CURRENT_LIST_DIR}/nlopt
				INSTALL_DIR ${CMAKE_CURRENT_LIST_DIR}/nlopt/nloptLib-install
				CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_CURRENT_LIST_DIR}/nlopt/nloptLib-install -DINSTALL_LIBDIR=${CMAKE_CURRENT_LIST_DIR}/nlopt/nloptLib-install/lib -DCMAKE_INSTALL_LIBDIR=${CMAKE_CURRENT_LIST_DIR}/nlopt/nloptLib-install/lib -DNLOPT_GUILE=OFF -DNLOPT_OCTAVE=OFF -DNLOPT_MATLAB=OFF -DNLOPT_SWIG=OFF -DNLOPT_PYTHON=OFF -DBUILD_SHARED_LIBS=OFF
				BUILD_COMMAND ${CMAKE_COMMAND} --build ${CMAKE_CURRENT_LIST_DIR}/nlopt/src/nloptLib-build --config Release
				BUILD_BYPRODUCTS ${CMAKE_CURRENT_LIST_DIR}/nlopt/nloptLib-install/lib/${LIBRARY_PREFIX}nlopt${LIBRARY_SUFFIX}
				UPDATE_DISCONNECTED ON
		)
		# FetchContent_MakeAvailable(nloptLib)
		add_library(nlopt STATIC IMPORTED)
		add_dependencies(nlopt nloptLib)
		set(nlopt_PREFIX_PATH "${CMAKE_CURRENT_LIST_DIR}/nlopt")
		if (MSVC)
			set(nlopt_INCLUDE_DIRS "${nlopt_PREFIX_PATH}/nloptLib-install/include" "${nlopt_PREFIX_PATH}/src/nloptLib/msvc/include")
		else()
			set(nlopt_INCLUDE_DIRS "${nlopt_PREFIX_PATH}/nloptLib-install/include")
		endif()
		file(GLOB nlopt_LIBRARIES "${nlopt_PREFIX_PATH}/nloptLib-install/lib/${LIBRARY_PREFIX}nlopt*")
		if (NOT nlopt_LIBRARIES)
			# message("WARNING: nlopt_LIBRARIES empty")
			# TODO: this is somewhat unreliable
			set(nlopt_LIBRARIES "${nlopt_PREFIX_PATH}/nloptLib-install/lib/${LIBRARY_PREFIX}nlopt${LIBRARY_SUFFIX}")
			# file(GLOB_RECURSE nlopt_LIBRARIES "${nlopt_PREFIX_PATH}/*.a")
		endif()
		message("Hoping nlopt_LIBRARIES will be compiled to: ${nlopt_LIBRARIES}")
		set_target_properties(nlopt PROPERTIES IMPORTED_LOCATION ${nlopt_LIBRARIES})
		set(nlopt_LOADED ON)
	endif()
endif()

# find_package(nlopt REQUIRED)
# if(nlopt_FOUND)
#   include_directories(${nlopt_INCLUDE_DIRS})
#   target_link_libraries(simple_setup_test_py nlopt)
# 	message("Found nlopt for simple_setup_test_py_cpp")
# else()
# 	message(WARNING "DID NOT FIND nlopt")
# endif()
