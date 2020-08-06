Introduction To Programming
===========================

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
This character when printed will become newline or carriage return.

String works with some opeartors just like numbers.::

  >>> "*"*5
  '*****'
  >>> "hello" + "world"
  'helloworld'


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
  >>> "vikrant"
  'vikrant'
  >>> vikrant
  10

here ``vikrant`` is different from ``'vikrant'``. ``vikrant`` is variable and
``'vikrant'`` is litteral string.

What can be used as variable name has some rules.

  * The variable name can't start with number
  * It can be single word (meaning no space or hyphen allowed.)
  * It can have alphabets, numbers and underscore

Now lets work slightly more with strings. Now that we can store strings in a variable,
let's store text data in a variable and play with it.

  >>> s = "hello"

We can

  >>> s[0] # 0th character in string
  'h'
  >>> s[4]
  'o'
  >>> s[-1] # last character
  'o'

Collections
-----------
Other than basic data types we feel need of collecting basic data types together
to form an array of sequencially arranged items. List is varsatile higher level
data type which alllows us to keep any number of items, sequencially.

  >>> [1, 1, 1]
  [1,1,1]
  >>> ["hello", "these", "are","words"]
  ['hello', 'these', 'are', 'words']
  >>> [1, "word", 2]





- Statements
- Functions
