Introduction To Python Programming
==================================

What is programming?
--------------------

Consider following sentences in different languages.

- दोन आणि पाच गुणाकार करा आणि आपल्या नोटबुकमध्ये परिणाम लिहा
- రెండు మరియు ఐదు గుణించి, మీ నోట్‌బుక్‌లో ఫలితాన్ని రాయండి
- இரண்டு மற்றும் ஐந்தைப் பெருக்கி, உங்கள் நோட்புக்கில் முடிவை எழுதுங்கள்
- બે અને પાંચને ગુણાકાર કરો અને તમારી નોટબુકમાં પરિણામ લખો
- দুই এবং পাঁচটি গুণান এবং আপনার নোটবুকের ফলাফল লিখুন
- दो और पांच गुणा करें और अपनी नोटबुक में परिणाम लिखें
- multiply two and five and write result in your notebook

When you read it what do you do? These are instructions for you to think and
act. Similarly 'programs' are instructions for computer to think and act.
Languages that humans speak have wide spectrum right from very primitive to
advanced one. Similarly computers also have wide spectrum of languages primitives
to advanced. Instructions in humans language can be regorous and plenty to do
simple tasks. And there can be few elegant and poetic sentences which can
inspire people to think and act in complicated and challening senarios.
Here we are going to learn poetic, pythonish way of writing programs which
will inspire machines to do seemingly complicated jobs.

Installation
------------

Before we start programming, let's get ready with the tools that we need for
python programming. We will need python with appropriate version installed on
our system. Thoughout the tutorial we will be using python 3.7 or more. You can
install python basic from python.org or you can get a python from anaconda with
a whole bunch of packages deafult with it.



Numeric And Text data
---------------------

Very primitive way of looking at **Programming** is manipulating numbers and
text. To manipulate numbers python has got basic numeric compabilities. Python
interpreter can be directly used as calculator::

  >> 42 + 42 # text after # is a comment
  84
  >> 42 - 42
  0
  >> 42 * 2 # multiplication
  84
  >> 5 / 2 # real number division
  2.5
  >> 5 // 2 # integer division
  2
  >> 2**5 # 2 raised to power 5!
  32
  >> 5 % 2 # remainder when divided by 2
  1

Numeric data in python has two forms , integers and real numbers. Real numbers
are represented by something called as ``float`` in python. floats have decimal
point in it while integers do not have decimal.::

  >>> 1.1 + 1.1
  2.2
  >>> 1.0 - 0.1
  0.9
  >>> 1.0 * 2
  2.0
  >>> 5.0 / 2
  2.5
  >>> 5.0 // 2.0
  2.0
  >>> 2.0 ** 5
  32.0

These symbols ``+``, ``-``, ``*``, ``**``, ``/``, ``//`` are called as operators.
And calculator commands above are called statements. Two or more operators can
be used in single statement. When two operators come in single statement , there is
predefined hirarchy or precedence. Here is list arranged from highest precedence to
lowest precedence operator.

  ============   ========
  operators      priority
  ============   ========
  ``**``         1
  ``% // / *``   2
  ``+ -``        3
  ============   ========

Have a look at following expressions carefully and find out whats the answer.
Can you think of steps involved? which operator will be evaluated first and whats
the sequence in which all of the operators in expression will be evaluated?

  >>> 2**5%5/2*7
  >>> 32%5/2*7
  >>> 2/2*7
  >>> 1.8*7
  >>> 7.0

Also observe how round braces change the precedence of operations. If one wants
to give precedence to some operation which is in low precedence from above table,
then we make use of braces to change the precedence. For example::

  >>> 7 + 2*3
  13
  >>> (7+2)*3
  27

Now that we know how to calculate, lets do some book keeping with text data.
Python supports text data in the from of very useful data type ``string``.
Anything enclosed in single quote ``'`` or  double quote ``"`` is ``string``
or text data in python. These are examples::

  >>> "Hello this is text"
  "Hello this is text"Data
  >>> 'And this is also text'

Python supports multiline text too. As we will learn later python allows all
those things which makes your code look more human readable. Anything that is
enclosed in triple quotes is multiline string.::

  >>>"""This is first line of my poem
  ... This is second line
  ... This is third line"""
  'This is first line of my poem\nThis is second \nand this s third line'
  >>>'''This is first line of my poem
  ... This is second line
  ... This is third line'''
  'This is first line of my poem\nThis is second \nand this s third line'

Make note of this special character ``\n``. This is called as newline character.
This character when printed will become newline or carriage return. Special
characters are escaped with this special charecter ``\``, for example.::

  ===========    =========
  escape char    meaning
  ===========    =========
  ``\n``         new line
  ``\t``         tab
  ``\\``         \
  ===========    =========

