dictionary
==========

what is a decorator
-------------------
::

  def suqare(x):
      return x*x

  def decor(f):

      def wrapper(*args, **kwargs):
          print("Debug ... before ", f.__qaulname__)
          r = f(*args, **kwargs)
          print("Debug .... after ", f.__qaulname__)
          return r

      return wrapper


  square(2)
  4
  square = decor(square)
  square(2)
  Debug ... before square
  Debug ... after square
  4

  @decor
  def add(a, b):
      return a+b


Example - Complex Vs Simple
---------------------------
Look at two COUNTIFS functions and lets learn from it. Here is first one::

  import operator as op

  def cond_and_value(cond):
    """
    find appropriate operator for given condition
    and find the number part from condtion
    """
    cond_ops = {
        ">=" :op.ge,
        "<>":op.ne,
        "<=" :op.le,
        ">":op.gt,
        "<":op.lt,
        }
    for condkey in cond_ops:
        if cond.startswith(condkey):
            #if len(condkey)==1 and ("=" in cond or ">" in cond):
            #   continue
            _, value = cond.split(condkey)
            return cond_ops[condkey], int(value)
    return op.eq, int(cond)

  def COUNTIF(conditionlist, cond):
    func, value = cond_and_value(cond)
    return len([item for item in conditionlist if func(item, value)])

Here is another one::

  def countifs(criteria_list, condition):
    number = int("".join([character for character in condition if character.isdigit()]))
    sign = "".join([sign for sign in condition if not sign.isdigit()])
    if sign =='<':
        count = len([value for value in criteria_list if value<number])
    elif sign =='<=':
        count = len([value for value in criteria_list if value<=number])
    elif sign =='>':
        count = len([value for value in criteria_list if value>number])
    elif sign =='>=':
        count = len([value for value in criteria_list if value>=number])
    elif sign =='':
        count = len([value for value in criteria_list if value==number])
    elif sign =='<>':
        count = len([value for value in criteria_list if value!=number])
    else:
        print("Please check your inputs")
    return count

Here is refined solution::

  import operator as op

  def cond_and_value(cond):
    """
    find appropriate operator for given condition
    and find the number part from condtion
    """
    cond_ops = {
        ">=" :op.ge,
        "<>" :op.ne,
        "<=" :op.le,
        ">"  :op.gt,
        "<"  :op.lt,
        ""   :op.eq
        }

    number = int("".join([character for character in cond if character.isdigit()]))
    sign = "".join([sign for sign in cond if not sign.isdigit()])

    return cond_ops[sign], number

  def COUNTIF(conditionlist, cond):
    func, value = cond_and_value(cond)
    return len([item for item in conditionlist if func(item, value)])


Also see a function generating prime numbers::

  def primes(n):
      p = []
      for i in range(1,n):
          prime = True
          for j in range(2,i):
              if i%j==0:
                  prime = False
                  break
          if prime:
              p.append(i)
      return p

Now lets break it up using basic defination of prime number! A prime number has
no factor other than 1 and itself.(for time lets count 1 as factor!)::

  def factors(n):
      return [f for f in range(1, n+1) if n%f==0]

  def is_prime(p):
      return factors(p)==[1,p]

  def primes(n):
      return [p for p in range(1, n+1) if is_prime(p)]

string formatting
-----------------
  - format
  - columns
  - "*" triangle
  - pascal triangle

- Working with Dictionaries
  - get
  - values, keys, items
  - dictionary comprehension

    1. with zip::

        >>> names = ['APPLE', 'IBM', 'AT&T', 'AGILENT']
        >>> values = [700.5, 300.1, 355.7, 600.3]
        >>> {name:value for name, value in zip(names, values)}
        {'APPLE': 700.5, 'IBM': 300.1, 'AT&T': 355.7, 'AGILENT': 600.3}

    alternatively::

        >>> dict(zip(names, values))

    2. Extracting a Subset of a Dictionary
        prices = {'APPLE': 700.5,
                  'IBM': 300.1,
                  'AT&T': 355.7,
                  'AGILENT': 600.3}

        p1 = { key:value for key, value in prices.items() if value > 400 }
        # Make a dictionary of subset
        few_names = { 'APPLE', 'IBM' }
        p2 = { key:value for key,value in prices.items() if key in few_names }

  - word count
  - sorting item in dict, histogram example

Some useful patterns
--------------------

- Finding commonalities in two dictionaries::

    a.keys() & b.keys() # common keys in a and b
    { 'x', 'y' }
