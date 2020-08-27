Classes and OOPS
================

Why classes?
------------

Classes are to provide
 - facility of data encapsulation
 - controlled methods to modify data

Pitorial representation of classes::


            Instance of class
            +---------------+
            |               |<---------methods to manipulate data
            |    data       |
            |               |<---------methods
            +---------------+
                    |
                    |
                    +------<------- methods to access data



Bank Account Example
--------------------



How to write classes in python
------------------------------
If we want to model electric light in classes, we need to think of what is the
data that we would like encapsulate? We will encapsulate , whether the light is
on or not. And provide mechanism to change that state.::

                  Light
            +---------------+
            |               |<---------switch_on
            |    on=True    |
            |               |<---------switch_off
            +---------------+
               |
               |
               +------<------- is_on


Actual code for this class would look like this::

  class Light:
      "Class representation of abstract idea of Light!"

      def __init__(self):
          "Create new instance of light"
          self.on = False

      def is_on(self):
          return self.on

      def switch_on(self):
          self.on = True

      def switch_off(self):
          self.on = False

Now lets use it!::

    >>> lightA = Light() # creation of instance
    >>> lightB = Light() # another instance
    >>> lightA.is_on() # make note of missing parameter self!
    False
    >>> lightB.is_on()
    False
    >>> lightA.switch_on() # here also self need not be passed
    >>> lightA.is_on()
    True
    >>> lightB.is_on() # different instances have their own data with them
    False
    >>> lightA.switch_off()


class variables and instance variables
--------------------------------------
Suppose we want to have lights of different colors, white and green. All instances
of WhiteLight will be white is color. All instances of GreenLight will be green
in color. Once a green light is bought, it can not be changed to other color. Here
is the code to model this situation.::

  class WhiteLight:
      "Class representation of abstract idea of Light!"

      color = "white"

      def __init__(self):
          "Create new instance of light"
          self.on = False

      def is_on(self):
          return self.on

      def switch_on(self):
          self.on = True

      def switch_off(self):
          self.on = False


  class GreenLight:
      "Class representation of abstract idea of Light!"

      color = "green"

      def __init__(self):
          "Create new instance of light"
          self.on = False

      def is_on(self):
          return self.on

      def switch_on(self):
          self.on = True

      def switch_off(self):
          self.on = False

Using these classes , create instances ::

  >>> w1 = WhiteLight()
  >>> w2 = WhiteLight()
  >>> g1 = GreenLight()
  >>> w1.color
  "white"
  >>> w2.color
  "white"
  >>> g1.color
  "green"
  >>> w1.on
  False

Here `color` is called as class variable. `on` is called as instance variable.
This means `color` is stored inside class. And `on` is strored inside each
instace.


Inheritance
-----------
In above example all the functionality of basic light is same in light of any
color so why to rewrite code for each colored light? All these lights belong
to one class of object that is `Light` but with slight modification. This
can be achived using inheritance::

  class WhiteLight(Light):

      color = "white"


  class GreenLight(Light):

      color = "green"

Here `Light` is called as parent class and `WhiteLight` and `GreenLight` are
called as inherited classes.::

  >>> w = WhiteLight()
  >>> g = GreenLight()
  >>> isinstaneof(w, WhiteLight)
  True
  >>> isinstaneof(g, GreenLight)
  True
  >>> isinstaneof(w, Light)
  True
  >>> isinstaneof(g, Light)
  True

With new advances in technology , it is now possible to change color of light
with some switches. To model such light we can have something as::

  class CustomColoredLight(Light):

      def __init__(self, color="white"):
          self.color = color
          super().__init__()

      def change_color(self, color):
          self.color = color

      def get_color(self):
          return self.color


Examples - EBook
----------------
Suppose ebook reading has to be modelled using classes. Contents of book are
given as text. The reader class takes text as input and allows browsing through
book pagewsie. size of page can be fixe to 20 lines to start with.::

  class EbookReader:

      def __init__(self, contents):
          self._lines = contents.split("\n")
          self._pagesize = 20
          self._position = 0

      def get_next_page(self):
          if self._position < len(self._lines):
              page = "\n".join(self._lines[self._position:][:20])
              self._position += self._pagesize
              return page
          return ""

      def read_next_page(self):
          print(self.get_next_page())


      def go_to(self, linenum):
          if linenum >= 0 and linenum < len(self._lines):
              self._position = linenum

      def go_to_start(self):
          self.go_to(0)


We can use this book reader::

  import random
  with open("zen.txt") as f:
    lines = [line.strip() for line in f]
    booklines = [random.choice(lines) for i in range(100)]
    text = "\n".join(booklines)
    ereader = EbookReader(text)

**Problem 3.1**
  Write a class for Stock with fields name, value, high, low and mechanism to
  update value. Updating value will also uodate max and min automatically if
  required.

**Problem 3.2**
  Write classes `PortFolio` and `Stock`. `PortFolio` has collecton of few
  Stocks. Each `Stock` has symbol, value (index price) and volume (number of
  shares of this stock).  On `PortFolio` you can ask for total value of portfolio.
  and PortFolio has a facility to save PortFolio to CSV file. Is it also possible
  write a `loader` function which when given this CSV file , can recreate
  new instance for PortFolio.







- Make sure you have installed python, jupyter notebook or jupyterlab on your
  windows system before day4. Try it today so that we can discuss any issues
  tomorrow. we will need the personal installation on day5.
