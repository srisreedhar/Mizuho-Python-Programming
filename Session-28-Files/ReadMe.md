### Files
###### WorkFlow
```
1) Locate the file
2) Open the file
		- read mode
		- write mode
 --- processes ---
 	2.1) Read the file
 	    apply 
           .read() method on the fileObj to read all at once
           .readline() to read the file line by line
           .readlines() to read the file into a list of strings


3) close the file

Fileobj.close()

  3.1) verify if the file is closed
      Fileobj.closed


2) Opening a file


open() -> To open all the files

2 args

	1) FilePath/FileName with extension
	2) access mode

open('FIleName.ext',AcessMode)	


Access Modes
	r - Read mode
	w - write mode
	a - append mode

open('data.txt','r')	


fileObj=open('data.txt','r')


FileName -> data.txt ( just filename if in the same foder)
			'c://someFolderName/data.txt' ( if in other folder )

```

### creating a File / writing to a file

```
open('FileYouWanttoCreate.txt','w')

```


### Write to a file

```
	- open the file in write mode
	- have the content ready which needs to be written
	- use .write()	 method to write to a file

	.write("content_to_be_written")
```
