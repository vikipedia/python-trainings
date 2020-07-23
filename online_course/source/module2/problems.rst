Problems
========

**Problem 2.1**

A text file has one item on one line. continious five lines consists of one
record. ::

  symbol
  name
  price
  change
  volume

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
  >>> SUMIFS(a, "40")
  3
  >>> SUMIFS(a, "<>40")
  5
