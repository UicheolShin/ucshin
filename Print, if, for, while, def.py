Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=3
>>> if a>1:
	print("a is greater than 1")

	
a is greater than 1
>>> for a in[1,2,3]:
	print(a)

	
1
2
3
>>> i=0
>>> while i<3:
	i=i+1
	print(i)

	
1
2
3
>>> def add(a,b):
	return a+b
>>> add(3,4)
SyntaxError: invalid syntax
>>> add(3,4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    add(3,4)
NameError: name 'add' is not defined
>>> 
================================ RESTART: Shell ================================
>>> def add(a,b):
	return a+b

>>> add(3,4)
7
>>> 