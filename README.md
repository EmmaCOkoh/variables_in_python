Variable: It is a container where we can put our value
e.g 
 x=2 #here x is variable and 2 is value
 x+3
 5
y=3

Note:If I want to use output of previous operation so we use underscore (_) 
 _+y
8  # previous output 5 and y is 3 

Use String as a variable:
-- Strings in python are surrounded by either single quotation marks, or double quotation marks.
-- e.g  "shiva" ,'shiva'

Assign String to a Variable:
-- Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
name='shiva'
name
shiva

Slicing String:
we can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.

-- Get the characters from position 2 to position 5 (not included):
name='youtube'
name[2:5]
 'utu'

Slice From the Start:
name[:5] #from starting to index 5 (exclude)
 'youtu'

Slice To the End:
name[2:] #from 2nd index to end
 'utube'

Negative Indexing:

0    1   2   3    4   5   6   #positive indexing
y    o   u   t    u   b   e
-7  -6  -5  -4   -3  -2  -1   #Negative indexing 

name[-1]
'e'

 name[:-1]
 'youtub'
name[:]
 'youtube'
 name [:0]
''
name[-5:-2]
'utu' 

Concatenate String:
 name+ ' telusko'
 'youtube telusko'
