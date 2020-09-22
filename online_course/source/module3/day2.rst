Virtual Environment
===================
Many times it happens that different projects have requirements of python
packages such that they conflict each other. In such cases how do you work on
two different project on same machine? If we install python packages for one
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

creating evenv
--------------
To create virutal environment on your system, what you need is python
version > 3.5. Python comes with a package called venv (virtual environment).
For older python, virtualenv was seperate application. We are going to work
with virtual environment that comes with python 3. Easy steps to work with it
are as given below. Open up terminal on linux/mac or cmd terminal on windows.
on the prompt type following command to create virtual environment with name
``env1``::

  python -m venv env1

This will create a folder with name env1 in the current directory. On linux
it will have following contents::

  +-env1
    |
    +-bin
    +-include
    +-lib
    +-lib64
    +-pyenv.cfg

on windows system it will have following contents::

  +-env1
    |
    +-Include
    +-Lib
    +-Scripts
    +-pyenv.cfg


To activate virtual environment on linux run following command on terminal.::

  bash$ source env1/bin/activate
  (env1) bash$ # you can see the env1 environment activated as change in prompt

To activate virtual environment on windows run following command on windows cmd
terminal::

  C:\Users\vik> env1\bin\activate.bat
  (env1) C:\Users\vik>

Installing packages in virtual environment
------------------------------------------
Once the virtul environment is created and activated, we are ready to use it. To
install packages in this active virtual environment use ``pip install``::

  pip install typer
  Collecting typer
    Using cached https://files.pythonhosted.org/packages/90/34/d138832f6945432c638f32137e6c79a3b682f06a63c488dcfaca6b166c64/typer-0.3.2-py3-none-any.whl
  Collecting click<7.2.0,>=7.1.1 (from typer)
    Using cached https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl
  Installing collected packages: click, typer
  Successfully installed click-7.1.2 typer-0.3.2

to check packages installed ::

  pip list
  Package    Version
  ---------- -------
  click      7.1.2
  pip        19.2.3
  setuptools 41.2.0
  typer      0.3.2

requirements.txt
----------------
If we want to replicate exact same virtual environment on other machine we need
list of packages that pip can understand. The format is called as requirements
file. it can be generated using::

  pip freeze
  click==7.1.2
  typer==0.3.2

The output can be saved to a file with name requirements.txt. This file can be
used in other virtual env to recreate the same environment. For example, lets
make use of above requirements to recreate another environment with name
``env1copy``::

  bash$ python -m venv env1copy
  bash$ source env1copy/bin/activate
  (env1copy) bash$ pip install -r requirements.txt
  Collecting click==7.1.2 (from -r env1/requirements.txt (line 1))
    Using cached https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl
  Collecting typer==0.3.2 (from -r env1/requirements.txt (line 2))
    Using cached https://files.pythonhosted.org/packages/90/34/d138832f6945432c638f32137e6c79a3b682f06a63c488dcfaca6b166c64/typer-0.3.2-py3-none-any.whl
  Installing collected packages: click, typer
  Successfully installed click-7.1.2 typer-0.3.2

you can check the packages installed::

  pip freeze
  click==7.1.2
  typer==0.3.2

Summary
-------
1. Virtual environment can be created by any user. No admin privileges required.
2. Every virtual environment is stored in seperate folder.
3. Packages installed in a virtual environment are only in that particular
   virtual environment.
4. With requirements.txt it is very easy to recreate the same replica of a
   particular virtul environment.