String works with some opeartors just like numbers.::

  >>> "*"*5
  '*****'
  >>> "hello" + "world"
  'helloworld'

**Problem 1.1**

  Use python to convert asset value, 20345.5 originally given in EUR to INR.

**Problem 1.2**

  Compount interest is calculated using formula P (1 + r/n)\ :sup:`nt`
  For this formula, ``P`` is the principal amount, ``r`` is the rate of interest
  per annum, ``n`` denotes the number of times in a year the interest gets
  compounded, and t denotes the number of years. Use python to compute compound
  interest for principle amount of 26780, rate of interest 7%, interest is
  compounded 4 quarterly, and amount is invested for 5 years.

Variables and literals
----------------------

In addition to arithmatic operators that we saw earlier there is a special operator
called assignment operator ``=``. It works like this. Suppose you write a statement
which involves assignment operator.

  >>> x = 10

This results in creation of object for integer 10. which will be stored in python's
memory space. Next it creates a name called ``x`` in something called as
active namespace. Then it connects this name ``x`` with the location in python's
memory where 10 is stored. Now magical thing happens due to this namespace.
whenever we type ``x`` we get::

  >>> x
  10

wow! so we stored the value in something which can be recalled with name ``x``.
This is called as variable. Till now we were talking about litterals.::

  >>> 10
  10

This is litteral. while what we see below is Variable::

  >>> x
  10

Be carefull with string litterals.::

  >>> vikrant = 10
  >>> "vikrant" # not a variable
  'vikrant'
  >>> vikrant
  10

here ``vikrant`` is different from ``'vikrant'``. ``vikrant`` is variable and
``'vikrant'`` is litteral string.

What can be used as variable name has some rules.

  * The variable name can't start with number
  * It can be single word (meaning no space or hyphen allowed.)
  * It can have alphabets, numbers and underscore

The assignment operator also allows us to assign multiple values at a time.::

  >>> a, b = 2, 3
  >>> a
  2
  >>> b
  3

**Problem 1.3**

  Have a look at following python statements. ::

    x = 10
    y = x
    x = x + 10

  What will be value of y after this?

**Problem 1.4**

  What will be value of x after executing all statements?::

    x = 10
    y = x
    y = 25


Now lets work slightly more with strings. Now that we can store strings in a variable,
let's store text data in a variable and play with it.

  >>> s = "hello"

We can access elements from this string with integer indices. Index starts at 0 and
goes till length minus one.

  >>> s[0] # 0th character in string
  'h'
  >>> s[4]
  'o'
  >>> s[-1] # last character
  'o'

Indices work as shown below.::

   +---+---+---+---+---+---+
   | P | y | t | h | o | n |
   +---+---+---+---+---+---+
   0   1   2   3   4   5   6
  -6  -5  -4  -3  -2  -1



Collections
-----------
Other than basic data types we feel need of collecting basic data types together
to form an array of sequencially arranged items. List is varsatile higher level
data type which allows us to keep any number of items, sequencially.::

  >>> [1, 1, 1]
  [1,1,1]

You can save any similar basic datatypes, or data of different types together in a list::

  >>> numbers = [1, 2, 3, 4]
  >>> words = ["hello", "these", "are","words"]
  >>> words
  ['hello', 'these', 'are', 'words']
  >>> mixed = [1, "word", 2]
  >>> mixed
  [1, "word", 2]

You can actually save lists inside list too.::

  >>> [['a','b','c'], 1, 2, [1, 1, 1]]
  [['a','b','c'], 1, 2, [1, 1, 1]]

You can access elements from a list with it's index. Lists are nothing but arraging
objects in a serial manner. Every item will have unique index, first one starting
at index zero. If index more than length -1 is given , python will throw error::

  >>> words[0]
  'hello'
  >>> words[2]
  'are'
  >>> words[3]
  'words'
  >>> words[-1]
  'words'
  >>> words[5]
  ---------------------------------------------------------------------------
  IndexError                                Traceback (most recent call last)
  <ipython-input-19-f6a2fb6dbef1> in <module>
  ----> 1 words[5]

  IndexError: list index out of range

Lists also support modification inplace. For example in a list we can go and
change element at specific index.::

  >>> words
  ['hello', 'these', 'are', 'words']
  >>> words[3] = "elements"
  >>> words
  ['hello', 'these', 'are', 'elements']

Just like strings , our lists support ``+`` and ``*`` operators.::

  >>> [1, 1]*3
  [1, 1, 1, 1, 1, 1]
  >>> [1, 1] + [0, 0]
  [1, 1, 0 , 0]

