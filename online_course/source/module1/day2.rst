Functions and Methods
=====================

Types and Converting
^^^^^^^^^^^^^^^^^^^^
As we know variable is nothing but just a name. So if we want to know what is it
that is stored with the given name?::

  >>> name = "rupali"
  >>> type(name)
  str
  >>> numbers = [1, 2, 3]
  >>> type(numbers)
  list
  >>> point = (0, 0, 1)
  >>> type(point)
  tuple
  >>> stock = {"name":"IBM", "open":123, "high":126, "low": 120, "close":123.5}
  >>> type(stock)
  dict
  >>> type(1)
  int
  >>> type(1.2)
  float

``str`` function can be used to convert other datatypes into string.::

  >>> str("23")
  23

``int`` can be used to convert string or float to integer::

  >>> int("42")
  42

``list`` can be used to make a list from string (for that matter from any collection)::

  >>> list("1234")
  ["1","2","3","4"]
  >>> r5 = range(5)
  >>> list(r5)
  [0,1,2,3,4]
  
  
``max`` function can find maximum value from collection like list or tuple.::

  >>> max([23, 12, 34, 13, 5, 6, 12, 35])
  35

``min`` function can find minimum value from list or tuple::

  >>> min([23, 12, 34, 13, 5, 6, 12, 35])
  5

``sum`` function sums all items from a list or tuple::

  >>> sum([1, 1, 1, 1])
  4

More built in functions
-----------------------

We have seen ``max, min, sum, int, str, float, type`` functions earlier. Now let
us see some more build in functions. Usually programming in any language starts
with hello world. It is time to make python's hello world.::

  >>> print("Hello World")
  'Hello World'
  >>> print("Hello", ",", "Let's", "print", 1, 2)
  Hello , Let's print 1 2

Next we will take input from user::

  >>> x = input("Input value for x:")
  Input value for x:3
  >>> print(x)
  3

We have already seen that functions ``sum, max, min`` operate on lists. Here is
another function which works on a list. ``sorted`` takes a list or tuple and
returns sorted list.::

  >>> sorted([3,2,4,1,1])
  [1, 1, 2, 3, 4]
  >>> sorted([3,2,4,1,1], reverse=True)# this is optional argument for sorted
  [4, 3, 2, 1, 1]


  
**Problem 1.5**
  Use python to find total income if the person has five income sources giving
  income of 123330, 250000, 45555, 232130, 11123

**Problem 1.6**

  Find out how many digits are there in 2\ :sup:`42`

**Problem 1.7**

  Using python find highest income from example 1.5

**Problem 1.8**

  Will this work?::

    sum(["a","b","c","d"])


List slicing
------------

Subset of lists can be accessed nicely with something called as slicing. Here is
how slicing works.::

    list[*start*:*end*:*step*]

So if you have a list ::

  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

you want a subset of this list which starts at index 2 , till index less than 8
and at steps of two.::

  >>> digits[2:8:2]
  [2, 4, 6]
  >>> digits[2:8:3] # start at 2 end at 8 (excluded) at step of 3
  [2, 5]
  >>> digits[2:8] #start at 2 end at 8 default step of 1
  [2, 3, 4, 5, 6, 7]

Make note of these default values

  * If step is not given , it is taken as 1 by default.
  * if start is not given it is taken at 0 by default
  * if end is not given it is taken as end of string

So here are some examples of default values for start, end::

  >>> digits[:5] # take first 5
  [0, 1, 2, 3, 4]
  >>> digits[4:] # drop first 4
  [4, 5, 6, 7, 8, 9]
  >>> digits[::2] # take alternate starting at 0
  [0, 2, 4, 6, 8]
  >>> digits[::-1] # reverse the list
  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

It is posible to write complicated list slicing expressions using combination
of -ve numbers and default values. But it makes the code cryptic. So it is
advised to make use of standard list slice as shown above. These standard slices
will make your code concise but same time readable.


Creating custom functions
-------------------------

So far we have used statements. Putting few statements together for frequent use
is doen through function. Functions allow us to make black box abstraction. Its
like a box which has got some inputs and it does something on inputs and user
justs the output back. For example let's make a balck box for computing square::

  def square(x):
      return x*x

The moment we define function as given above, python creates some blackbox for
the code inside it. it stores that box in python's memory. It creates a name
``square`` in current namespace. And links this name to the black box. This is how
we call this function.::

  >>> square # this is not calling, it is just refering to name, square!
  <function __main__.square(x)>
  >>> square(4) ## <--- this is how you call the black box functionality.
  16

Let's look closely at the syntax::

  def sumofsquares(a, b): # this is where function defination starts, has to end with :
      a2 = square(a) # next line must be indented (4 spaces as a convention)
      b2 = square(b) # all lines in this code block have same indentation.
      return a1 + b2 # finally return statement

  sumofsquares(2, 3) ## here indentation comes back to original , function is over this line is outside function.

As function must have atleast one statement. There is empty statement to make
empty function.::

  def donothing():
      pass

A function can be defined without return statement too.::

  def say_hello(name):
      print("Hello ", name)

Make a note what happens if save the result of function in a variable.::

  >>> sqr5 = square(5)
  >>> print(sqr5)
  25
  >>> hello = say_hello("python")
  Hello python
  >>> print(hello)
  None


Calling Function Vs Function
----------------------------
One has to understand difference between calling a function, defining a function
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


Nested function call
--------------------

When function calls are nested, inner most function is evaluated first then next
inner most, then next ... like this till all nested function calls are over.::

  def square(x):
      return x*x

  def double(x):
      return 2*x

  def addone(x):
      return x+1

Following line will get executed as given below::

  addone(double(square(3)))
  addone(double(9)) # square is evaluated
  addone(18) # double is evaluated
  19 # addone is evaluated

**Problem 2.1**

  Net asset value, or NAV, is equal to a fund's or company's total assets less its
  liabilities. NAV is usually computed per share value for MF,ETF or closed ended
  fund. Write a function to compute NAV. Compute NAV for total assets of 25,00,00,000,
  liabilities of 30,00,000 and 1000 shares.

    >>> NAV(assets,liabilities,shares)


**Problem 2.2**

  Have a look at following python code, what will it do? Can you correct it?::

    def twice(x):
        print(2*x)

    print(twice(twice(3)))

  
