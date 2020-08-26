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
    >>> lightA.is_on()
    False
    >>> lightB.is_on()
    False
    >>> lightA.switch_on()
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


- Examples on OOPS





- Make sure you have installed python, jupyter notebook or jupyterlab on your
  windows system before day4. Try it today so that we can discuss any issues
  tomorrow. we will need the personal installation on day5.
