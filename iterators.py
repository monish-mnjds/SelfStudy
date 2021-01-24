my_list = [4, 7, 0, 3]
# define a list 

my_iter = iter(my_list)
# get an iterator using iter()

# iterate through it using next()

print(next(my_iter))
# Output: 4

print(next(my_iter))
# Output: 7

# next(my_iter) is same as my_iter.__next__()

print(my_iter.__next__())
# Output: 0

print(my_iter.__next__())
# Output: 3

next(my_iter)
# This will raise error, no items left
---------------------------------------------

#elegant way of iterating

for element in my_list:
  print(element)
  
---------------------------------------------

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# We can also use a for loop to iterate over our iterator class.

for i in PowTwo(5):
  print(i)

-----------------------------------------------------

#infinite iterator

class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
           
a = iter(InfIter())
next(a)
next(a)
next(a)        #this will keep on returning odd numbers.....

---------------------------------------------------------------------
#Custom Iterator
class MyItr:
    """Iterator for looping over a sequence."""
    def __init__(self, iterable):
        self.data = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


num = MyItr([1, 2, 3, 4, 5])
_list = MyItr(['apple', 'google', 'yahoo', 'facebook'])
string = MyItr('spam')

for n in num:
    print(n)

for l in _list:
    print(l)

for s in string:
    print(s)
-----------------------------------------------------------------------------
