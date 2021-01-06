class employee():
    def __init__(self,name,age,id,salary):   #creating a function
        self.name = name                     #self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id
 
emp1 = employee("harshit",22,1000,1234) #creating objects
emp2 = employee("arjun",23,2000,2234)
print(emp1.__dict__)                    #Prints dictionary


'''
    ’emp1′ and ’emp2′ are the objects that are instantiated against the class ’employee’.

    Here, the word (__dict__) is a “dictionary” which prints all the values of object ‘emp1’ 
against the given parameter (name, age, salary).  
    
    (__init__) acts like a constructor that is invoked whenever an object is created.'''
