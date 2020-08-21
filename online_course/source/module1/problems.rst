Problems
========


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

  On a website login only alphanumeric usernames are allowed. a string is stored
  in a variable ``username``. How will you check if username is as per rules?


**Problem 2.2**

  A sentence has hyphen between every two words.

    >>> sentence = "Yet-another-sentence-with-nothing-in-it"

  How can you transorm it such that there will be space between every two words.

**Problem 2.3**

  A a path seperator for windows operating system is

    >>> sep = "\\" # remember escape characters?

  Folder names starting from ``C:`` drive till the folder containing an executable
  'python.exe' are given in a list.

    >>> folders = ["C:", "Program Files", "python3.8"]

  How will you make a string for complete path to python.exe?

**Problem 2.4**

  A path to file is given for a linux system. on a linux system path seperator
  is "/"

    >>> path = "/home/vikrant/trainig/day1.html"

  How will you find only name of file from given path?


**Problem 2.5**

  Using string methods can you find extension of a file if filename is stored
  in a variable ``filename = "hello.xlsx"``

**Problem 2.6**

  Net asset value, or NAV, is equal to a fund's or company's total assets less its
  liabilities. NAV is usually computed per share value for MF,ETF or closed ended
  fund. Write a function to compute NAV. Compute NAV for total assets of 25,00,00,000,
  liabilities of 30,00,000 and 1000 shares.

    >>> NAV(assets,liabilities,shares)


**Problem 2.7**

  In a financial terms a negative balance is represented with round barackets
  around the number instead of ``-`` sign. Write a function ``numeric_value``
  which returns actual numeric value. For example a value ``"(1234)"`` should
  get -1234 as numeric value. while "1234.5" will still get value as 1234.5.::

    >>> numeric_value("(35.5)")
    -35.5
    >>> numeric_value("32.5")
    32.5

**Problem 2.8**

  Have a look at following python code, what will it print? Can you correct it?::

    def twice(x):
        print(2*x)

    print(twice(twice(3)))

**Problem 3.1**

  What will this print?::

    x = 10
    def foo():
        x = 20

    foo()
    print(x)

**Problem 3.2**

  What will this print?::

    x = 10

    def foo():
        print(x)

    foo()

**Problem 3.3**

  What will this print?::

    x = 10

    def foo():
        x = x + 1

        foo()
    print(x)

**Problem 3.4**

  What will this print?::

    x = [1, 1, 1]

    def appendzero(y):
        y = y + [1]

    appendzero(x)
    print(x)


**Problem 3.5**

  What will this print?::

    x = [1, 1, 1]

    def appendzero(y):
        y.append(0)

    appendzero(x)
    print(x)


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


**Problem 5.1**

  Write a function ``longlistdir`` which will print filenames and folder names in a
  given folder, such that before every folder it prints a charecter d, and before
  every file it prints f.::

    >>> longlistdir("/home/vikrant/training")
    d arcesium_batch1_module1
    f notes.txt
    f hello.py
    f scratch.ipynb

**Problem 5.2**

  Write a function ``findfiles`` which finds all files in given directory
  recursively with given extension.::

    >>> findfiles("/var/")
    ['/var/log/bootstrap.log',
    '/var/log/alternatives.log',
    '/var/log/dpkg.log',
    '/var/log/apt/term.log',
    '/var/log/apt/history.log']

**Problem 5.3**

  Write a function ``dirsize`` whch finds size of a folder in MB.::

    >>> dirsize("/home/vikrant/Documents")
    728

**Problem 5.4**

  Write a function `greeting` which greets randomly in variaus ways::

    >>> greeting("Vikrant")
    "Hello Vikrant"
    >>> greeting("Vikrant")
    "Namaste Vikrant"
    >>> greeting("Vikrant")
    "Good day Vikrant"
    >>> greeting("Vikrant")
    "Guten morgen Vikrant"


**Problem 5.5**

  Write a function `trange` which generates `n` dates from start date. if start
  is not given , today is taken as start date.::

    >>> trange(5, datetime.datetime(2019, 1, 1))
    [datetime.datetime(2019, 1, 1, 0, 0),
     datetime.datetime(2019, 1, 2, 0, 0),
     datetime.datetime(2019, 1, 3, 0, 0),
     datetime.datetime(2019, 1, 4, 0, 0),
     datetime.datetime(2019, 1, 5, 0, 0)]
