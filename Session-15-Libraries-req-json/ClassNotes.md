# Libraries / Modules / packages 

Libraries - a program / collection of multiple functions ( packed together under one name space)

A sample Library, mathematics would have multiple math related functions

Mathematicspy
- addition()
- sin()
- cosine()
- subtration ()
- sqrt()

# importing functions / classes  from a library

##### First install the package
using below, install a library / package / module 	

	pip install moduleName 
	
##### Calling the library into our workspace
 syntax :

	import <ModuleName> 

##### call a functionality from an imported library
 syntax :
 
		ModuleName.functionality()

##### This is how we need to import
:
```
1#) import -> keyword
	import moduleName
	Usage :
		moduleName.methodName(inputs)


2# ) selective imports

	from ModuleName import MethodName
	from ModuleName import MethodName,MethodName,MethodName,MethodName

3#) Nick Names to the imports / aliasing

	import math as nope
	from ModuleName import MethodName as nopenope

```

### libraries , we'll use in our class


> requests -> how to connect to internet
> os -> how to interact with the OS/System
> json -> to deal with json data



#### requests -> browser


1) enter the web address
2) send request
3) catch the response

4) perform/use response

```
1) enter the web address
	-> define a variable
2) send request
	-> requests.get(URL/URLVariable)
3) catch the response
	-> assign a var to the resp
	-> respObj = requests.get(URL/URLVariable)

4) perform/use response
	deal with respObj
```

#### JSON ->  Data Format

```
- create a json object
	- convert a python Obj into a JSON data
		- json.dumps(pythonObj)

- create a python object
	- convert a json data into Python Object
		-json.loads(jsonObj)
```




