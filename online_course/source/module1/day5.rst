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

**Problem 5.3**

  Write a function ``dirsize`` whch finds size of a folder in MB.::

    >>> dirsize("/home/vikrant/Documents")
    728

Here is one more important module ::

  import random
  random.random() # returns a random number between 0-1
  random.choice([1, 2, 3, 4, 5]) # will randomly select one item from list
  random.shuffle([1, 2, 3, 4, 5]) # shuffle list and return nothing



Working with dates is made easy with datetime module.::

  d1 = datetime.datetime(2020, 11, 20)
  d2 = datetime.datetime.today()

  d2 > d1
  False
  d1 > d2
  True
  d1 + datetime.timedelta(1)
  datetime.datetime(2020, 11, 21, 0, 0)

**Problem 5.4**

  Write a function `greeting` which greets randomly in variaus ways::

    >>> greeting("Vikrant")
    "Hello Vikrant"
    >>> greeting("Vikrant")
    "Namaste Vikrant"
    >>> greeting("Vikrant")
    "Good day Vikrant"
    >>> greeting("Vikrant")
    "Guten morgen Vikrant"


**Problem 5.5**

  Write a function `trange` which generates `n` dates from start date. if start
  is not given , today is taken as start date.::

    >>> trange(5, datetime.datetime(2019, 1, 1))
    [datetime.datetime(2019, 1, 1, 0, 0),
     datetime.datetime(2019, 1, 2, 0, 0),
     datetime.datetime(2019, 1, 3, 0, 0),
     datetime.datetime(2019, 1, 4, 0, 0),
     datetime.datetime(2019, 1, 5, 0, 0)]


Writing your own modules
------------------------

Your own module is nothing but a text file with extension .py . Inside this
file one writes related functions and data variables. This module can be
imported in python interpreter or in other modules. Here is a simple module
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

  %%file hello.py
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
  Hello vikrant!
  Welcome to python programming!

Lets put some prints to understand how sys.argv works::

  %%file hello.py
  import sys

  def hello(name):
      print("Hello", name + "!")

  def welcome(name):
      hello(name)
      print("Welcome to python programming!")

  print("sys.argv arguments -> ", sys.argv)
  name = sys.argv[1]
  welcome(name)

Now if we run the script with some arguments::

  !python3 hello1.py vikrant kfddf saghjg hgshjg khdfjgdsf
  sys.argv arguments ->  ['hello1.py', 'vikrant', 'kfddf', 'saghjg', 'hgshjg', 'khdfjgdsf']
  Hello vikrant!
  Welcome to python programming!

sys.argv is list of commandlines arguments populated by python like a magic
variable. All the parameters we pass from commandline are populated in this
list automaticaly by python. Argument at index 0 is always script name. So real
arguments to script start from index 1. Also note that all commandline arguments
are always text, even if we pass numeric values.::

  !python3 hello1.py vikrant 23 1.1 jkhdfj kdjhfk
  sys.argv arguments ->  ['hello1.py', 'vikrant', '23', '1.1', 'jkhdfj', 'kdjhfkd']
  Hello vikrant!
  Welcome to python programming!

So if we have to write a script that works on numeric arguments, it is script's
responsiblity to convert the data to appropriate type. e.g.::

  %%file add.py
  import sys

  def add(x, y):
    return x+y


  a = int(sys.argv[1])
  b = int(sys.argv[2])

  print(add(a, b))

Runing this from command line::

  !python3 add.py 343 4343
  4686

But wait, lets try to make use of this as module in interpreter!::

  >>> import add
  ValueError                                Traceback (most recent call last)
  <ipython-input-114-81459ef23ada> in <module>
  ----> 1 import add

  ~/trainings/2020/arcesium_finop_batch1_module1/add.py in <module>
        5
        6
  ----> 7 a = int(sys.argv[1])
        8 b = int(sys.argv[2])
        9

  ValueError: invalid literal for int() with base 10: '-f'

To fix this lets observe value of a magic variable `__name__`. To see this we
will add a print statement in above file add.py::

  %%file add.py
  import sys

  def add(x, y):
    return x+y


  print(__name__)
  a = int(sys.argv[1])
  b = int(sys.argv[2])

  print(add(a, b))

If we run this as script from commandline::

  python add.py 2 3
  __main__
  5

if we import this module from interpreter::

  >>> import add
  add
  ---------------------------------------------------------------------------
  ValueError                                Traceback (most recent call last)
  <ipython-input-118-5ffa442179a0> in <module>
  ----> 1 import add1

  ~/trainings/2020/arcesium_finop_batch1_module1/add1.py in <module>
        6
        7 print(__name__)
  ----> 8 a = int(sys.argv[1])
        9 b = int(sys.argv[2])
       10

  ValueError: invalid literal for int() with base 10: '-f'

So this magic variable `__name__` has value `"__main__"` when we run this file
as script. On the other hand when import this file as module this magic variable
`__name__` has value `"add"`, i.e. name of module! We can make use of this fact
that irrespective what module it is , when we run the script from commandline,
value of `__name__` is always `"__main__"`. We can use this thing to control
behavior script while running script. For example use of sys.argv is useful
only while running the module as script. so sys.argv should be accessed only if
`__name__` is `"__main__"`::

  %%file add2.py
  import sys

  def add(x, y):
    return x+y


  print("__name__ = ", __name__)
  if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(add(a, b))




- Putting it all together
    - Building command line applications using typer/click
- Assignments - introduction

- Writing your own modules
- Distinguishing modules and scripts
