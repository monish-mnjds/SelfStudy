
#functions that take other functions as arguments are also called higher order functions.

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

operate(inc,3)
operate(dec,3)
----------------------------------

#Furthermore, a function can return another function.

def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()

--------------------------------------------------------
#decorator without @

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
    
pretty = make_pretty(ordinary)

pretty()

# using @

@make_pretty
def ordinary():
    print("I am ordinary")
    
# is equivalent to 
def ordinary():
    print("I am ordinary")

mydeco = make_pretty(ordinary)

----------------------------------------------------------

#decorator with parameters

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)
    
divide(2,0)   #I am going to divide 2 and 0    # Whoops! cannot divide

--------------------------------------------------------------------------

# decorator which works for all

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        print("Currently, calling ---> ",func.__name__)
        return func(*args, **kwargs)
    return inner
  
@works_for_all
def add(a,b):
    return a+b

add(10, 20)

--------------------------------------------------------------------------
