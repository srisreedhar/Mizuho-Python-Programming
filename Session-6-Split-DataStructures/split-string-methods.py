Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="Nikola tesla"
>>> name
'Nikola tesla'
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'name']
>>> 
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> name.title()
'Nikola Tesla'
>>> 
>>> dir(111)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> # dunder methods
>>> 
>>> 
>>> name
'Nikola tesla'
>>> name2=" Srinivasa ramanujan "
>>> name2
' Srinivasa ramanujan '
>>> 
>>> name.split()
['Nikola', 'tesla']
>>> 
>>> name2.lstrip()
'Srinivasa ramanujan '
>>> name2.rstrip()
' Srinivasa ramanujan'
>>> name2.strip()
'Srinivasa ramanujan'
>>> 
>>> row="2015-02-18,29136.07,29411.32,29126.91,29320.26,11000,29320.26"
>>> 
>>> row
'2015-02-18,29136.07,29411.32,29126.91,29320.26,11000,29320.26'
>>> 
>>> # .split(delimitter/seperator)
>>> # by default - space as delimitter
>>> 
>>> row.split(",")
['2015-02-18', '29136.07', '29411.32', '29126.91', '29320.26', '11000', '29320.26']
>>> 
>>> row.split(",")[0]
'2015-02-18'
>>> 
>>> name
'Nikola tesla'
>>> 
>>> name.split()
['Nikola', 'tesla']
>>> name.split()[0]
'Nikola'
>>> name.split()[1]
'tesla'
>>> name.split()[1]
'tesla'
>>> 
>>> type(str(78.005))
<class 'str'>
>>> 
>>> name.split()[1].upper()
'TESLA'
>>> 
>>> 
KeyboardInterrupt
>>> """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
>>> 
>>> 
>>> """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
>>> 
>>> 
>>> 
>>> 
>>> para="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
 Ipsum has been the industry's standard dummy text ever since the 1500s, when an
 unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic
  typesetting, remaining essentially unchanged. It was popularised in the 1960s 
  with the release of Letraset sheets containing Lorem Ipsum passages, and more 
  recently with desktop publishing software like Aldus PageMaker including 
  versions of Lorem Ipsum."""
>>> 
>>> para
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem\n Ipsum has been the industry's standard dummy text ever since the 1500s, when an\n unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic\n  typesetting, remaining essentially unchanged. It was popularised in the 1960s \n  with the release of Letraset sheets containing Lorem Ipsum passages, and more \n  recently with desktop publishing software like Aldus PageMaker including \n  versions of Lorem Ipsum."
>>> 
>>> 
>>> para.split("\n")
['Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem', " Ipsum has been the industry's standard dummy text ever since the 1500s, when an", ' unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic', '  typesetting, remaining essentially unchanged. It was popularised in the 1960s ', '  with the release of Letraset sheets containing Lorem Ipsum passages, and more ', '  recently with desktop publishing software like Aldus PageMaker including ', '  versions of Lorem Ipsum.']
>>> para.split("\n")[1]
" Ipsum has been the industry's standard dummy text ever since the 1500s, when an"
>>> 
>>> para.split("\n")[1].split()
['Ipsum', 'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s,', 'when', 'an']
>>> 
>>> para.split("\n")[1].split(11)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    para.split("\n")[1].split(11)
TypeError: must be str or None, not int
>>> para.split("\n")[1].split()
['Ipsum', 'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s,', 'when', 'an']
>>> para.split("\n")[1].split()[11]
'1500s,'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 1,2,3,4,5,6,7
(1, 2, 3, 4, 5, 6, 7)
>>> 
>>> 
>>> 