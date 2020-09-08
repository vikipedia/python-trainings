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


**Problem 1.11**
  - Write a function `transpose` to transpose the 2D list data.
  - Write a function `clockwise` to rotate tabulardata clockwise by 90 degrees.
  - Write a function `anticlockwise` to rotate tabulardata anti clockwise by 90
    degrees.

**Problem 2.1**
Write a python script `cat.py` which mimics unix command cat. Essentially cat.py
should print the contents of file to screen.::

  python3 cat.py zen.txt
  The Zen of Python, by Tim Peters

  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!

**Problem 2.2**
Write a python script `head.py` which mimics unix command head. It should show
first n lines of file passed as argument.::

  !python3 head.py 5 zen.txt
  The Zen of Python, by Tim Peters

  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.

**Problem 2.3**
Write python script `grep.py` which mimics unix command `grep`. grep searches
for given string in given files and prints those lines which contains the search
string. Use `typer` module to implement advanced option like
--invert. when --invert option is given it will print the lines which do not
have the search string.

**Problem 2.4**
Write a python script `wc.py` which mimics unix command wc. It should show line
count , word count and character count of a file.::

  !python3 wc.py zen.txt
  21 144 857 zen.txt

**Problem 2.2**
Write a python script `tail.py` which mimics unix command tail. It should show
last n lines of file passed as argument.::

  !python3 tail.py --n 5 zen.txt
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!

**Problem 3.1**
  Write a class for Stock with fields name, value, high, low and mechanism to
  update value. Updating value will also uodate max and min automatically if
  required.

**Problem 3.2**
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
                 "<>":op.ne,
                 ""  :op.eq}

      sign = "".join([s for s in cond if not s.isdigit()])
      number = int("".join([d for d in cond if d.isdigit()]))

      return cond_ops[sign], number

  def COUNTIFS(conditionlist, cond):
      func, value = cond_and_value(cond)
      return sum([1 for x in conditionlist if func(x, value)])

**Solution 1.10**::

  def factors(n):
      return [i for i in range(1, n+1) if n%i==0]

  def is_prime(p):
      return len(factors(p))==2

  def primes(n):
      return [p for p in range(1, n+1) if is_prime(p)]


**Solution 1.11**

  def column(tabulardata, n):
      """
      return nth column
      """
      return [row[n] for row in tabulardata]

  def transpose(tabulardata):
      colcount = len(tabulardata[0])
      return [column(tabulardata, c) for c in range(colcount)]

  def reversed_col(data, c):
      return list(reversed(column(data, c)))

  def rotateclockwise(data):
      colcount = len(data[0])
      return [reversed_col(data, c) for c in range(colcount)]

  def rotate_anticlock(data):
    colcount = len(data[0])
    return [column(data, c) for c in reversed(range(colcount))]
