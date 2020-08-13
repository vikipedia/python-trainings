Functions and Scope
===================


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

  def compound_interest(P, r, n, t):
      return P*(1 + r/n)**(n*t)

The result we get by using correct order of arguments is::

  >>> compound_interest(25000, 0.07, 4, 5)
  35369.454893894996

and if we give arguments in wrong order? it is way different from answer when
we give correct order::

  >>> compound_interest(0.07, 25000, 4, 5)
  5.808821324493564e+74

How do we solve this? Don't worry python has a solution for this. when in confusion
use named arguments.::

  >>> compound_interest(P=25000, n=4, t=5, r = 0.07)
  35369.454893894996

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


Namespace and Functions
-----------------------

Everytime we call a function. With entry to function, it creates it's own name
space. And in that name space it creates names for function parameters. These
names point to same location from where the pararameters are passed.


Scope of Variables
------------------
Variables defined at top level of program where main script starts are global
variables. At this level globals and locals are same. Once we call a function,
as soon as function execution starts, all variables created there are local to
that function. Variables passed as argument to function are passed by reference.
it means they refer to same object, which is passed to function. Only difference
is that it is called by a different name inside the function. This is because with
every function call a new namespace is created. And variables in function reside
in this newly created namespace. As soon as function call is over, namespace
created with function call is also deleted, so all variables in it.

Scope rules
  - Any name the statement refers, is looked in local scope first.
  - if name is not there is local scope, global scope is chacked for reading
  - if local name exists, then there is no way we can get global with same name


**Problem 3.1**

What will this print?::

  x = 10
  def foo():
      x = 20

  foo()
  print(x)

**Problem 3.2**

What will this print?::

  x = 10

  def foo():
      print(x)

  foo()

**Problem 3.3**

What will this print?::

  x = 10

  def foo():
      x = x + 1

  foo()
  print(x)

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

Similaraly how to find a record that has max gain?::

  def get_gain(r):
      return r[1]

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
