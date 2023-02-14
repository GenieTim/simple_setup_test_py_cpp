Installation
============

You can use PyPip to install this package:

.. code:: bash

  python -m pip install simple_setup_test_py

NOTE: 
  depending on your OS and Python environment, you may require an installation of some dependencies.
  In this case, a custom compilation could be a workaroud.
  Checkout the following sections for your system. 

Manual Compilation
===================

MacOS / Unix systems
---------------------

Please make sure to have a current version of `git`_ installed before following the next steps.
A complete script to install this library including all dependencies could look like this:

.. code:: bash

  git clone https://github.com/GenieTim/simple_setup_test_py simple_setup_test_py
  python -m pip install ./simple_setup_test_py

To update the custom installation, follow the steps below:

.. code:: bash
  
  cd simple_setup_test_py
  git pull
  python -m pip install .

Windows
--------

Please make sure to have a current version of `Visual Studio`_ as well as `git`_ installed before following the next steps.
A complete PowerShell script to install this library including all dependencies could look like this:

.. code:: bash

  git clone https://github.com/GenieTim/simple_setup_test_py simple_setup_test_py
  python -m pip install .\simple_setup_test_py

To update the custom installation, follow the steps below:

.. code:: bash

  cd simple_setup_test_py
  git pull
  python -m pip install .


.. _git: https://www.git-scm.com/
.. _Visual Studio: https://visualstudio.microsoft.com/
