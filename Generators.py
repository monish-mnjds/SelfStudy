
def new(dict):
  
  for x, y in dict.items():
    yield x, y

a = {1:'hi', 2:'welcome'}

b = new(a)

print(b)         #returns generator object

next(b)         #(1, 'hi')
next(b)         #(2, 'welcome')

next(b)         #StopIteration

------------------------------------------

def ex():
  n = 3
  yield n 
  
  n = n * n 
  yield n
  
v = ex()

next(v)      # 3 
next(v)      # 9
next(v)      # StopIteration

------------------------------------------

def ex():
  n = 3
  yield n 
  
  n = n * n 
  yield n
  
v = ex()

#type - 1       for iterating

for x in v:       #looping through the generator object
  print(x)
  
#type -2 

for x in ex():    #directly calling the function in for loop
  print(x)

------------------------------------------------------------

#Generator Expression
---------------------

f = range(6)
print('list comp', end = ':' )

q = [ x + 2   for x in f ]
print(q)

print('gen exp', end = ':')
r = ( x+2   for x in f )         # this is generator expression and not tuple comprehension.....
print(r)

for x in r:
  print(x)
  
print(min(r))
print(max(r))

