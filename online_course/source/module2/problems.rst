Problems
========

**Problem 1.1**

  There is a string "abrakadabra", we want to capitalize alternate character from it.
  how can we do it? can a list comprehension be used to do this?

**Problem 1.3**

  There are two lists

    >>> a = [1, 2, 3]
    >>> b = ['a', 'b', 'c']

  write a function ``merge`` which will merge the lists into a single list such that
  alternatively one item from first list and one item from second list is taken.
  e.g for above case the merge should result in::

    >>> merge(a, b)
    [1, 'a', 2, 'b', 3, 'c']



**Problem 1.2**
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


**Problem 2.2**

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
  >>> SUMIFS(a, "<40")
  3
  >>> SUMIFS(a, ">=40")
  5
  >>> SUMIFS(a, "40")**Problem 1.2**

  Write a function ``flatten`` which flattens 2 dimentional list into one
  dimensional list. it should work like this::

    >>> flatten([[1,2,3], ['a','b','c']])
    [1, 2, 3, 'a', 'b', 'c']
  3
  >>> SUMIFS(a, "<>40")
  5

Solutions
=========

**Solution 1.1**

    >>> "".join([x.upper() if i%2==0 else x.lower() for i,x in enumerate("abrakadabra")])

**Solution 1.2**::

  def merge(first, second):
      return sum([[a,b] for a,b in zip(first, second)], [])
