### Exercise :1

Write a generator named **frange** which takes arguments “start”, “end” and “step” and prints the floating point numbers.

**Solution**
```python
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

>>> for i in frange(0, 1, 0.1):
	print(round(i, 1))

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
>>> for i in frange(0, 1, 0.5):
	print(round(i, 1))
	
0
0.5
>>> 
>>> for i in frange(0, 1, 0.2):
	print(round(i, 1))

0
0.2
0.4
0.6
0.8
>>> 
```

**Using Iterator Protcol**

```python
class Frange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):       # Should return an object instance which has implemented __next__ method
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration          # StopIteration exception must be raised. Otherwise IndexError exception will be raised.
        item = self.start
        self.start = self.start + self.step
        return item

>>> f = Frange(1, 5, 1)
>>> next(f)
1
>>> next(f)
2
>>> next(f)
3
>>> next(f)
4
>>> next(f)
5
>>> next(f)
Traceback (most recent call last):
  File "<pyshell#404>", line 1, in <module>
    next(f)
  File "/Users/sandeep/Documents/Python_Practice/_descreptors.py", line 274, in __next__
    raise StopIteration
StopIteration
```

### Exercise :2

**Reverse Iterator using Iterator Protocol**

```python
class Reverse_Iterator:
    def __init__(self, iterable):
        self.index = len(iterable)-1
        self.iterable = iterable

    def __iter__(self):     # Should return an object instance which has implemented __next__ method
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration    # Must be raised as part of Iterator Protocol
        item = self.iterable[self.index]
        self.index = self.index - 1
        return item

>>> r = Reverse_Iterator([1, 2, 3, 4])
>>> next(r)
4
>>> next(r)
3
>>> next(r)
2
>>> next(r)
1
>>> next(r)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    next(r)
  File "/Users/sandeep/Documents/Training/_Iterators.py", line 278, in __next__
    raise StopIteration
StopIteration
>>> 
```

**Reverse Iterator using Generator Function**

```python
def reverse_iterator(iterable):
    index = len(iterable) - 1
    while index >= 0:
        yield iterable[index]
        index -= 1

>>> r = reverse_iterator([1, 2, 3])
>>> next(r)
3
>>> next(r)
2
>>> next(r)
1
>>> next(r)
Traceback (most recent call last):
  File "<pyshell#389>", line 1, in <module>
    next(r)
StopIteration
```

### Exercise :3

**Forward Iterator using Iterator Protocol**

```python
class Forward_Iterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):     # Should return an object instance which has implemented __next__ method
        return self

    def __next__(self):
        if self.index > len(self.iterable)-1:
            raise StopIteration      # Must be raised as part of Iterator Protocol
        item = self.iterable[self.index]
        self.index = self.index + 1
        return item

>>> f = Forward_Iterator([1, 2, 3, 4])
>>> next(f)
1
>>> next(f)
2
>>> next(f)
3
>>> next(f)
4
>>> next(f)
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    next(f)
  File "/Users/sandeep/Documents/Training/_Iterators.py", line 294, in __next__
    return next(self.iterable)
StopIteration
>>> 
```

**Forward Iterator using Generator Function**

```python
def forward_iterator(iterable):
    index = 0
    while index <= len(iterable)-1:
        yield iterable[index]
        index +=1

>>> f = forward_iterator([1, 2, 3])
>>> next(f)
1
>>> next(f)
2
>>> next(f)
3
>>> next(f)
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    next(f)
StopIteration
```

### Exercise :4

**Custom Object which can be iterated in reversed order**
(implement _ _reversed_ _ special method)
```python
class Spam:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)

    def __reversed__(self):
        return reversed(self.iterable)

>>> s = Spam([1, 2, 3, 4])
>>> for num in reversed(s):
	print(num)
	
4
3
2
1
>>> 
```
### Exercise :5

Write a custom iterator which takes a file object, splits the lines based on comma and returns each line.

**Using Iterator Protocol**
```python
class SplitLines:
    def __init__(self, file_object):
        self.lines = file_object.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.lines.__next__()
        return line.strip().split(',')

>>> f = open('lines.txt')   # Open the file
>>> l = SplitLines(f)    # Create an instance to SplitLines class
>>> next(l)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance']
>>> next(l)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance']
>>> next(l)
['Jerry', 'Male', '3/4/2005', '1:00 PM', '138705', '9.34', 'true', 'Finance']
>>> next(l)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance']
>>> next(l)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance']
>>> next(l)
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    next(l)
  File "/Users/sandeep/Documents/Python_Practice/Hello.py", line 74, in __next__
    line = next(self.lines)
StopIteration
>>> 
```

**Using Generator Function**

```python
def splitlines(f_object):
    for line in f_object:
        yield line.split(',')

>>> f = open('lines.txt')   # Open the file
>>> g = splitlines(f)
>>> g       
>>> <generator object splitlines at 0x7fa27e7b0c80>     # g is a Generator Object
>>> next(g)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance\n']
>>> next(g)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance\n']
>>> next(g)
['Jerry', 'Male', '3/4/2005', '1:00 PM', '138705', '9.34', 'true', 'Finance\n']
>>> next(g)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance\n']
>>> next(g)
['Maria', 'Female', '4/23/1993', '11:17 AM', '130590', '11.858', 'false', 'Finance\n']
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    next(g)
StopIteration
>>> 
```
### Exercise :6

