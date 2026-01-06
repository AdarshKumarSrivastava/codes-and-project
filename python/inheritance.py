'''class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person): #way to inherit data fromm one class to another
  def _init_(self, fname, lname):
    Person._init_(self, fname, lname)
  def printabc(self):
    print(self.firstname, self.lastname)

class Third(Student): #way to inherit data fromm one class to another
  def _init_(self, fname, lname):
    Person._init_(self, fname, lname)
  def printaa(self):
    print(self.firstname, self.lastname)


x = Third(3,6)
x.printname()
x.printaa()'''

#polymorphism
class Car:
  def __init__(self, brand, model,a):
    self.brand = brand
    self.model = model
    self.a=45

  def move(self):
    print("Drive!")
    print(self.brand,self.a)

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail! aaaaaaaaaaaa ddddddddddd")
    print("Sail! aaaaaaaaaaaa ddddddddddd")

class Plane:
  def __init__(self, brand):
    self.brand = brand
 

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang",45)       #Create a Car object
boat1 = Boat("Ibiza", "Touring20") #Create a Boat object
plane1 = Plane("Boeing")     #Create a Plane object

for x in (car1, boat1):
  x.move() 
