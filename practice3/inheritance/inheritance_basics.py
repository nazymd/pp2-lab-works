class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


class Person:
    def walk(self):
        print("Walking")

class Student(Person):
    def study(self):
        print("Studying")



class Animal:
    def eat(self):
        print("I can eat")

class Dog(Animal):
    pass
d = Dog()
d.eat()


class A:
    def hello(self):
        print("Hello")

class B(A):
    pass
b = B()
b.hello()


class Vehicle:
    def start(self):
        print("Engine started")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
c = Car()
b = Bike()
c.start()
b.start()


