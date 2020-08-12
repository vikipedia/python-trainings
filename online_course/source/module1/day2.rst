Functions and Methods
=====================


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


String methods
--------------

Till now we used built in functions of python. Now lets see some useful methods
from some useful datatyeps. Methods are tied to specific opjects. That way functions
are independent. Let us say we have a string stored in a variable `sentence`.::

  >>> sentence = "These Are Few Wise Words"

We have few methods in string object that allows us to do some checks::

  >>> sentence.startswith("These")
  True
  >>> sentence.startswith("This")
  False
  >>> sentence.endswith("Words")
  True
  >>> sentence.endswith("nums")
  False
  >>> sentence.isupper()
  False
  >>> sentence.islower()
  False
  >>> "alllower".islower() #can be called with litterals too.
  True
  >>> sentence.istitle()
  True
  >>> sentence.isalpha() # does it have only alphabets, no space too
  False
  >>> "onlyletters".isalpha()
  True
  >>> sentence.isalnum() # check if string has only letters and numbers
  False
  >>> "user123".isalnum()
  True


In addition to checks there are few useful transformation methods in string
object.::

    >>> "hello".capitalize()
    'Hello'
    >>> sentence.upper()
    'THESE ARE FEW WISE WORDS'
    >>> sentence.lower()
    'these are few wise words'
    >>> "hello world".title()
    'Hello World'
    >>> sentence.rjust(50)
    '                          These Are Few Wise Words'
    >>> sentence.ljust(50)
    'These Are Few Wise Words                          '
    >>> sentence.center(50)
    '             These Are Few Wise Words             '
    >>> sentence.replace("Wise", "Foolish")
    'These Are Few Foolish Words'


These two transform methods are most widely used with string processing.::

  >>> sentence.split()
  ['These', 'Are', 'Few', 'Wise', 'Words']
  >>> words = sentence.split()
  >>> "_".join(words)
  'These_Are_Few_Wise_Words'
  >>> " ".join(words)
  'These Are Few Wise Words'
  >>> "-".join(words)
  'These-Are-Few-Wise-Words'


Here are some methods that allow us to remove trainling spaces from a string.::

  >>> "   hello this has spaces to left".lstrip()
  'hello this has spaces to left'
  >>> 'and this has spaces to right        '.rstrip()
  'and this has spaces to right'
  >>> '    this has spaces on both sides     '.strip()
  'this has spaces on both sides'

Method chaining
---------------

Have a look at chain of methods called on a string.::

  sentence = "   hello method chaining!   "
  sentence.strip().split()[-1]
  ---->---->---->----->----->methods will get executed in this order

**Problem 2.1**

  On a website login only alphanumeric usernames are allowed. a string is stored
  in a variable ``username``. How will you check if username is as per rules?


**Problem 2.2**

  A sentence has hyphen between every two words.

    >>> sentence = "Yet-another-sentence-with-nothing-in-it"

  How can you transorm it such that there will be space between every two words.

**Problem 2.3**

  A a path seperator for windows operating system is

    >>> sep = "\\" # remember escape characters?

  Folder names starting from ``C:`` drive till the folder containing an executable
  'python.exe' are given in a list.

    >>> folders = ["C:", "Program Files", "python3.8"]

  How will you make a string for complete path to python.exe?

**Problem 2.4**

  A path to file is given for a linux system. on a linux system path seperator
  is "/"

    >>> path = "/home/vikrant/trainig/day1.html"

  How will you find only name of file from given path?


**Problem 2.5**

  Using string methods can you find extension of a file if filename is stored
  in a variable ``filename = "hello.xlsx"``

List methods
-------------

A lists has methods to find items in it.::

  >>> nums = [1, 2, 3, 4]
  >>> nums.index(1)
  0
  >>> nums.count(2)
  1
  >>> nums = [1, 2, 2, 3, 3, 3]
  >>> nums.count(2)
  2

It has various methods to add new items to it.::

  >>> empty = []
  >>> empty.append(1)
  >>> empty
  [1]
  >>> empty.append(1)
  >>> empty
  [1, 1]
  >>> empty.insert(0, 23) # insert 23 at location 0
  >>> empty
  [23, 1, 1]
  >>> empty.extend([0, 0, 0])
  >>> empty
  [23, 1, 1, 0, 0, 0]

It has various methods to remove items from it.::

  >>> nums = [1, 2, 3]
  >>> nums.remove(2)
  >>> nums
  [1, 3]
  >>> nums.pop() # removes last item
  3
  >>> nums
  [1]
  >>> digits = [0, 1, 2, 3, 4, 5, 6]
  >>> digits.pop(2) # removes item at location 2
  2
  >>> digits
  [0, 1, 3, 4, 5, 6]
  >>> digits.clear() # removes all elements!
  >>> digits
  []

and some other manipulations::

  >>> nums = [ 3, 2, 4, 1]
  >>> nums.sort() # sorts list inplace
  >>> nums
  [1, 2, 3, 4]
  >>> nums.reverse() # reverse inplace
  >>> nums
  [4, 3, 2, 1]
  >>> nums.copy()  ### returns a copy of list ..just as nums[:]
  [4, 3, 2, 1]


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
  >>> square(4) ## <--- this is how you call the blackbox functionality.
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

**Problem 2.6**

  Net asset value, or NAV, is equal to a fund's or company's total assets less its
  liabilities. NAV is usually computed per share value for MF,ETF or closed ended
  fund. Write a function to compute NAV. Compute NAV for total assets of 25,00,00,000,
  liabilities of 30,00,000 and 1000 shares.

    >>> NAV(assets,liabilities,shares)


**Problem 2.7**

  In financial terms a negative balance is represented with round barackets
  around the number instead of ``-`` sign. Write a function ``numeric_value``
  which returns actual numeric value. For example a value ``"(1234)"`` should
  get -1234 as numeric value. while "1234.5" will still get value as 1234.5.::

    >>> numeric_value("(35.5)")
    -35.5
    >>> numeric_value("32.5")
    32.5

**Problem 2.8**

  Have a look at following python code, what will it print? Can you correct it?::

    def twice(x):
        print(2*x)

    print(twice(twice(3)))
