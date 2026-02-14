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


class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")


class Animal:
    def eat(self):
        print("I can eat")

class Dog(Animal):
    pass
d = Dog()
d.eat()


class Animal:
    def sound(self):
        print("Animal sound")
class Cat(Animal):
    def sound(self):
        print("Meow")
c = Cat()
c.sound()


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


