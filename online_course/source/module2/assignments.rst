Assignments
===========

**Assignment 2.1**

One year statement for a customer of a online wallet is given in CSV format.
There are five categories of expenses for that customer as food, travel, utility,
books and music. Find total yearly expense for each category of expense.

**Assignment 2.2**

See wikipedia page for `qif` file format. Write a script to convert a bank
statement given in qif format to CSV format. Every transaction looks as
given below::

  D3/23/20
  T-435.60
  N
  P
  SNo
  LUncategorized
  A290787.28
  V3/23/20
  MIPAY/ESHP/BD/2603301992/SIDB8647142351_AMAZON


**Assignment 2.3**
Convert following loops into list/dictionary comprehensions

  1::

    mat = []
    for c in range(5):
      row = []
      for r in range(5):
          if c==r:
            row.append(1)
          else:
            row.append(0)
      mat.append(col)

  2::

    r = []
    for row in data:
        if row[0] == "IBM":
          r.append(row[2])

  3::

    caps = []
    for word in words:
      caps.append(word.capitalize())

  4::

    weekly = {}
    for t in ["IBM","MICROSOFT","APPLE"]:
      a = weeklyaverage(prices, t)
      weekly[t] = a
