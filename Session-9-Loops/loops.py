Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ['melon','papaya','grapes','apple','cherry','banana']
>>> fruits[0]
'melon'
>>> fruits[0].capitalize()
'Melon'
>>> fruits[1].capitalize()
'Papaya'
>>> fruits[2].capitalize()
'Grapes'
>>> 
>>> # convert all the values in fruits nito upper case and add them to a seperate list
>>> fruits_upper=[]
>>> fruits[0].capitalize()
'Melon'
>>> fruits_upper.append(fruits[0].capitalize())
>>> fruits_upper
['Melon']
>>> fruits_upper.append(fruits[1].capitalize())
>>> fruits_upper.append(fruits[2].capitalize())
>>> fruits_upper
['Melon', 'Papaya', 'Grapes']
>>> 
>>> # for - loop , looping every value in a collection and apply code on it
>>> 
>>> fruits
['melon', 'papaya', 'grapes', 'apple', 'cherry', 'banana']
>>> for fruit in fruits:
	print(fruit.upper())

	
MELON
PAPAYA
GRAPES
APPLE
CHERRY
BANANA
>>> # always apply/write code onthe temp variable
>>> # make sure the tempVariable is unique
>>> 
>>> 
>>> fruit
'banana'
>>> 
>>> fruit=fruits[0]
>>> fruit.upper()
'MELON'
>>> fruit=fruits[1]
>>> fruit.upper()
'PAPAYA'
>>> fruit=fruits[2]
>>> fruit.upper()
'GRAPES'
>>> 
>>> 
>>> numbers=[9,1,8,2,7,4,7,5,2,0,1]
>>> numbers
[9, 1, 8, 2, 7, 4, 7, 5, 2, 0, 1]
>>> # add 100 to every value in the list
>>> 
>>> for num in numbers:
	print(num+100)

	
109
101
108
102
107
104
107
105
102
100
101
>>> # convert every number in numbers to string and add "$" to it
>>> # then append all converted values to a new list
>>> 
>>> newlist=[]
>>> for num in numbers:
	t=str(num)
	c="$"+t
	newlist.append(c)

	
>>> newlist
['$9', '$1', '$8', '$2', '$7', '$4', '$7', '$5', '$2', '$0', '$1']
>>> 
>>> num
1
>>> t
'1'
>>> c
'$1'
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c', 'fruit', 'fruits', 'fruits_upper', 'newlist', 'num', 'numbers', 't']
>>> newlist=[]
>>> newlist
[]
>>> 
>>> 
>>> for num in numbers:
	t="$"+str(num)
	newlist.append(t)

	
>>> newlist
['$9', '$1', '$8', '$2', '$7', '$4', '$7', '$5', '$2', '$0', '$1']
>>> 
>>> 
>>> newlist=[]
>>> newlist
[]
>>> for num in numbers:
	newlist.append("$"+str(num))

	
>>> newlist
['$9', '$1', '$8', '$2', '$7', '$4', '$7', '$5', '$2', '$0', '$1']
>>> for num in numbers:
	t=str(num)
	c="$"+t
newlist.append(c)
SyntaxError: invalid syntax
>>> 
>>> 