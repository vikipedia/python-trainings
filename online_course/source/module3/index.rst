
Module III
==========

Module-III goes beyond basics and covers some advanced utilities where you will
learn manipulating tabular data with ease. Also some basics of data scraping,
python packaging , debuging , managing virtual environments etc. will be
covered.



Pandas as excel utility
-----------------------

Consider following excel functions::

    d = [1,2,3,4,5,4,4,5]
    a = [10,20,30,40,50,40,40,50]

    assert SUMIFS(d, a, "<40") == 6
    assert SUMIFS(d, a, "<=40") == 18
    assert SUMIFS(d, a, ">40") == 10
    assert SUMIFS(d, a, ">=40") == 22
    assert SUMIFS(d, a, 40) == 12
    assert SUMIFS(d, a, "<>40") == 16


How can we do this with pandas?

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   problems.rst
   project.rst
