class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
d = Dog()
d.sound()


class Animal:
    def sound(self):
        print("Animal sound")
class Cat(Animal):
    def sound(self):
        print("Meow")
c = Cat()
c.sound()


class Shape:
    def area(self):
        print("Area formula")

class Circle(Shape):
    def area(self):
        print("Area = 3.14 * r * r")


class Figure:
    def perimeter(self):
        print("Perimeter formula")
class Rectangle(Figure):
    def perimeter(self, a, b):
        print(2 * (a + b))
class Triangle(Figure):
    def perimeter(self, a, b, c):
        print(a + b + c)
r = Rectangle()
r.perimeter(3, 4)

t = Triangle()
t.perimeter(3, 4, 5)


class Power:
    def calculate(self, x):
        print("Base power")
class SquarePower(Power):
    def calculate(self, x):
        print(x ** 2)
class CubePower(Power):
    def calculate(self, x):
        print(x ** 3)
s = SquarePower()
s.calculate(4)  

c = CubePower()
c.calculate(3)
