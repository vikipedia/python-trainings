Introduction To Python Programming
==================================

What is programming?
--------------------

Consider following sentences in different languages.

- दोन आणि पाच गुणाकार करा आणि आपल्या नोटबुकमध्ये उत्तर लिहा
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
to advanced. Instructions in humans language can be rigorous and plenty to do
simple tasks. And there can be few elegant and poetic sentences which can
inspire people to think and act in complicated and challenging scenarios.
Here we are going to learn poetic, pythonish way of writing programs which
will inspire machines to do seemingly complicated jobs.

Installation
------------

Before we start programming, let's get ready with the tools that we need for
python programming. We will need python with appropriate version installed on
our system. Throughout the tutorial we will be using python 3.7 or more. You can
install python basic from ``python.org`` or you can get a python from anaconda with
a whole bunch of packages default with it.


First Steps - Running python
-------------------------------
There are various ways you can run python. Simplest option is to go to 
commandline tool of your system. For Linux and Mac Os it is terminal,
for Windows it is cmd. Open up commandline , type `python` and enter.



Working with jupyter notebook
-----------------------------
Another fancy way of programming python is jupyter notebook. once you launch
jupyter from console or from start menu, a browser will be launched.
Create a new notebook. To work with notebook you need to know few key strokes.

  ===========   ====================================
  keys          action                              
  ===========   ====================================
  esc+m         convert the cell to markdown        
  esc+y         convert the cell to code            
  shift+enter   execute the cell                   
  !command      execute system command from jupyter 
  ===========   ====================================


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
characters are escaped with this special charecter ``\``, for example.

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

  Compound interest is calculated using formula P (1 + r/n)\ :sup:`nt`
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
This is called as variable. Till now we were talking about literals.::

  >>> 10
  10

This is a literal. while what we see below is Variable::

  >>> x
  10

Be carefull with string literals.::

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

There are boolean types supported in python which has only two possible literal
values

  >>> True
  >>> False

Key things to remembers
-----------------------

- to make a list we make use square brackets []
- to make a string we make use of single or double quotes
- to make a tuple we make use of round brackets ()
- to make a dictionary we make use of curley brackets {}, inside you have to give key:value pairs separated by comma


- to access item from a string we use square bracket and integer index inside that string[2]
- to access item from a list we use square bracket and integer index inside that list[2]
- to access item from a tuple we use square bracket and integer index inside that tuple[2]
- to access item from a dictionary we use square bracket and key inside that d['key']to make a dictionary we make use of curley brackets {}, inside you have to give

  
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

..  LocalWords:  pythonish
