Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # String
>>> 
>>> # string methods
>>> # to change the case of strings
>>> 
>>> # StringName.upper() -> upper case
>>> # StringName.lower() -> lower case
>>> # stringName.capitalize() -> capitalized case
>>> 
>>> name="python is easy"
>>> 
>>> name.upper()
'PYTHON IS EASY'
>>> name
'python is easy'
>>> # the results are non-persistent
>>> # over-riding
>>> 
>>> name=name.upper()
>>> name
'PYTHON IS EASY'
>>> 
>>> name.lower()
'python is easy'
>>> name
'PYTHON IS EASY'
>>> name=name.lower()
>>> 
>>> 23456.upper()
SyntaxError: invalid syntax
>>> 
>>> 
>>> "23456".upper()
'23456'
>>> 
>>> # Method - object specific
>>> # method is applied on the object
>>> 
>>> # Function(Input)  - dir(),type(), str(234)
>>> # Input.Function() 