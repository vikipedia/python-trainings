
Iterations and List comprehensions
==================================


Iteration patterns
------------------
For loops in python allows us going through the entire collection without leting
us fall in trap of index errors. Sometimes if we need to go over the collection
in different fashion, for example want to acess items in reversed way.::

  for i in reversed(range(5)):
      print(i, end=",")

  4,3,2,1,0

and sometimes we also need index with every item::

  poem = """Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts."""

  lines = poem.split("\n")

  for i, line in enumerate(lines):
      print(i+1, line)

  1 Beautiful is better than ugly.
  2 Explicit is better than implicit.
  3 Simple is better than complex.
  4 Complex is better than complicated.
  5 Flat is better than nested.
  6 Sparse is better than dense.
  7 Readability counts.

sometimes we need to go over multiple collections together!::

  firstname = ["Alice", "Elsa", "Alex", "Elisa"]
  lastname = ["Wondergirl", "Frozen", "Lion", "Hacker"]
  for name, surname in zip(firstname, lastname):
      print(name, surname)

  Alice Wondergirl
  Elsa Frozen
  Alex Lion
  Elisa Hacker

We can go over as many lists as possible::

  xs = ["x1", "x2", "x3", "x4"]
  ys = ["y1", "y2", "y3", "y4"]
  zs = ["z1", "z2", "z3", "z4"]

  for x, y, z in zip(xs, ys, zs):
      print(x, y, z)
  x1 y1 z1
  x2 y2 z2
  x3 y3 z3
  x4 y4 z4

There are few things we should remember abour `reversed` and `enumerate`. whatever
`reversed` and `enumerate` returns is for one time use. i.e it is just a mechanism
to traverse through the list just once.::

  r = reversed(range(5))
  for i in r:
      print(i, end=",")

  0,1,2,3,4

  for i in r:
      print(i, end=",")

The second for loop will not print anything. Also it is not possible to find
length of reversed or enumerate iterator::

  len(reversed([1, 2, 3]))
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-8-11c939ffc16b> in <module>
  ----> 1 len(reversed([1, 2, 3, 4]))

  TypeError: object of type 'list_reverseiterator' has no len()


**Problem 1.1**
  Write a function vector_add, which does vector addition of two vectors taken
  as lists.::

    >>> vector_add([1, 1, 1], [3, 4, 5])
    [4, 5, 6]

**Problem 1.2**
  A matrix is called unit matrix if all elements except diagonal elements in
  every row are 0 and diagonal elements as 1. Write a function to check if given
  matrix is unit matrix or not?::

    >>> m = [[1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1]]
    >>> is_unit_matrix(m)
    True
    >>> is_unit_matrix([[1, 2],[2, 1]])
    False

