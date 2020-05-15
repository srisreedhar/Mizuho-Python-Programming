Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sum([1,2,3,4,5,6,7,8,9,10])
55
>>> 
>>> def nothing(*args):
	return args

>>> nothing()
()
>>> nothing(1,2)
(1, 2)
>>> nothing(1,2,3,4,5,6,7,8,9,10)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> 
>>> def plus(*numbers):
	total=0
	for number in numbers:
		total=total+number
	return total

>>> plus
<function plus at 0x000000098E83E948>
>>> plus(1)
1
>>> plus(1,2)
3
>>> plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
55
>>> # pass multiple strings and join them together
>>> 
>>> # and return a sentence
>>> 
>>> 
>>> 
>>> def simint(p,t,r):
	'''
p -> principle
t -> time
r -> rate
formula -> (ptr)/100'''
	return (p*t*r)/100

>>> def simint(p,t,r):
	'''
	p -> principle
	t -> time
	r -> rate
	formula -> (ptr)/100
	'''
	return (p*t*r)/100

>>> def simint(p,t,r):
	"""
	p -> principle
	t -> time
	r -> rate
	formula -> (ptr)/100
	"""
	return (p*t*r)/100

>>> 
>>> 