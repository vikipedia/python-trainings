day5
====


- Debugging python programs
    - Tips for debugging, looking at trace, error messages to find faults
    - debugging with pdb, sample session
- Distributing libraries and packages.
    - modules
    - directory as a module
    - PYTHONPATH
    - python package
    - One sample example of creating a python package
    - stand alone script with dependencies, py2exe
    - library and usable script.


Look At Error Messages
======================
- Syntax Errors
  - variable name
  - indentation

- Common Exceptions
  - NameError
  - ValueError
    - Trying to convert invalid data
  - TypeError
    - trying to do operations with incompatible data
  - AttributError
    - Trying to access attribute which is not there
  - IndexError
    - Check index access or dictinary access


- No errors , but program is not working
 - Look whether your function has return statement and check indentation level
   the same
 - print statements
 - pdb
