Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits=[]
>>> fruits
[]
>>> fruits=['banana','cherry','melon','pappaya']
>>> fruits
['banana', 'cherry', 'melon', 'pappaya']
>>> 
>>> len(fruits)
4
>>> fruits[0]
'banana'
>>> fruits[1]
'cherry'
>>> fruits[2]
'melon'
>>> fruits[3]
'pappaya'
>>> fruits[4]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fruits[4]
IndexError: list index out of range
>>> 
>>> numbers=['one','two',3,4,5]
>>> 
>>> 
>>> veg=["ocra",'eggplant','snakeguard']
>>> 
>>> fruits
['banana', 'cherry', 'melon', 'pappaya']
>>> 
>>> 
>>> fruits[0]
'banana'
>>> fruits[0].upper()
'BANANA'
>>> 
>>> fruits.upper()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fruits.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> 
>>> 
>>> fruits
['banana', 'cherry', 'melon', 'pappaya']
>>> # adding a new value to a list
>>> # listName.append(Value)
>>> 
>>> fruits.append('melon')
>>> fruits
['banana', 'cherry', 'melon', 'pappaya', 'melon']
>>> fruits.append("grape")
>>> fruits
['banana', 'cherry', 'melon', 'pappaya', 'melon', 'grape']
>>> 
>>> veg
['ocra', 'eggplant', 'snakeguard']
>>> 
>>> fruits.append(veg)
>>> fruits
['banana', 'cherry', 'melon', 'pappaya', 'melon', 'grape', ['ocra', 'eggplant', 'snakeguard']]
>>> 
>>> len(fruits)
7
>>> fruits[5]
'grape'
>>> fruits[6]
['ocra', 'eggplant', 'snakeguard']
>>> 
>>> 
>>> fruits.extend(veg)
>>> fruits
['banana', 'cherry', 'melon', 'pappaya', 'melon', 'grape', ['ocra', 'eggplant', 'snakeguard'], 'ocra', 'eggplant', 'snakeguard']
>>> 
>>> # fruits.remove(veg)
>>> # fruits.remove([1,2,3,4,5])
>>> fruits.remove(veg)
>>> fruits
['banana', 'cherry', 'melon', 'pappaya', 'melon', 'grape', 'ocra', 'eggplant', 'snakeguard']
>>> # fruits.remove('melon')
>>> 
>>> 
====== RESTART: C:/Users/User/Desktop/Mizuho/Programs/Session-7-/interview_list.py ======
Enter your Namesri
Enter your Year of birth2010
Enter your DegreemBA

Hi,
Your name is sri,
You're 10 years old and you've studied mBA
the list is  ['sri', 2010, 'mBA']
>>> 
====== RESTART: C:/Users/User/Desktop/Mizuho/Programs/Session-7-/interview_list.py ======
Enter your Name sree
Enter your Year of birth 2009
Enter your Degree mca

Hi,
Your name is sree,
You're 11 years old and you've studied mca
the list is  ['2009', 'sree', 'mca']
>>> 
====== RESTART: C:/Users/User/Desktop/Mizuho/Programs/Session-7-/interview_list.py ======
Enter your Name spidey
Enter your Year of birth 1891
Enter your Degree ba

Hi,
Your name is spidey,
You're 129 years old and you've studied ba
the list is  ['1891', 'spidey', 1891, 'ba']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> details
['1891', 'spidey', 1891, 'ba']
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'curent_year', 'details', 'dob', 'edu', 'name', 'yr']
>>> 