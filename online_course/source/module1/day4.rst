Introduction to Programming constructs
======================================

FIXME: Temporarily added here!

Styleguide for writing functions
--------------------------------

A mathematical function that computes result but prints it, is not reusable!::

  def twice(x):
      print(2*x)

  fourtimes7 = twice(twice(7)) # this will fail.

  a, b = 2, 3

  def add():
      return a+b # does not take a, b as parameter of function, not reusable!

  n = 5
  def power_(x):
      return x**n # not good practice, n is taken directly from global context.

Some guidelines to remember
  - A reusable function is perfect black box. it works only on given inputs.
  - A reusable function returns the computed value
  - A reusable function does not make use of gloabl variables.
  - A reusable function takes all that is required as argument.

Style guide
  - Give meaningful names to functions
  - Give meaningful names to variables
  - Write code to be read by humans first then by machine.

**Problem 3.4**

What will this print?::

  x = [1, 1, 1]

  def appendzero(y):
      y = y + [1]

  appendzero(x)
  print(x)


**Problem 3.5**

What will this print?::

  x = [1, 1, 1]

  def appendzero(y):
      y.append(0)

  appendzero(x)
  print(x)


Functions Arguments
-------------------

Have a look at the function::

  def say_hello(name, greeting):
      print(greeting, name + "!")

The right way to call this function is

  >>> say_hello("Vikrant", "Hello")
  Hello Vikrant!

But the user mistook the order of argumets!

  >>> say_hello("Hello", "Vikrant")
  Vikrant Hello!

Which is obviously not acceptable. It could have been some numeric computaion.
If the order of arguments is wrong, we will likely get wrong results.

  def cylinder_volume(radius, height):
      return 3.14*radius**2*height

The result we get by using correct order of arguments is::

  >>> cylinder_volume(1.0, 2.0)
  6.28

and if we give arguments in wrong order? it is way different from answer when
we give correct order::

  >>> cylinder_volume(2, 1)
  12.56

How do we solve this? Don't worry python has a solution for this. when in confusion
use named arguments.::

  >>> cylinder_volume(radius=1, height=2)
  6.28

  >>> say_hello(greeting="Namaskar", name="Vikrant")
  Namaskar Vikrant!

Also sometimes we feel need for default argumets. For example, if no greeting is
specified take it "hello" by default!::

  def say_hello(name, greeting="Hello"):
      print(name, greeting + "!")


  >>> say_hello("Vikrant")
  Hello Vikrant!
  >>> say_hello("Vikrant", greeting="Namaskar")
  Namaskar Vikrant!


Passing Functions As Arguments
------------------------------

Functions are nothing different from integers and other datatypes. Just like
integers can be stored inside a variable, same way function can also be! in fact
they are variables stored inside a variable which has name as *function name*::

  def foo:
      print("foobar!")

If we examine this variable foo::

  >>> foo
  <function __main__.foo()>
  >>> bar = foo
  >>> bar
  <function __main__.foo()>
  >> bar()
  foobar!

This means just like other variables, one should be able to pass on functions
as arguments to another functions. One way of looking at pythonish way of
programming is resuse. Never rewrite same code at two places in same program.::

  def square(x):
      return x*x

  def sumofsquares(x, y):
      return square(x) + square(y)

  def cube(x):
      return x**3

  def sumofcubes(x, y):
      return cube(x) + cube(y)

If you look closely functions `sumofsquares` and `sumofcubes` are actually same
pieces of code except the functions `square` and `cube` used in it! This is perfect
example of code repeatation. We can avoid it by writing a fucntion which abstracts
out the core idea of ``sumof``::

  def sumof(x, y , func):
      return func(x) + func(y)

With this function we can do the job of `sumofsquares` using::

  >>> sumof(2, 3, square)
  13

With the same function we can do the job of `sumofcubes`::

  >>> sumof(2, 3, cube)
  35

This idea of passing functions as argument is so useful that many python builtin
functions make use of it. For example max, min, sorted these functions have a named
parameter. We know normal working of max function::

  >>> max([3, 23, 4, 2])
  23

But what about working with some complex task like, finding max by some logic.::

  >>> words = ["one", "two", "three", "four", "five", "six"]
  >>> max(words)
  'two'

This is as we know by logic of ASCII order. but what if we want to find a word
with maximum length.::

  >>> max(words, key=len) # tell max.. how to find max... max by len!
  "three"

Suppose we have some records as given below. A record has name, value and gain::

  records = [
    ("TATA", 200.0, 5.5),
    ("INFY", 2000.0, -5),
    ("RELIANCE", 1505.5, 50.0),
    ("HCL", 1200, 70.5)
  ]

How to find a record that has max value?::

  def get_value(r):
      return r[1]

  max(records, key=get_value)
  ("INFY", 2000.0, -5)

Similarly how to find a record that has max gain?::

  def get_gain(r):
      return r[2]

  max(records, key=get_gain)
  ("HCL", 1200, 70.5)


Functions returning functions
-----------------------------
One can write a nested function as given below.::

  def make_addder(x):

      def adder(y):
          return x+y

      return adder

  >>> adder5 = make_addder(5)
  >>> adder5(11)
  16
  >>> adder5(7)
  12


lambda expression
-----------------

Following two are equivalent functions::

  def add(x, y):
      return x+y

  add = lambda x, y: x+y

