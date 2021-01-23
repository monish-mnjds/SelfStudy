a = [ 1,2,3,4,5,['a','b'],[1,'hello'],40],[90]


type(a)    #<class 'tuple'>

for item in a:
	if isinstance(item, list):
		for i in item:
			if isinstance(i, list):
				for ch in i:
					if ch == 'hello':
						print(ch)
            
            
#tracing 

item =  [1, 2, 3, 4, 5, ['a', 'b'], [1, 'hello'], 40]

i =  1
i =  2
i =  3
i =  4
i =  5
i =  ['a', 'b']

ch =  a
ch =  b

i =  [1, 'hello']
ch =  1
ch =  hello

hello                  #this is what we are expecting.......

i =  40

item =  [90]

i =  90

------------------------------------------------------------------------

a = [['A','B'],['a','b'],'-']
#output ['A-a', 'B-b']

capital, small, hyphen = a                #we are unpacking here......

#capital  #['A', 'B']
#small    #['a', 'b']
#hyphen   # '-'

l = []
for i in range(len(a)-1):
	res = ''.join(capital[i] + hyphen + small[i])    #''.join('A' + '-' + 'a')
	l.append(res)					 #''.join('B' + '-' + 'b')
	
print(l)                                  #['A-a', 'B-b']

---------------------------------------------------------------------------------------

d = {'a':'apple','b':10.3,'c':{'x':25.3,'y':30}, 'd':15}

for key, value in d.items():
    if isinstance(value, (int, float)):
        d[key] = value + 10
    if isinstance(value, dict):
        for k, v in value.items():
            if isinstance(v, (int, float)):
                d[key][k] = v + 10
	
--------------------------------------------------------------------------------------
l = ['add','subtracting']

_list = []
for item in l:
    if len(item) == 3:
        _list.append(item + 'ing')

    if len(item) > 3 and item.endswith('ing'):
        _list.append(item + 'ly')

print(_list)

#['adding', 'subtractingly']
-------------------------------------------------------------------------

l = ['apple.com', 'google.in', 'nic.in', 'testyantra.org']

_list = []

for item in l:
    company, ext = item.split('.')

    if ext == 'in':
        _list.append(item)

    elif ext != 'in':
        temp = company[::-1]
        dot = '.'
        _list.append(temp + dot + ext)

print(_list)

#['elppa.com', 'google.in', 'nic.in', 'artnaytset.org']
---------------------------------------------------------------------------------

string = 'python coding'

d = {}

for item in string:
    if item not in d:
        d[item] = 1

    elif item in d:
        d[item] += 1

print(d)		#{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'c': 1, 'd': 1, 'i': 1, 'g': 1}

----------------------------------------------------------------------------------------------------------------------

#prime using lambda

def prime(num):
    
    r = range(2, num)
    m = map(lambda item: num % item == 0 , r)    
    return m

res = prime(13)

if all(res) == False:
    print('prime')
else:
    print('Not a prime')

---------------------------------------------------------------------------------
