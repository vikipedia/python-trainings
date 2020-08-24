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

To open  file we use builtin function `open` and close the file using `close`
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
there in file. `print` also adds new line after every print! this can be fixed
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

Every file opened using `open` must be closed manually. Operating system puts
a limitation on how many files should be opened at a time. So it is a resouce
which has to be used with care. What if error happens before closing file? To
bypass all these problems there is solution provided by python, the `with`
statement. File opened under with block will be closed automatically by python
for any case. ::

    with open("zen.txt") as f:
        for line in f:
            print(line, end=",")

- Writing to text files
- String formatting
