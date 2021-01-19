import webbrowser

class Web:
    __url = 'https://www.github.com/monish-mnjds/'          #private access modifiers  

    def __init__(self):                                     #it can be used within the base class & not in the derived class.
        webbrowser.open(self.__url)

w = Web()
print(w._Web__url)  # we can access it but it is not recommended.

------------------------------------------------------------------------------

class Web:
    _url = 'https://www.github.com/monish-mnjds/'           #protected access modifiers


class Git(Web):                                             #it can be used within the base class as well as derived class.
    def __init__(self):
        webbrowser.open(self._url)

g = Git()
print(g._url)   # we can access it but it is not recommended.


dir(g)
dir(w)  #using this we can find the attributes which can be applied.

------------------------------------------------------------------------------------------------------------------------------

#If we declare any variable or method as private, then they can be accessed only within the class in which they are defined.
#In Python, private members are preceded by two underscores.

#'length' and 'breadth' are the two private variables declared and can be accessed within the class 'Rectangle'.

class Rectangle:
    __length = 0 #private variable
    __breadth = 0 #private variable
    def __init__(self): #constructor
        self.__length = 5
        self.__breadth = 3    #printing values of the private variable within the class
        print(self.__length)
        print(self.__breadth)

rec = Rectangle() #object created for the class 'Rectangle'

#printing values of the private variable outside the class using the object created for the class 'Rectangle'
print(rec.length)
print(rec.breadth)

#Since we have accessed private variables outside the class 'Rectangle', we got an error. 
#Hence in the above program, Encapsulation is achieved using the private variables 'length' and 'breadth'.

--------------------------------------------------------------------------------------------------------------------------

class Shape:#protected variables
    _length = 10 
    _breadth = 20

class Circle(Shape):
    def __init__(self):#printing protected variables in the derived class
        print(self._length)
        print(self._breadth)

cr = Circle()

#printing protected variables outside the class 'Shape' in which they are defined
print(cr.length)
print(cr.breadth)

#When we try to access protected variables in the derived class, we got output. 
#But, in the main() method, we got an error.
#Hence in the above example, Encapsulation is achieved using the protected variables 'length' and 'breadth'.