There is a sibling of list, called tuple. It is exactly similar to list except ,
it can not be modified like lists.::

  >>> color = (0, 0, 256)
  >>> color[0]
  0
  >>> color[-1]
  256
  >>> color + color
  (0, 0, 256, 0, 0, 256)
  >>> color * 2
  (0, 0, 256, 0, 0, 256)
  >>> color[0] = 100
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-31-6f0411612089> in <module>
  ----> 1 color[0] = 100

  TypeError: 'tuple' object does not support item assignment

Lists and tuples allow us to save items by location, i.e by index we can access items.
But there is one more interesting hogher level datatype called dictinary. Dictionary allows
to save items in a collection with a name. In a small classroom it is more natural
to call out students by name than roll number (index!)::

  >>> scorebyname = {"rupali":20, "alice":19, "maya":18, "kavya":20}
  >>> scorebyname['rupali']
  >>> scorebyname['kavya']
  >>> scorebyname['seema']
  ---------------------------------------------------------------------------
  KeyError                                  Traceback (most recent call last)
  <ipython-input-36-350bc8d22721> in <module>
  ----> 1 scorebyname['seema']

  KeyError: 'seema'
  >>> scorebyname['seema'] = 15
  >>> scorebyname
  {'rupali': 20, 'alice': 19, 'maya': 18, 'kavya': 20, 'seema': 15}
  >>> scorebyname['seema']
  15

Here is another example of dictionary::

  >>> stock = {"name":"IBM", "open":123, "high":126, "low": 120, "close":123.5}
  >>> stock['open']
  123


Boolean
-------

There are boolean types supported in python

  >>> True
  >>> False

Functions
---------
Now that basic and some higher level data types are known to us and statements as well,
lets see functions. Function is nothing but collections of statememnts put together to
do more complex task. For time being we will see some built in functions in python.
``len`` is one function which we will be using a lot. Function call consists of
calling a function with some arguments. argumets are some data on which function
will operate and try to calculate some value or try to perform some operation.
For example ``len`` is used to find length of any collection as well as of string.
let's say we have a string stored in a variable ``name``. we want to find length of
string stored inside ``name``. To do this we call function ``len`` with ``name``
as argument to it.::

  >>> name = "Rupali"
  >>> len(name)
  6
  >>> numbers = [1, 1, 2, 2, 1]
  >>> len(numbers)
  5
  >>> point = (0, 0, 2)
  >>> len(point)
  3
  >>> stock = {"name":"IBM", "open":123, "high":126, "low": 120, "close":123.5}
  >>> len(stock)
  6

Types and Converting
^^^^^^^^^^^^^^^^^^^^
As we know variable is nothing but just a name. So if we want to know what is it
that is stored with the given name?::

  >>> name = "rupali"
  >>> type(name)
  str
  >>> numbers = [1, 2, 3]
  >>> type(numbers)
  list
  >>> point = (0, 0, 1)
  >>> type(point)
  tuple
  >>> stock = {"name":"IBM", "open":123, "high":126, "low": 120, "close":123.5}
  >>> type(stock)
  dict
  >>> type(1)
  int
  >>> type(1.2)
  float

``str`` function can be used to convert other datatypes into string.::

  >>> str("23")
  23

``int`` can be used to convert string or float to integer::

  >>> int("42")
  42

``max`` function can find maximum value from collection like list or tuple.::

  >>> max([23, 12, 34, 13, 5, 6, 12, 35])
  35

``min`` function can find minimum value from list or tuple::

  >>> min([23, 12, 34, 13, 5, 6, 12, 35])
  5

``sum`` function sums all items from a list or tuple::

  >>> sum([1, 1, 1, 1])
  4

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


List slicing
------------

Subset of lists can be accessed nicely with something called as slicing. Here is
how slicing works.::

    list[*start*:*end*:*step*]

So if you have a list ::

  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

you want a subset of this list which starts at index 2 , till index less than 8
and at steps of two.::

  >>> digits[2:8:2]
  [2, 4, 6]
  >>> digits[2:8:3] # start at 2 end at 8 (excluded) at step of 3
  [2, 5]
  >>> digits[2:8] #start at 2 end at 8 default step of 1
  [2, 3, 4, 5, 6, 7]

Make note of these default values

  * If step is not given , t is taken as 1 by default.
  * if start is not given it is taken at 0 by default
  * if end is not given it is taken as end of string

So here are some examples of default values for start, end::

  >>> digits[:5] # take first 5
  [0, 1, 2, 3, 4]
  >>> digits[4:] # drop first 4
  [4, 5, 6, 7, 8, 9]
  >>> digits[::2] # take alternate starting at 0
  [0, 2, 4, 6, 8]
  >>> digits[::-1] # reverse the list
  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

It is posible to write complicated list slicing expressions using combination
of -ve numbers and default values. But it makes the code cryptic. So it is
advised to make use of standard list slice as shown above. These standard slices
will make your code concise but same time readable.
