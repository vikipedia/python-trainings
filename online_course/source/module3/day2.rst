Virtual Environment
===================
Many times it happens that different projects have requirements of python
packages such that they conflict each other. In such cases how do you work on
two differen project on same machine? If we install python packages for one
project, those packages will confict with other projects. Virtual environment
is there to help us. Virtual environment allows us to have set of python
packages seperately for each project. Also added advantage is, it won't affect
system python's packages. The way to handle this is with help of ``venv`` module
we create virtual environment for each project. All requirements for the proejct
are installed in the virtual environment and not in system python's packages.
Let's take some examples.

Conflicting Requirements
------------------------

Suppose we have two projects, ``datascraping`` and  ``analytics``. For
``datascraping`` project requirements are following packages::

  requests==2.24.0
  openpyxl==2.4.8

and ``analytics`` project needs following packages::

  pandas==1.1.2
  openpyxl==3.0.5
  requests==2.24.0

Now here is confiliting requirement, one project needs openpyxl verson 2.4.8
and other needs 3.0.5.






- Managing virtual environments
  - creating evenv
  requests==
  - activation

  - installing
  - pip freeze
  - pip install -r requirements.txt


- Using third party libraries (installing, accessing , managing etc.)


pip search
pip install
pip uninstall
pip list


**Problem**
  Install `typer` module to your system
