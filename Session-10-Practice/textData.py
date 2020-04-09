Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """name,genus,vore,order,conservation,sleep_total,sleep_rem,sleep_cycle,awake,brainwt,bodywt
Cheetah,Acinonyx,carni,Carnivora,lc,12.1,NA,NA,11.9,NA,50"""
'name,genus,vore,order,conservation,sleep_total,sleep_rem,sleep_cycle,awake,brainwt,bodywt\nCheetah,Acinonyx,carni,Carnivora,lc,12.1,NA,NA,11.9,NA,50'
>>> rows="""name,genus,vore,order,conservation,sleep_total,sleep_rem,sleep_cycle,awake,brainwt,bodywt
Cheetah,Acinonyx,carni,Carnivora,lc,12.1,NA,NA,11.9,NA,50"""
>>> 
>>> 
>>> rows.split('\n')
['name,genus,vore,order,conservation,sleep_total,sleep_rem,sleep_cycle,awake,brainwt,bodywt', 'Cheetah,Acinonyx,carni,Carnivora,lc,12.1,NA,NA,11.9,NA,50']
>>> rows.split('\n')[0]
'name,genus,vore,order,conservation,sleep_total,sleep_rem,sleep_cycle,awake,brainwt,bodywt'
>>> rows.split('\n')[1]
'Cheetah,Acinonyx,carni,Carnivora,lc,12.1,NA,NA,11.9,NA,50'
>>> 
>>> 
>>> rows.split('\n')[0].split(',')
['name', 'genus', 'vore', 'order', 'conservation', 'sleep_total', 'sleep_rem', 'sleep_cycle', 'awake', 'brainwt', 'bodywt']
>>> 
>>> rows.split('\n')[0].split(',').index('name')
0
>>> rows.split('\n')[0].split(',').index('sleep_total')
5
>>> rows.split('\n')[0].split(',')[0]
'name'
>>> rows.split('\n')[0].split(',')[5]
'sleep_total'
>>> rows.split('\n')[1].split(',')[0]
'Cheetah'
>>> rows.split('\n')[1].split(',')[5]
'12.1'
>>> 
>>> 
>>> 
>>> print(rows.split('\n')[0].split(',')[0],"\t",
      rows.split('\n')[0].split(',')[5], "\n",
      rows.split('\n')[1].split(',')[0],"\t",
      rows.split('\n')[1].split(',')[5])
name 	 sleep_total 
 Cheetah 	 12.1
>>> 
>>> 
>>> print("a\tb")
a	b
>>> print("""
%s \t %s"""%(rows.split('\n')[1].split(',')[0],rows.split('\n')[1].split(',')[5]))

Cheetah 	 12.1
>>> 
>>> 
>>> 
>>> # looping
>>> # is it line ? is it a word ?
>>> # loop variable
>>> # extra credit -> convert the string(sleep_time) -> float
>>> 