
Iterations and List comprehensions
==================================

day1 - 2 hours
--------------

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

There are few things we should remeber abour `reversed` and `enumerate`. whatever
`reversed` and `enumerate` returns is for one time use. i.e it is just a mechanism
to traverse through the list just once.

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
    ('IBM', 'Friday', 140.25154281801224)]

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
