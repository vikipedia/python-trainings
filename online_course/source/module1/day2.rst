Functions and Methods
=====================






Calling Function Vs Function
----------------------------
One has to understand defference between calling a function, defining a function
and just reffering a function. When we call a function, the arguments can be litterals
or variables. While when we define a function, arguments defined can be only variable names.
It can not be litteral while defining a function. For example this would be a mistake::

  def add(2, 3):#incorrect
      return 2+3

  def add("a", "b"):#incorrect
      return a + b

  def add("a", "b"):#incorrect
      return "a" + "b"

Correct way to define this add function is as shown below.::

  def add(a, b):
      return a + b

While calling a function::

  add(2, 3) #correct
  add(a, b) #incorrect if a and b are are not predefined.
  a = 2
  b = 3




string methods
--------------

checks

>>> startswith
>>> endswith
>>> isupper
>>> islower
>>> isalpha
>>> isalnum
>>> isdecimal
>>> isspace
>>> istitle

transforms

>>> capitalize
>>> lower
>>> upper
>>> split
>>> join
>>> rjust
>>> center
>>> ljust

trimming
>>> strip
>>> lstrip
>>> rstrip
