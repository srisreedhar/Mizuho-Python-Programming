Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d
{}
>>> type(d)
<class 'dict'>
>>> 
>>> fruits={
	"melon":5,
	"grapes":10,"banana":10,
	"cherry":200
	}
>>> fruits
{'melon': 5, 'grapes': 10, 'banana': 10, 'cherry': 200}
>>> len(fruits)
4
>>> fruits={
	"melon":5,
	"grapes":['red','black'],
	"banana":10,
	"cherry":200
	}
>>> 
>>> fruits
{'melon': 5, 'grapes': ['red', 'black'], 'banana': 10, 'cherry': 200}
>>> len(fruits)
4
>>> fruits={
	"melon":5,
	"grapes":{'red':100,
		  'black':200},
	"banana":10,
	"cherry":200
	}
>>> 
>>> fruits
{'melon': 5, 'grapes': {'red': 100, 'black': 200}, 'banana': 10, 'cherry': 200}
>>> len(fruits)
4
>>> 
>>> animals={
	"name":"Sleep_total",
	"Cheetah":12.1,
	"Owl Monkey":17,
	"Owl Monkey":17.17}
>>> animals
{'name': 'Sleep_total', 'Cheetah': 12.1, 'Owl Monkey': 17.17}
>>> 
>>> 
>>> 