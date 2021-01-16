from abc import ABC
class Shape(ABC):     #abstract class
    def calculate_area(self):     #abstract method
        pass

class Rectangle(Shape):
  length = 5
  breadth = 3
  def calculate_area(self):
      return self.length * self.breadth

class Circle(Shape):
  radius = 4
  def calculate_area(self):
      return 3.14 * self.radius * self.radius

rec =Rectangle()    #object created for the class 'Rectangle'
cir = Circle()    #object created for the class 'Circle'
print("Area of a rectangle:", rec.calculate_area())     #call to 'calculate_area' method defined inside the class 'Rectangle'
print("Area of a circle:", cir.calculate_area())    #call to 'calculate_area' method defined inside the class 'Circle'

----------------------------------------------------------------------------------------------------------------------------------------

# An abstract class having a normal method and an abstract method

from abc import ABC
class Shape(ABC):
    def print(self):
        print("I am a normal method defined inside the abstract class 'Shape'")
    def calculate_are(self):
        pass

class Rectangle(Shape):
    length = 5
    breadth = 3
    def calculate_area(self):
        return self.length * self.breadth

rec = Rectangle() #object created for the class 'Rectangle'
rec.print()
print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'

---------------------------------------------------------------------------------------------------------------------------------------

