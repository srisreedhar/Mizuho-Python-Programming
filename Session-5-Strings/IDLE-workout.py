Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age=input("-->")
-->10
>>> age
'10'
>>> new_age=int(age)
>>> new_age
10
>>> age=int(age)
>>> age
10
>>> type(str(1111))
<class 'str'>
>>> 
>>> age=int(input("Enter a number -->"))
Enter a number -->60
>>> age
60
>>> age=int(input("Enter a number -->"))
Enter a number -->10.500
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    age=int(input("Enter a number -->"))
ValueError: invalid literal for int() with base 10: '10.500'
>>> age=int(input("Enter a number -->"))
Enter a number -->sreedhar
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    age=int(input("Enter a number -->"))
ValueError: invalid literal for int() with base 10: 'sreedhar'
>>> 
>>> age=input("-->")
-->4444
>>> age
'4444'
>>> 
>>> 
>>> # prints
>>> 
>>> print("what a beautiful morning this is")
what a beautiful morning this is
>>> 
>>> print("This is line 1
      
SyntaxError: EOL while scanning string literal
>>> print("""This is line 1
this is line 2
this is line 3



this is ine4""")
This is line 1
this is line 2
this is line 3



this is ine4
>>> 
>>> print("it is raining here")
it is raining here
>>> 
>>> print('its raining here')
its raining here
>>> 
>>> print('it's raining here')
      
SyntaxError: invalid syntax
>>> print("it's raining here")
it's raining here
>>> 
>>> 
>>> print('''
Hi,
Good Morning
Could you ask''',"sreedhar",''' to forward me
the ''',5,"th","video")

Hi,
Good Morning
Could you ask sreedhar  to forward me
the  5 th video
>>> 
>>> 
>>> 
>>> # string formatters
>>> # placeholders of values in print
>>> 
>>> # %s -> strings
>>> # %d -> Integers
>>> # %f -> floats
>>> # %r -> raw strings
>>> 
>>> 
>>> # " %placeHOlder1 ....... %placeholder2... %placeholder3"%(value1,value2,value3)
>>> 
>>> " His name is %s he is %s years old "%("Python",15)
' His name is Python he is 15 years old '
>>> 
>>> 
>>> " His name is %s he is %s years old "%(15,"Python")
' His name is 15 he is Python years old '
>>> 
==== RESTART: C:/Users/User/Desktop/Mizuho/Programs/Session-5-/input-formating.py ===
Enter your name: sreedhar
Enter your year of birth: 2010
Enter your qualification: mba

Hi,

below are thedetails you've entered :

your Name is : sreedhar ,
your year of Birth is : 2010 ,
your Qualification is : mba
>>> 