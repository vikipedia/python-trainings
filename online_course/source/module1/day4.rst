Introduction to Programming constructs
======================================


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
      print("hell!")
  elif "cel" in "hell": # optional
      print("cell!")
  elif "del" in "bell":
      print("dell!")
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



For loop
--------

The problem with ``print_list`` function defined above is that , it make use of
index to iterate over items in list. It is error prone. Many bugs creap in the
program due to bad book keeping of indices. Python provides a way out of it. To
iterate over a collection you don't need to keep track of index. Just like in
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


- Python modules - some built in modules os, sys

**Problem 4.9**

  Write a function ``listdir`` which will print filenames and folder names in a
  given folder, such that before every folder it prints a charecter d, and before
  every file it prints f.::

    >>> listdir("/home/vikrant/training")
    d arcesium_batch1_module1
    f notes.tex
    f hello.py
    f scratch.ipynb


- Writing your own modules
- Distinguishing modules and scripts
