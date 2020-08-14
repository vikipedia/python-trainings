Assignments - Module I
======================

These assignments have to be solved at http://lab1/pipal.in
login with your username and credentials. create a notebook with name
`module1-assignment.ipynb`. Submit your solutions on or before 20th august.


**Assignment 1.1**

Write a python script ``mean.py`` which finds mean of all numbers that are
passed as command line arguments.

**Assignment 1.2**

Daily average prices of some symbols are given each for five days. Write a
function to compute weekly average for given symbol using this data.::

  prices = [('IBM', 'Monday', 111.71436961893693),
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

**Assignment 1.3**

Write a function to create a single list from given lists. In other words write
a function ``flatten`` which creates a one dimensional list from two dimensional
list.

  >>> [[1,2,3],[4,5,6],[7,8,9]]

should create a list

  >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]


**Assignment 1.4**

A title of a novel is given in small case as a string. Write a python script
called ``titlecase.py`` which converts this string such that first letter of
every word is in upper case.::

  !python3 titlecase.py programming adventures of a nonprogrammer
   Programming Adventures Of A Nonprogrammer

**Assignment 1.5**

Write a python function ``findfiles`` to find out all filenames which start with
a given prefix and have given extension from given folder. sample run of
function will be as given below::

  >>> folderpath = "somefolderpath"
  >>> prefix = "Equitydata_jun"
  >>> extension = ".xlsx"
  >>>  findfiles(folderpath, prefix, extension)
  ["Equitydata_jun01.xlsx",
  "Equitydata_jun02.xlsx",
  "Equitydata_jun03.xlsx",
  .
  .
  .]

**Assignment 1.6**

Implement excel function SUMIFS as a function in python.
SUMIFS(sum_list, criteria_list, condition). Here first argument is the list on
which sum will be performed. Second argument is the list on which condition is
checked, and third argument is condition as a string , as in excel.

  | "<" --------- less than
  | "<="--------- less than or equal to
  | ">" --------- greater than
  | ">="--------- greater than or equal to
  | "<>"--------- not equal to

Sample run is shown below::

  >>> d = [1,2,3,4,5,4,4,5]
  >>> a = [10,20,30,40,50,40,40,50]
  >>> SUMIFS(d, a, "<40")
  6
  >>> SUMIFS(d, a, ">=40")
  22
  >>> SUMIFS(d, a, "40")
  12
  >>> SUMIFS(d, a, "<>40")
  16


**Assignment 1.7**

There is a database which has record of few stock indices with symbol, name,
last price, change, volume. in volume B stands for billion and M stands for
million::

  indexdata = [
  ("GSPC", "S&P 500", 3257.30, 5.46, "2.472B"),
  ("DJI", "Dow Jones Industrial Average", 26840.40, 159.53, "367.24M"),
  ("IXIC", "NASDAQ Composite", 10680.36, -170.73, "682.685M"),
  ("NYA", "NYSE COMPOSITE (DJ)", 12508.68, 115.70, "0"),
  ("BUK100P", "Cboe UK 100 Price Return", 623.03, -1.54, "0")]

Using python how will you find a row with maximum change? also find a row with
maximum volume. Also sort this record by volume.
