Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> avengers=['ironman','spidey','spuerman','Mr.bean','AquaMan']
>>> avengers
['ironman', 'spidey', 'spuerman', 'Mr.bean', 'AquaMan']
>>> avengers.append("Sreedhar")
>>> 
>>> avengers
['ironman', 'spidey', 'spuerman', 'Mr.bean', 'AquaMan', 'Sreedhar']
>>> 
>>> avengers.remove('spuerman')
>>> avengers
['ironman', 'spidey', 'Mr.bean', 'AquaMan', 'Sreedhar']
>>> 
>>> avengers.pop()
'Sreedhar'
>>> avengers
['ironman', 'spidey', 'Mr.bean', 'AquaMan']
>>> s=avengers.remove('spuerman')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s=avengers.remove('spuerman')
ValueError: list.remove(x): x not in list
>>> s=avengers.pop()
>>> s
'AquaMan'
>>> avengers
['ironman', 'spidey', 'Mr.bean']
>>> 
>>> s=[]
>>> # s.append("Mr.bean")
>>> avengers[2]
'Mr.bean'
>>> # s.append(avengers[2])
>>> # s.append(avengers.pop())
>>> 
>>> avengers=['ironman','spidey','superman','Mr.bean','AquaMan']
>>> 
>>> avengers[3]
'Mr.bean'
>>> 
>>> avengers.pop(3)
'Mr.bean'
>>> avengers.pop(1)
'spidey'
>>> avengers
['ironman', 'superman', 'AquaMan']
>>> s=[1,2,3,[4,5,[6,7,[8,[9,[10],11],12],13],14],15]
>>> 
>>> # use Indexing to extract 3,5,7,9,10,11,14,15
>>> len(s)
5
>>> s[0]
1
>>> s[1]
2
>>> s[2]
3
>>> s[3]
[4, 5, [6, 7, [8, [9, [10], 11], 12], 13], 14]
>>> 