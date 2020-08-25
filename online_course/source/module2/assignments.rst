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
greater than ``x``

**Assignment 2.5**

Write classes ``Workbook`` and ``Sheet`` such that Sheet consists of rows and
columns (in simple words tabular data). Sheet supports following actions.

  * it can be asked to give row count
  * it can be asked to give column count
  * it can be asked to give name of sheet
  * it can be asked to give item in m'th row and n'th column
  * it can be asked to give i'th row.

class ``Workbook`` has collection of sheets in it. It should support following
actions.

  * one can ask for name of Workbook
  * one can ask for number sheets it has
  * one can add a new sheet to it.
  * one can delete a sheet of given name from it.
  * one can ask for names of sheets in it.
  * one can ask for a sheet of given name from it.
