Problems
========


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
  - Write a function `factors` which finds all factors of given number (include 1
    and self)
  - Write a function `is_prime` which checks if given number is prime based on
    fact that prime number has only two factors 1 and self.
  - Write a list comprehension to generate prime numbers less than n.

**Problem 2.1**
A text file has one item on one line. continious five lines consists of one
record. After five lines there is an empty line. ::

  symbol
  name
  price
  change
  volume

  Parse this file to make a table
  which looks like as given below::

  ====== ==== =====
  symbol name price



Solutions
=========

**Solution 1.4**::

  def merge(first, second):
      return sum([[a,b] for a,b in zip(first, second)], [])

**Solution 1.5**::

    >>> "".join([x.upper() if i%2==0 else x.lower() for i,x in enumerate("abrakadabra")])
    >>> "".join(["".join([x, y]) for x, y in zip(s[::2], s[1::2].upper())]) #smart but looks complex!

**Solution 1.8**::

  def increament(strnum):
    return str(int(strnum) + 1)

  def correct_time(date):
    dt, t = date.split()
    if "24:" in t:
        y, m, d_ = dt.split("-")
        d_ = increament(d_)
        return " ".join(["-".join([y, m, d_]), t.replace("24:","00:")])
    else:
        return date

  [(correct_time(dt), x, y) for dt, x, y in records]

**Solution 1.9**::

  import operator as op

  def cond_and_value(cond):
      cond_ops = {">":op.gt,
                 ">=":op.ge,
                 "<" :op.lt,
                 "<=":op.le,
                 "<>":op.ne}

      for condkey in cond_ops:
          if cond.startswith(condkey):
              if len(condkey)==1 and ("=" in cond or ">" in cond):
                  continue

              _, value = cond.split(condkey)
              return cond_ops[condkey], int(value)
      return op.eq, int(cond)

  def COUNTIFS(conditionlist, cond):
      func, value = cond_and_value(cond)

      return sum([1 for x in conditionlist if func(x, value)])
