Modules and Scripts
===================

Modules - buit int modules
--------------------------

From statements to functions was one level of abstraction. Modules are where
related functions are kept together. Modules like functions can be recalled
later when needed. Here are two built in modules of utmost importance.::

  import os

  for path, dirs, files os.walkdir("/home/vikrant/trainig/"):
      for f in files:
          print(os.path.join(path, f))

  /home/vikrant/trainig/hello.txt
  /home/vikrant/training/hello.py
  /home/vikrant/trainig/day1.ipynb


  os.mkdir("/home/vikrant/training/test") # creates a directory
  os.mkdirs("/home/vikrant/training/test/text/x") # creates complete path


**Problem 5.1**

  Write a function ``longlistdir`` which will print filenames and folder names in a
  given folder, such that before every folder it prints a charecter d, and before
  every file it prints f.::

    >>> longlistdir("/home/vikrant/training")
    d arcesium_batch1_module1
    f notes.txt
    f hello.py
    f scratch.ipynb

**Problem 5.2**

  Write a function ``findfiles`` which finds all files in given directory
  recursively with given extension.::

  >>> findfiles("/var/")
  ['/var/log/bootstrap.log',
 '/var/log/alternatives.log',
 '/var/log/dpkg.log',
 '/var/log/apt/term.log',
 '/var/log/apt/history.log']

**Problem 5.3*

  Write a function ``dirsize`` whch finds size of a folder in MB.::

  >>> dirsize("/home/vikrant/Documents")
  728


Writing your own modules
------------------------

Your own module is nothing but a text file with extension .py . Inside this
file one writes related functions and data variables. This module can be
imported in python interpreteror or in other modules. Here is a simple module
called stats.py::

  import math

  def mean(nums):
      return sum(nums)/len(nums)

  def std(nums):
      m = mean(nums)
      s = 0
      for n in nums:
        s += (n-m)**2
      return math.sqrt(s/(len(nums)-1))

  def median(nums):
      n = len(nums)
      c = n//2
      if n%2==0:
          return (num[c] + num[c-1])/2.0
      else:
          return num[c]


This can be imported in interpreter session if the stats.py file is in same
directory. if it is in some other directory then one has to add the path of the
folder in which it resides to PYTHONPATH.::

  import stats

  print(stats.mean([1, 2, 3, 4, 5]))
  3

Writing Scripts
---------------
If we run python files as written abouve using python interpreter, we call it as
a python script. Have a look at simple python file hello.py::

  import sys

  def hello(name):
      print("Hello", name + "!")

  def welcome(name):
      hello(name)
      print("Welcome to python programming!")


  name = sys.argv[0]
  welcome(name)


if we run this script using::

  python3 hello.py



- Putting it all together
    - Building command line applications using typer/click
- Assignments - introduction

- Writing your own modules
- Distinguishing modules and scripts
