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
