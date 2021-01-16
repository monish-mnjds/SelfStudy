#Function Polymorphism in Python

# Python program to demonstrate in-built poly-morphic functions 

# len() being used for a string 
print(len("geeks")) 

# len() being used for a list 
print(len([10, 20, 30])) 

-------------------------------------------------------------------------------------
# with class methods

''' We create a for loop that iterates through a tuple of objects. 
Then call the methods without being concerned about which class type each object is.
We assume that these methods actually exist in each class.'''

class India(): 
	def capital(self): 
		print("New Delhi is the capital of India.") 

	def language(self): 
		print("Hindi is the most widely spoken language of India.") 

	def status(self): 
		print("India is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def status(self): 
		print("USA is a developed country.") 

ind = India() 
usa = USA() 

for country in (ind, usa): 
	country.capital() 
	country.language() 
	country.status() 

	 #or
		
def func(obj): 
       obj.capital() 
       obj.language()
       obj.status()
         
func(ind) 
func(usa)
-----------------------------------------------------------------------------------------

#method overriding
-------------------

class Bird: 
    def intro(self): 
	    print("There are many types of birds.") 
	
    def flight(self): 
	    print("Most of the birds can fly but some cannot.") 
	
class parrot(Bird): 
    def flight(self): 
	    print("parrot can fly.") 
	
class penguin(Bird): 
    def flight(self): 
	    print("penguin cannot fly.") 
	
bird = Bird() 
par = parrot() 
pen = penguin() 

bird.intro() 
bird.flight() 

par.intro() 
par.flight() 

pen.intro() 
pen.flight() 

---------------------------------------------------------------------------------------------

#Example 1: Polymorphism in addition operator

num1 = 1
num2 = 2
print(num1+num2)

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

#Here, we can see that a single operator + has been used to carry out different operations for distinct data types.
#This is one of the most simple occurrences of polymorphism in Python.
