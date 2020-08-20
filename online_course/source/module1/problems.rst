Problems
========

Seeing numbers in different world
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem 1.1**

  Use python to convert asset value originally given in EUR to INR.

**Problem 1.2**

  Compount interest is calculated using formula P (1 + r/n)\ :sup:`nt`
  For this formula, ``P`` is the principal amount, ``r`` is the rate of interest
  per annum, ``n`` denotes the number of times in a year the interest gets
  compounded, and t denotes the number of years. Use python to compute compound
  interest for principle amount of 26780, rate of interest 7%, interest is
  compounded 4 quarterly, and amount is invested for 5 years.

**Problem 1.3**

  Have a look at following python statements. ::

    x = 10
    y = x
    x = x + 10

  What will be value of y?

**Problem 1.4**

  What will be value of x after executing all statements?::

    x = 10
    y = x
    y = 25

**Problem 1.5**
  Use python to find total income if the person has five income sources giving
  income of 123330, 250000, 45555, 232130, 11123

**Problem 1.6**

  Find out how many digits are there in 2\ :sup:`42`

**Problem 1.7**

  Using python find highest income from example 1.5

**Problem 1.8**

  Will this work?::

    sum(["a","b","c","d"])


**Problem 2.1**

  Net asset value, or NAV, is equal to a fund's or company's total assets less its
  liabilities. NAV is usually computed per share value for MF,ETF or closed ended
  fund. Write a function to compute NAV. Compute NAV for total assets of 25,00,00,000,
  liabilities of 30,00,000 and 1000 shares.

    >>> NAV(assets,liabilities,shares)


**Problem 2.2**

  In a financial terms a negative balance is represented with round barackets
  around the number instead of ``-`` sign. Write a function ``numeric_value``
  which returns actual numeric value. For example a value ``"(1234)"`` should
  get -1234 as numeric value. while "1234.5" will still get value as 1234.5.::

    >>> numeric_value("(35.5)")
    -35.5
    >>> numeric_value("32.5")
    32.5


**Problem 3.1**

  Govt. has decided to categorize business firms into following categories based
  on their quarterly turnover. Write a function ``firm_category`` which tells the
  category of business if quarterly turnover is given.::

    ========    ==================================
    category    turnover
    ========    ==================================
    tiny        less than 7 digits
    medium      more than 6 and less than 9 digits
    large       more than 9 digits
    ========    ==================================

**Problem 3.2**

  Use python to find name of company whoose share value is max. Share values for
  different companies are are as below::

    HCL 1200
    INFOSYS 2500
    TATA 400
    WIPRO 1800

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