very handy sometimes for experimentation during development. In production code
instead of writing lambda functions write functions with appropriate names.


Conditions
----------

We have seen boolean which has got two values ``True``, ``False``. Boleans are
results of various operators as given below

  >>> "hel" in "hello" # the in operator checks if first string is part of second string
  True
  >>> "hel" in "world!"
  False
  >>> x = "hello"
  >>> y = "hello"
  >>> x == y  #equality operator
  True
  >>> 1 in [2, 2, 2, 1, 1, 2] #checks if element 1 is in list on right
  True
  >>> 5 not in [1, 2, 3, 4] # checks if element 5 not in list on right side
  True
  >>> x , y = 5, 4
  >>> x > y
  True
  >>> x >= y
  True
  >>> y < x
  True
  >>> y <= x
  True
  >>> x != y # checks if left and right side are not equal
  True

Conditions are one of the basic building blocks of basic programming constructs.::

  if "hel" in "cell":
      print("hell!") # executed if condition of this block is True
  elif "cel" in "hell": # optional
      print("cell!") # executed if condition of this block is True
  elif "del" in "bell":
      print("dell!") # executed if condition of this block is True
  else:                 # if no condition matched, this is too optional
      print("opps!")


if the conditions have only two possiblities and simple statements, then it
is also possible to make one liner if, else statement.

  >>> cond = True
  >>> x = 2 if cond else 3
  >>> x
  2
  >>> cond = False
  >>> x = 2 if cond else 3
  >>> x

For loop
--------

To iterate over a collection you don't need to keep track of index. Just like in
english one would say ``for every_student in class`` ... to iterate over all
students in class, same way one can iterate over items in a collection in python.::

  words = ["one", "two", "three", "four", "five", "six"]

  for word in words:
      print(word, end=",")

  'one','two','three','four','five',

for loops works on strings, lists, tuples, dictionaries etc.::

  for item in {"x":1, "y":2}:
      print(item)
  x
  y


  d = {"x":1, "y":2}
  for key, value in d.items():
      print(key, value)

  x 1
  y 2
  

Example
^^^^^^^
Write our own function `mysum` which finds sum of numbers from a list::

  def mysum(nums):
      s = 0
      for n in nums:
          s = s + n
	  #s += n
      return s

  mysum(range(1,11))
  55
  
Simple Problems
^^^^^^^^^^^^^^^

**Problem 4.1**

  Write a function ``product`` which finds product of all elements from a list.

    >>> product([3, 2, 4])
    24

**Problem 4.2**

  Write a function ``factorial`` to find factorial of a number.

  >>> factorial(5)
  120

**Problem 4.3**

  Write a function ``findlens`` which finds lengths of every word from a given
  list of words.

    >>> findlens(["one", "two", "three"])
    [3, 3, 5]

**Problem 4.4**

  Write a function ``find_words_of_len`` to find words of given length from
  given list.::

    >>> find_words_of_len(words, 3)
    ['one', 'two', 'six']

**problem 4.5**

  Write a function ``generate_random`` which generates list of n random numbers::

    >>> generate_random(5)
    [0.2343,0.6545,0.2947,0.7395,0.4739]

Medium level Problems
^^^^^^^^^^^^^^^^^^^^^

**Problem 4.5**

  Write a function ``unique`` which will remove duplicates from a list.::

    >>> unique([1, 1, 2, 3, 1, 2, 3, 2, 4])
    [1, 2, 3, 4]

**Problem 4.6**

  List of urls is given. Some urls are from same domain, some are from different.
  Find unique domain names used in the urls.::

    urls = ['www.abrakadabra.com/dccEcB/EGdd',
   'www.abrakadabra.com/gADFeD/bcAF',
   'www.abra.com/AGadbb/eagE',
   'www.dabra.com/cffdfD/FCAD',
   'www.abra.com/GFGaBE/dcfc',
   'www.abra.com/gaFegG/Bdaf',
   'www.abrakadabra.com/aGabaf/EEfa',
   'www.dabra.com/ceEgFD/bGgc',
   'www.dabra.com/bDEffC/bcEA']

**Problem 4.7**

  Write a function ``min2`` which find minimum from given two numbers. Also write
  a function ``min3`` which can find minimum number from given 3 numbers. Do not
  make use of bulit in ``min`` function.


**Problem 4.8**

  Write a function ``rearramge_max`` to rearrange digits of an integer so as to
  make maximum integer from it.

    >>> rearramge_max(1312)
    3211

  
While Loop
----------

Here are few examples of using while loop::

  def print_list(items):
    i = 0
    while i < len(items):
        print(items[i], end=",")
        i += 1

  >>> numbers = [1, 2, 3, 4, 5, 6, 7]
  >>> print_list(numbers)
  1,2,3,4,5,6,7,


and here is classic fibonacci generators::

  def print_fib(n):
      """
      Print fobonacci numbers less than n
      """
      curr, prev = 1, 1

      while prev < n:
            print(prev, end=",")
            curr, prev = prev+curr, curr

  >>> print_fib(100)
  1,1,2,3,5,8,13,21,34,55,89,

The problem with ``print_list`` function defined above is that , it make use of
index to iterate over items in list. It is error prone. Many bugs creap in the
program due to bad book keeping of indices. Python provides a way out of it. To

