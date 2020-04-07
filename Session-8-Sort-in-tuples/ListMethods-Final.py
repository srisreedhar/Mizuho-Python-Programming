Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> avengers=['spidey','aquaman','wonderwoman','ironMan','birdman']
>>> # value exists in a list/collection
>>> # Membership checking operator
>>> 
>>> #  in -> membership
>>> # value in collection
>>> 
>>> 'spidey' in avengers
True
>>> 'aquaman' in avengers
True
>>> 'Aquaman' in avengers
False
>>> # 'p' in 'python
>>> # 1 in '1990'
>>> # 1 in 1990
>>> 
>>> # findout the index of a value in a list
>>> avengers.index('ironMan')
3
>>> # ListName.index(Value) -> integer
>>> avengers.append("ironman")
>>> avengers
['spidey', 'aquaman', 'wonderwoman', 'ironMan', 'birdman', 'ironman']
>>> 
>>> 
>>> numbers=[9,1,8,2,7,3,7,4,6,0,5]
>>> numbers
[9, 1, 8, 2, 7, 3, 7, 4, 6, 0, 5]
>>> # sorting
>>> # ascen / descen
>>> 
>>> # ListName.sort()
>>> 
>>> numbers.sort()
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
>>> 
>>> numbers=[9,1,8,2,7,3,7,4,6,0,5]
>>> numbers
[9, 1, 8, 2, 7, 3, 7, 4, 6, 0, 5]
>>> 
>>> # sorting in descending order
>>> # ListName.sort(reverse=True)
>>> 
>>> numbers.sort(reverse=True)
>>> numbers
[9, 8, 7, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> 
>>> numbers.sort(reverse=False)
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
>>> 
>>> numbers.sort()
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
>>> 
>>> 
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
>>> numbers=[9,1,8,2,7,3,7,4,6,0,5]
>>> 
>>> 
>>> numbers
[9, 1, 8, 2, 7, 3, 7, 4, 6, 0, 5]
>>> 
>>> # builtin function
>>> # sorted()
>>> 
>>> sorted(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
>>> numbers
[9, 1, 8, 2, 7, 3, 7, 4, 6, 0, 5]
>>> 
>>> 
>>> avengers
['spidey', 'aquaman', 'wonderwoman', 'ironMan', 'birdman', 'ironman']
>>> # batman
>>> 
>>> # inserting values at a defined index
>>> # ListName.insert(Value,Index)
>>> 
>>> # ListName.insert(Index,value) -> .insert(where,what)
>>> 
>>> avengers.insert(0,'batman')
>>> avengers
['batman', 'spidey', 'aquaman', 'wonderwoman', 'ironMan', 'birdman', 'ironman']
>>> 
>>> # ListName.append(Value)
>>> # ListName.insert(Index,value)
>>> # ListName.remove(Value)
>>> # Listname.pop(index)
>>> 
>>> "Nikola Tesla ".split()
['Nikola', 'Tesla']
>>> 
>>> # joining
>>> 
>>> # collection , delimitter
>>> # add all the values to the delimitter
>>> 
>>> # "Delimitter".join(Collection)
>>> 
>>> "".join(['Nikola', 'Tesla'])
'NikolaTesla'
>>> " ".join(['Nikola', 'Tesla'])
'Nikola Tesla'
>>> 
>>> "\n".join(avengers)
'batman\nspidey\naquaman\nwonderwoman\nironMan\nbirdman\nironman'
>>> print("\n".join(avengers))
batman
spidey
aquaman
wonderwoman
ironMan
birdman
ironman
>>> 
>>> 
>>> # Tuple
>>> 
>>> t=()
>>> type(t)
<class 'tuple'>
>>> sample=(1,2,3,4,)
>>> sample
(1, 2, 3, 4)
>>> # dir(sample)
>>> 
>>> len(sample)
4
>>> 
>>> 
>>> t
()
>>> 
>>> 1,2,3,4,5,6,7
(1, 2, 3, 4, 5, 6, 7)
>>> 
>>> 
>>> # list+tuple
>>> # tuple + tuple
>>> 
>>> # in
>>> 
>>> 
>>> 
>>> 
>>> # Indexing in Lists
>>> 
>>> 
>>> 