Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> 
>>> # take a number and return the square of it
>>> num=8
>>> sr_num=num*num
>>> sr_num
64
>>> 
>>> def sqr(number):
	result=number*number
	return result

>>> sqr(2)
4
>>> sqr(8)
64
>>> sqr(89)
7921
>>> 
>>> sqr()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sqr()
TypeError: sqr() missing 1 required positional argument: 'number'
>>> 
>>> 
>>> type(sqr)
<class 'function'>
>>> 
>>> type()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> 
>>> 
>>> # create a function that takes a number and returns the
>>> # cube of the number
>>> 
>>> # create a function that takes 3 numbers and returns the
>>> # sum of 3 numbers
>>> 
>>> # create a function that takes a value and returns
>>> # the type of it
>>> 
>>> 
>>> def cube(number):
	result=number*number*number
	return result

>>> cube(2)
8
>>> cube(3)
27
>>> cube(4)
64
>>> 
>>> def total(x,y,z):
	result=x+y+z
	return result

>>> total
<function total at 0x0000004C142768B8>
>>> 
>>> total(10,10,10)
30
>>> 
>>> def typeof(value):
	return type(value)

>>> typeof(3)
<class 'int'>
>>> 
>>> typeof("   ")
<class 'str'>
>>> 
>>> 
>>> 
>>> # function that takes 3 args and returns the 3 values as it
>>> 
>>> def someNme(a,b,c):
	return a,b,c

>>> someNme(1,2,3)
(1, 2, 3)
>>> 
>>> someNme("python","is","awesome")
('python', 'is', 'awesome')
>>> 
>>> def someNme(a,b,c):
	return [a,b,c]

>>> someNme(1,2,3)
[1, 2, 3]
>>> 
>>> 
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'cube', 'num', 'someNme', 'sqr', 'sr_num', 'total', 'typeof']
>>> cube(2)
8
>>> two=cube(2)
>>> two
8
>>> three=cube(3)
>>> three
27
>>> 
>>> c=someNme(1,2,3)
>>> c
[1, 2, 3]
>>> 
>>> c
[1, 2, 3]
>>> c
[1, 2, 3]
>>> 
>>> def cube(number):
	result=number*number*number
	return result

>>> def cube(number):
	result=number*number*number
	print(result)

	
>>> def cube(number):
	result=number*number*number
	return result

>>> cube(5)
125
>>> five=cube(5)
>>> five
125
>>> 
>>> 
>>> def cube(number):
	result=number*number*number
	print(result)

	
>>> cube(5)
125
>>> five=cube(5)
125
>>> five
>>> five
>>> five
>>> type(five)
<class 'NoneType'>
>>> 
>>> # function that does nothing
>>> def dummy():
	return pass
SyntaxError: invalid syntax
>>> 
>>> def dummy():
	return None

>>> dummy
<function dummy at 0x0000004C14276678>
>>> dummy()
>>> 
>>> 
>>> 