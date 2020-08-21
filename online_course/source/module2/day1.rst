
Iterations and List comprehensions
==================================

day1 - 2 hours
--------------

Iteration patterns
------------------
For loops in python allows us going through the entire collection without leting
us fall in trap of index errors. Sometimes if we need to go over the collection
in different fashion, for example want to acess items in reversed way.::

  for i in reversed(range(5)):
      print(i, end=",")

  4,3,2,1,0

and sometimes we also need index with every item::

  poem = """Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts."""

  lines = poem.split("\n")

  for i, line in enumerate(lines):
      print(i+1, line)

  1 Beautiful is better than ugly.
  2 Explicit is better than implicit.
  3 Simple is better than complex.
  4 Complex is better than complicated.
  5 Flat is better than nested.
  6 Sparse is better than dense.
  7 Readability counts.

sometimes we need to go over multiple collections together!::




- list comprehensions
    - Mapping one list to another list
    - Filtering lists on some conditions
