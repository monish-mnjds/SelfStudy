#simple inheritance
-------------------

import webbrowser           #if the derived class has only one parent and parent has only one child then it is simple inheritance

class Web:
    def fb(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1(Web):
    def ig(self):
        webbrowser.open("https://www.instagram.com/")
        
w = Web1()    

w.ig()      #method of the derived class can be accessed by creating an object instance for the derived class
w.fb()      #method of the base class can be accessed using inheritance

--------------------------------------------------------------------------------------------------------------

#method overriding
------------------

import webbrowser
class Web:
    def openbrowser(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1(Web):
    def openbrowser(self):
        webbrowser.open("https://www.instagram.com/")
        
    def git(self):
        webbrowser.open("https://www.github.com/")
        
w = Web1()
w.openbrowser()     #method inherited from parent class can be overrided by derived class if needed

-------------------------------------------------------------------------------------------------------

#usage of super()
-----------------

import webbrowser
class Web:
    def openbrowser(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1(Web):
    def openbrowser(self):
        super().openbrowser()                             #we can access the parent class method by using the super() in the child class,
        webbrowser.open("https://www.instagram.com/")     #even if we override the parent class method
        
w = Web1()
w.openbrowser()    
----------------------------------------------------------------------------------------------------------------------------------------------

#multilevel inheritance
------------------------

import webbrowser
class Web:
    def fb(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1(Web):
    def ig(self):
        webbrowser.open("https://www.instagram.com/")

class Web2(Web1):
    def git(self):
        webbrowser.open("https://www.github.com/")

w = Web2()
w.fb()
w.ig()
w.git()             #parent of the web2 is the derived class(web1) of the web class
--------------------------------------------------------------------------------------

#multiple inheritance
---------------------

import webbrowser
class Web:
    def fb(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1:
    def ig(self):
        webbrowser.open("https://www.instagram.com/")

class Web2(Web, Web1):
    def git(self):
        webbrowser.open("https://www.github.com/")

w = Web2()
w.fb()
w.ig()
w.git()         #web2 child class can access the method from the parent class web and web1
---------------------------------------------------------------------------------------------

#hierarchical inheritance
-------------------------

import webbrowser
class Web:
    def fb(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1(Web):
    def ig(self):
        webbrowser.open("https://www.instagram.com/")

class Web2(Web):
    def git(self):
        webbrowser.open("https://www.github.com/")

w = Web1()
x = Web2()
w.fb()
x.fb()          #Both the child classes web1 and web2 can access the method of the parent class

----------------------------------------------------------------------------------------------------

#hybrid inheritance
-------------------

import webbrowser
class Web:
    def fb(self):
        webbrowser.open("https://www.facebook.com/")
       
class Web1(Web):
    def ig(self):
        webbrowser.open("https://www.instagram.com/")

class Web2(Web):
    def git(self):
        webbrowser.open("https://www.github.com/")

class Web3(Web1, Web2):
    def yt(self):
        webbrowser.open("https://www.youtube.com/")

w = Web3()

Web3.__mro__
Web3.mro()

---------------------------------------------------------------------------------------------------------
