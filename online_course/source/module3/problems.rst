Problems
========


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
