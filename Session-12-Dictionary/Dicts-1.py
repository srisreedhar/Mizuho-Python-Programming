Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> languages={
	"usa":"English",
	"China":"Chineese",
	"Japan":"Japaneese",
	}
>>> languages
{'usa': 'English', 'China': 'Chineese', 'Japan': 'Japaneese'}
>>> # Adding values to a dictionary
>>> # india - Hindi
>>> #dictName['NewKey']=NewValue
>>> 
>>> languages['india']='hindi'
>>> languages
{'usa': 'English', 'China': 'Chineese', 'Japan': 'Japaneese', 'india': 'hindi'}
>>> 
>>> language['china']='chineese'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    language['china']='chineese'
NameError: name 'language' is not defined
>>> languages['china']='chineese'
>>> languages
{'usa': 'English', 'China': 'Chineese', 'Japan': 'Japaneese', 'india': 'hindi', 'china': 'chineese'}
>>> 
>>> 
>>> 
>>> marks={
	"student1"=[20,30,50],
	
SyntaxError: invalid syntax
>>> marks={
	"student1":[20,30,50],
	"student2":[50,10,20],
	"student3":[90,10,20]
	}
>>> 
>>> marks
{'student1': [20, 30, 50], 'student2': [50, 10, 20], 'student3': [90, 10, 20]}
>>> 
>>> marks['student4']=[1,1,1]
>>> marks
{'student1': [20, 30, 50], 'student2': [50, 10, 20], 'student3': [90, 10, 20], 'student4': [1, 1, 1]}
>>> 
>>> 
>>> 
>>> marks['student1']
[20, 30, 50]
>>> type(marks['student1'])
<class 'list'>
>>> 
>>> 
>>> type(languages['usa'])
<class 'str'>
>>> 
>>> 
>>> marks['student1'].append(111)
>>> marks
{'student1': [20, 30, 50, 111], 'student2': [50, 10, 20], 'student3': [90, 10, 20], 'student4': [1, 1, 1]}
>>> marks['student2'].append(111)
>>> marks['student3'].append(111)
>>> marks['student4'].append(111)
>>> marks['student5'].append(111)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    marks['student5'].append(111)
KeyError: 'student5'
>>> 
>>> 
>>> marks.get('student1')
[20, 30, 50, 111]
>>> marks['student1']
[20, 30, 50, 111]
>>> marks['student5']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    marks['student5']
KeyError: 'student5'
>>> marks.get('student5')
>>> marks.get('student5',"Check the key Name, it doesnt exist")
'Check the key Name, it doesnt exist'
>>> marks.get('student2',"Check the key Name, it doesnt exist")
[50, 10, 20, 111]
>>> 
>>> marks.keys()
dict_keys(['student1', 'student2', 'student3', 'student4'])
>>> 
>>> marks.values()
dict_values([[20, 30, 50, 111], [50, 10, 20, 111], [90, 10, 20, 111], [1, 1, 1, 111]])
>>> type(marks.keys())
<class 'dict_keys'>
>>> 
>>> 
>>> 
>>> list,list()
(<class 'list'>, [])
>>> 
>>> list(marks.keys())
['student1', 'student2', 'student3', 'student4']
>>> list(marks.keys())[0]
'student1'
>>> marks[list(marks.keys())[0]]
[20, 30, 50, 111]
>>> 