Assignments - Module II
=======================


**Assignment 2.1**

One year statement for a customer of a online wallet is given in CSV format.
There are five categories of expenses for that customer as food, travel, utility,
books and music. Find total yearly expense for each category of expense. The data
can be downloaded from
url="https://raw.githubusercontent.com/vikipedia/python-trainings/master/online_course/source/module2/wallet.csv"
make use of following python script in your jupyter notebook to download the
file.::

  %%file download.py
  import sys
  import requests

  def download(url, filename):
    resp = requests.get(url)
    with open(filename, "w") as f:
        f.write(resp.text)

  if __name__ == "__main__":
    url = sys.argv[1]
    filename = sys.argv[2]
    download(url, filename)

in jupyter you can use following command to download file.::

  !python3 download.py https://raw.githubusercontent.com/vikipedia/python-trainings/master/online_course/source/module2/wallet.csv wallet.csv


**Assignment 2.2**

Write a script to convert a bank statement given in qif format to CSV format.
Every transaction looks as given below. Every transcation has five items, each
item in seperate line. Item is decided from first character of line.


==================  ============
First character     meaning
==================  ============
D                   date
T                   amount
L                   category
A                   balance
M                   description
==================  ============


here is one sample entry from transcation.::

  D3/23/20
  T-435.60
  LUncategorized
  A290787.28
  MIPAY/ESHP/BD/2603301992/SIDB8647142351_AMAZON
  ^

Every transaction is seperated by one or more empty lines. Last line of
transaction is a line with character "^". First line of file tells what type of
statement it is.::

  !Type:Bank

Here is url for downloading file https://raw.githubusercontent.com/vikipedia/python-trainings/master/online_course/source/module2/statement.qif

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


**Assignment 2.4**

Financial data is given in tabular format as two dimensional list. It is a list
of rows and every row is again list of numeric or text values. Write a
function ``filter_rows`` to filter out rows such that n'th item in row is
greater than ``x``::

  >>> indexdata = [('IBM', 'Monday', 111.71436961893693),
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
  >>> n, x = 2, 225
  >>> filter_rows(indexdata, n, x)
  [('MICROSOFT', 'Monday', 235.0403622499107),
  ('MICROSOFT', 'Tuesday', 225.0206535036475),
  ('MICROSOFT', 'Friday', 235.80850482793264),
  ('APPLE', 'Monday', 321.49182055844256),
  ('APPLE', 'Tuesday', 340.63612771662815),
  ('APPLE', 'Wednesday', 303.9065277507285),
  ('APPLE', 'Thursday', 338.1350605764038),
  ('APPLE', 'Friday', 318.3912296144338)]

**Assignment 2.5**

Write classes `PortFolio` and `Stock`. Choose appropriate names for instance
variables and methods.

`PortFolio`
 - has collection of few Stocks.
 - PortFolio has name.
 - From `PortFolio` you can ask for total value of portfolio.
 - has a mechanism to get a stock of given symbol.
 - PortFolio has a facility to save PortFolio to a CSV file.
 - One can add new stocks to PortFolio.


Each `Stock` has
 - symbol,
 - value (index price)
 - volume (number of shares of this stock).
 - has a mechanism by which when printed it shows `Stock(symbol, value, volume)`
 - has a mechanism to update value
 - has a mechanism to update volume

write a `loader` function which when given CSV file saved by `PortFolio`, can
recreate new instance for PortFolio.