**Problem 1.3**
  A poem is given in variable `poem`. Write a function `inverted` to print poem
  in such fashion that last line is printed first, then second last, continue
  like things and finally at last prints first line.::

    >>> poem = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts."""

    >>> inverted(poem)
    Readability counts.
    Sparse is better than dense.
    Flat is better than nested.
    Complex is better than complicated.
    Simple is better than complex.
    Explicit is better than implicit.
    Beautiful is better than ugly

**Problem 1.4**
  There are two lists

    >>> a = [1, 2, 3]
    >>> b = ['a', 'b', 'c']

  write a function ``merge`` which will merge the lists into a single list such that
  alternatively one item from first list and one item from second list is taken.
  e.g for above case the merge should result in::

    >>> merge(a, b)
    [1, 'a', 2, 'b', 3, 'c']


List Comprehensions
-------------------
We can see some pattern in following loops::

  def findlens(words):
      lens = []
      for word in words:
          lens.append(len(word))

      return lens

  def squares(nums):
      sqrs = []
      for n in nums:
          sqrs.append(n*n)

      return sqrs

  import datetime
  def trange(n):
      """
      generates next n dates starting from today
      """
      dates = []
      start = datetime.datetime.today()
      for i in range(n):
          dates.append(start + datetime.timedelta(days=i))

      return dates

All these functions are basically creating a new list from original list with
some operation on each element. They all can be converted simple one liners::

    def findlens(words):
        return [len(word) for word in words]

    def squares(nums):
        return [x*x for x in nums]

    def trange(n):
        return [datetime.datetime.today() + datetime.timedelta(days=i) for i in range(n)]


General form of list comprehension is ::

  newitem = []
  for item in olditems:
      newitem.append(do_something(item))

translates to ::

  newitems = [do_something(item) for item in olditems]


Filtering lists on some conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Other than simple mapping operation we do filtering operation while creating a
new list. Here are few exmaples::

  def even(x):
      return x%2==0

  def evens(nums):
      e = []
      for n in nums:
          if even(n):
              e.append(n)
      return e

  def find_words_of_len(words, n):
      words_of_len = []
      for w in words:
          if len(w) == n:
              words_of_len.append(w)
      return words_of_len


this can be written using list comprehension as simple one liners::

  def evens(nums):
      return [n for n in nums if even(n)]

  def find_words_of_len(words, n):
      return [w for w in in words if len(w)==n]


We can combine mapping and filtering.::

  newlist = []
  for item in oldlist:
      if cond(item):
          newlist(do_operation(item))

is equivalent to ::

  newlist = [do_operation(item) for item in oldlist if cond(item)]

For example we want to find squares of even numbers only!::

  nums = [1, 2, 3, 4, 5, 6, 7]
  [x*x for x in nums if even(x)]
  [4, 16, 36]

Lets look at slightly complicated problem.
Consider prices of stocks given in following format. WE want to find all items
for given symbol lets say `"IBM"`::

  indexdata = [('IBM', 'Monday', 111.71436961893693),
            ('IBM', 'Tuesday', 141.21220022208635),
            ('IBM', 'Wednesday', 112.40571010053796),
            ('IBM', 'Thursday', 137.54133351926248),
            ('IBM', 'Friday', 140.25154281801224),
            ('MICROSOFT', 'Monday', 235.0403622499107),
            ('MICROSOFT', 'Tuesday', 225.0206535036475),
            ('MICROSOFT', 'Wednesday', 216.10342426936444),
            ('MICROSOFT', 'Thursday', 200.38038844494193),
            ('MICROSOFT', 'Friday', 235.80850482793264),
            ('APPLE', 'Monday', 321.49182055844256),
            ('APPLE', 'Tuesday', 340.63612771662815),
            ('APPLE', 'Wednesday', 303.9065277507285),
            ('APPLE', 'Thursday', 338.1350605764038),
            ('APPLE', 'Friday', 318.3912296144338)]

Without list compreshension we would do it as given here::

  IBMdata = []
  for index in indexdata:
      if index[0]=="IBM":
          IBMdata.append(index)

  print(IBMdata)
  [('IBM', 'Monday', 111.71436961893693),
    ('IBM', 'Tuesday', 141.21220022208635),
    ('IBM', 'Wednesday', 112.40571010053796),
    ('IBM', 'Thursday', 137.54133351926248),
n    ('IBM', 'Friday', 140.25154281801224)]

With list comprehension for this piece of code reduces to single line.::

  [index for index in indexdata if indexdata[0]=="IBM"]
  [('IBM', 'Monday', 111.71436961893693),
    ('IBM', 'Tuesday', 141.21220022208635),
    ('IBM', 'Wednesday', 112.40571010053796),
    ('IBM', 'Thursday', 137.54133351926248),
    ('IBM', 'Friday', 140.25154281801224)]

What if We want only price of stock for symbol `"IBM"`?::

  [price for symbol, day, price in indexdata if symbol=="IBM"]

So how do we find weekly average for given symbol?::


  def mean(nums):
      return sum(nums)/len(nums)

  def prices(indexdata, symbol):
      return [price_ for symbol_, day_, price_ in indexdata if symbol_==symbol]

  def weeklyaverage(indexdata, symbol):
      return mean(prices(indexdata, symbol))

  weeklyaverage(indexdata, "APPLE")
  324.51215324332736

**Problem 1.5**
  write function listpy (just like os.listdir!) which uses list comprehension to
  identify py files in given directory.::

    >>> listpy(os.getcwd())
    add.py
    add1.py
    add2.py
    hello.py

**Problem 1.6**
  find sum of all multiples of 7 or 11 below 1000.

**Problem 1.7**
  There is a string "abrakadabra", we want to capitalize alternate character from it.
  how can we do it? can a list comprehension be used to do this?

**Problem 1.8**
  Some records are stored with timestamp in database as shown below.::

    records = [("2018-11-11 24:04","11803","16602"),
                ("2018-11-11 24:09","11782","16568"),
                ("2018-11-11 24:14","11741","16524"),
                ("2018-11-11 24:19","11756","16543"),
                ("2018-11-11 24:24","11741","16538"),
                ("2018-11-11 24:28","11722","16558"),
                ("2018-11-11 24:34","11716","16457"),
                ("2018-11-11 24:39","11724","16430"),
                ("2018-11-11 24:44","11723","16572"),
                ("2018-11-11 24:49","11739","16611"),
                ("2018-11-11 24:54","11740","16501"),
                ("2018-11-11 24:58","11743","16568"),
                ("2018-11-12 01:04","11754","16626")]

  The timestamp given above has been misprinted, instead of 11th Nov 24:04 ,
  it should be 12 Nov 00:04! Write a function to correct the record. use list
  comprehension to do this.

**Problem 1.9**

  Implement excel function COUNTIFS as a function in python.
  COUNTIFS(criteria_list, condition). Here first argument is the list on
  which count will be performed. Second argument is condition as a string ,
  as in excel.

    | "<" --------- less than
    | "<="--------- less than or equal to
    | ">" --------- greater than
    | ">="--------- greater than or equal to
    | "<>"--------- not equal to

  Sample run is shown below::

    >>> a = [10,20,30,40,50,40,40,50]
    >>> COUNTIFS(a, "<40")
    3
    >>> COUNTIFS(a, ">=40")
    5
    >>> COUNTIFS(a, "40")
    >>> COUNTIFS(a, "<>40")
    5

**Problem 1.10**
  - Write a function factors which finds all factors of given number (include 1
    and self)
  - Write a function is_prime which checks if given number is prime based on
    fact that prime number has only two factors 1 and self.
  - Write a list comprehension to generate prime numbers.

**Problem 1.11**
  - Write a function `transpose` to transpose the 2D list data.
  - Write a function `clockwise` to rotate tabulardata clockwise by 90 degrees.
  - Write a function `anticlockwise` to rotate tabulardata anti clockwise by 90
    degrees.
