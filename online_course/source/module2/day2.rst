Working With Files
==================

Reading Text Files
------------------
Without reading and writing files most of office automation part is not possible.
So let's see how to read text files in python. Consider a text file with
contents as given below.::

  %%file zen.txt
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

To open  file we use builtin function ``open`` and close the file using ``close``
method from filehandle::

  filename = "zen.txt"
  f = open("zen.txt"):
  for line in f: # it is possible to put for loop on file handle
      print(line)
  f.close() # remember to close the file.

This will print the contents of file to output screen.::

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

This prints extra new line for every new line in file! This is because when we
read line from a file , it also contains a new line character at end if it is
there in file. ``print`` also adds new line after every print! this can be fixed
by adding one extra parameter while printing::

  filename = "zen.txt"
  f = open("zen.txt"):
  for line in f: # it is possible to put for loop on file handle
      print(line, end=",")
  f.close() # remember to close the file.

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

Every file opened using ``open`` must be closed manually. Operating system puts
a limitation on how many files should be opened at a time. So it is a resouce
which has to be used with care. What if error happens before closing file? To
bypass all these problems there is solution provided by python, the ``with``
statement. File opened under with block will be closed automatically by python
for any case. ::

    with open("zen.txt") as f:
        for line in f:
            print(line, end=",")


With the filehandle that ``open`` returns there are few possiblities with which it
cab be operated with::

  f = open("zen.txt")
  f.readline() # will read one line and file pointer will move one line ahead
  The Zen of Python, by Tim Peters
  for line in f.readlines(): # will read all remaining lines and return as list.
      print(line, end="")

::

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

::

  f.close()
  f = open("zen.txt")
  print(f.read()) # will read complete file as a single string

::

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



**Problem 2.1**
Write a python script ``cat.py`` which mimics unix command cat. Essentially cat.py
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
Write a python script ``head.py`` which mimics unix command head. It should show
first n lines of file passed as argument.::

  !python3 head.py 5 zen.txt
  The Zen of Python, by Tim Peters

  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.

**Problem 2.3**
Write a python script ``wc.py`` which mimics unix command wc. It should show line
count , word count and character count of a file.::

  !python3 wc.py zen.txt
  21 144 857 zen.txt


**Problem 2.4**
Write a function ``csvparse`` to read following data from a CSV file.::

  file%% data.csv
  symbol,day,price
  IBM,Monday,111.71436961893693
  IBM,Tuesday,141.21220022208635
  IBM,Wednesday,112.40571010053796
  IBM,Thursday,137.54133351926248
  IBM,Friday,140.25154281801224
  MICROSOFT,Monday,235.0403622499107
  MICROSOFT,Tuesday,225.0206535036475
  MICROSOFT,Wednesday,216.10342426936444
  MICROSOFT,Thursday,200.38038844494193
  MICROSOFT,Friday,235.80850482793264
  APPLE,Monday,321.49182055844256
  APPLE,Tuesday,340.63612771662815
  APPLE,Wednesday,303.9065277507285
  APPLE,Thursday,338.1350605764038
  APPLE,Friday,318.3912296144338
  ​

After parseing the data should be in following format.::

  indexdata = [('IBM', 'Monday', 111.71436961893693),
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


Writing Text Data
-----------------

To write file we use similar approach to open file but with different mode.::

  with open("numbers.txt", "w") as f:
      for word in "one two three four five".split():
          f.write(word)
          f.write("\n")

Now lets look at whats written in file using our already built utility cat.py::

  !python cat.py numbers.txt
  one
  two
  three
  four
  five

Here are different modes in which file can be opened::

  ================   ============================================
  mode               meaning
  ================   ============================================
  no mode given      open file in text mode for reading
  ``w``              open file to write. if file exists, overrite
  ``a``              open file to append. if file exists, append
  ``rb`` or  ``b``   open file to read bibary
  ``wb``             open file in write mode to write binary.
  ``wa``             open file in bibary and append mode
  ================   ============================================


Example
-------
A text file has one item on one line. continious five lines consists of one
record. After five lines there is an empty line. ::

  symbol
  price
  change
  volume

  IBM
  123
  5.5
  1000

  XYZ
  .
  .
  .

Covert this file to make it in csv format.
  which looks like as given below::
  symbol,price,change,volume
  IBM,123,5.5,1000
  .
  .
  .

First lets us read original file. If we call it serial format, to parse this
serially written data we write a fucntion as given below.::

  def parseSerialFormat(filename):
    with open(filename) as f:
        tabular = []
        row = []
        for line in f:
            item = line.strip()
            if item:
                row.append(item)
            else:
                tabular.append(row)
                row = []
        if row:
            tabular.append(row)

    return tabular

Once we have tabular data (i.e 2D list) it is easy to write it in CSV format.::

  def writeCSV(tabular, filename):
      with open(filename, "w") as f:
          for row in tabular:
              strrow = [str(item) for item in row]
              f.write(",".join(strrow))
              f.write("\n")

String formatting
-----------------
