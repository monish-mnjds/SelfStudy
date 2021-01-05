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