Write a custom iterator which counts the occurrence of a specific word in a file.

**Using iterator protocol**

```python
class CountWord:
    def __init__(self, f_obj, key):
        self.f_obj = f_obj.__iter__()
        self.key = key     # word to be counted in each line
        self.line_no = 0    # To keep track of line number

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.f_obj)
        msg = f'Line No:{self.line_no} Count: {line.count(self.key)}'
        self.line_no += 1
        return msg

>>> c = CountWord(f, 'world')
>>> c
<__main__.CountWord object at 0x7fd16fdd14f0>
>>> next(c)
'Line No:0 Count: 2'
>>> next(c)
'Line No:1 Count: 0'
>>> next(c)
'Line No:2 Count: 1'
>>> next(c)
'Line No:3 Count: 1'
>>> next(c)
Traceback (most recent call last):
  File "<pyshell#373>", line 1, in <module>
    next(c)
  File "/Users/sandeep/Documents/Training/_Iterators.py", line 442, in __next__
    line = next(self.f_obj)
StopIteration
>>>  
```

**Using Generator function**

```python
def countword(f_obj, key):
    for no, line in enumerate(f_obj):
        if key in line:
            yield f'Line No: {no} Count: {line.count(key)}'

>>> c = countword(f, 'world')
>>> c
<generator object countword at 0x7ff74d7b3dd0>
>>> next(c)
'Line No: 0 Count: 2'
>>> next(c)
'Line No: 2 Count: 1'
>>> next(c)
'Line No: 3 Count: 1'
>>> next(c)
Traceback (most recent call last):
  File "<pyshell#366>", line 1, in <module>
    next(c)
StopIteration
>>> 
```

### Exercise :7

Write a custom iterator to print the line number if the word to be searched is found.

**Using Iterator protocol**
```python
class _find:
    def __init__(self, f_obj, key):
        self.f_obj = f_obj 
        self.key = key      # word to be searched
        self.line_no = 0    # To Keep track of Current line number

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.f_obj)
        current_line_no = self.line_no        # Save the current line number in a variable 'current_line_no'
        if self.key in line:
            self.line_no +=1
            return current_line_no
        else:
            self.line_no +=1

>>> g = _find(f, 'world')
>>> g
<__main__._find object at 0x7ffcf5bdb4f0>
>>> next(g)
0
>>> next(g)
>>> next(g)
2
>>> next(g)
3
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#453>", line 1, in <module>
    next(g)
  File "/Users/sandeep/Documents/Training/_Iterators.py", line 391, in __next__
    line = next(self.f_obj)
StopIteration
>>> 
```

**Using Generator function**

```python
def _find(f_obj, key):
    for no, line in enumerate(f_obj):
        if key in line:
            yield no

>>> g = _find(f, 'world')
>>> g
<generator object _find at 0x7fa3bfa64200>
>>> next(g)
0
>>> next(g)
2
>>> next(g)
3
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#459>", line 1, in <module>
    next(g)
StopIteration
>>> 
```

### Exercise :8

Write a custom iterator to print valid python lines in a file. i.e. ignore the lines starting from "#" (ignore lines with comments)

**Using Iterator protocol**
```python
class ValidPyLines:
    def __init__(self, lines):
        self.lines = lines

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.lines)
        line = line.strip()
        if line and not line.startswith('#'):
            return line
>>> valid = ValidPyLines(f)
>>> valid
<__main__.ValidPyLines object at 0x7fc2a56024f0>
>>> next(valid)
>>> next(valid)
>>> next(valid)
'def is_anagram(str1, str2):'
>>> next(valid)
'if str1.upper() == str2.upper():    # Return False if both words are same'
>>> next(valid)
'return False'
>>> next(valid)
's_str1 = sorted(str1.upper())   # Convert to upper case and sort'
>>> 
```

**Using Generator function**

```python
def VaildPyLines(lines):
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#'):
            continue
        yield line

>>> g = VaildPyLines(f)
>>> next(g)
'def is_anagram(str1, str2):'
>>> next(g)
'if str1.upper() == str2.upper():    # Return False if both words are same'
>>> next(g)
'return False'
>>> next(g)
's_str1 = sorted(str1.upper())   # Convert to upper case and sort'
>>> 
```

### Exercise :9

Feeding output of one generator function to another (Setting up pipelines)

```python
"get_lines" is a generator function that yield a line.
def get_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            if line:
                yield line

"grep" is a generator function that accepts a pattern and a generator
def grep(pattern, g_lines):
    for line in g_lines:
        if pattern in line:
            yield line

"_split" is a generator function that splits the line based on comma.
def _split(g_lines):
    for line in g_lines:
        yield line.split(',')

below is the contents of sample.txt

"""
Hello world java there Hello world
Hello java Hello India Hello universe
Hello python Hello there Hello world
Hello python Hello India Hello world
"""

f = follow('sample.txt')
g = grep('python', f) # Generator "f" is being fed to another generator "grep"
s = _split(g)    # Generator "g" is fed to another generator "_split"

>>> for line in s:
	print(line)

['Hello', 'python', 'Hello', 'there', 'Hello', 'world\n']
['Hello', 'python', 'Hello', 'India', 'Hello', 'world']
>>> 
```