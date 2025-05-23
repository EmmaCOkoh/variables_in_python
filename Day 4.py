Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
2 + 3
5
x = 2
x + 3
5
y = 3
x + y
5
x = 9
x + y
12
x
9
abc
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
x + 10
19
abc = 17
abc
17
x + abc
26
x + 10
19
_ + y
22
name = "Youtube"
name
'Youtube'
name + "rocks"
'Youtuberocks'
name + 'rocks'
'Youtuberocks'
>>> name +, "rocks"
SyntaxError: invalid syntax
>>> name + "rocks"
'Youtuberocks'
>>> name "rocks"
SyntaxError: invalid syntax
>>> name[0]
'Y'
>>> name[1]
'o'
>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> name[0,4]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[0,4]
TypeError: string indices must be integers, not 'tuple'
>>> name[0:4]
'Yout'
>>> name[1:]
'outube'
>>> name[:5]
'Youtu'
>>> name[3:10]
'tube'
>>> name[0:3] = "my"
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    name[0:3] = "my"
TypeError: 'str' object does not support item assignment
>>> "my" + name[3:]
'mytube'
myname = "Emmanuel"
len(myname)
8
