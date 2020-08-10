Functions and Programming Constructs
====================================



Namespace and Functions
-----------------------

Everytime we call a function. With entry to function, it creates it's own name
space. And in that name space it


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
functions make use of it.

- Functions returning functions
- Introduction to Programming constructs
    - conditions,
    -  loops
