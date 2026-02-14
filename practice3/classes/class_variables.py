class Student:
    school = "KBTU"   # class variable
    def __init__(self, name):
        self.name = name  # instance variable
s1 = Student("Ali")
s2 = Student("Dana")

print(s1.school)  # Harvard
print(s2.school)  # Harvard


class Student:
    school_name = 'ABC School '   
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
s2 = Student('Jessa', 20)
print(s2.name, s2.roll_no, Student.school_name)


class Dog:
    species = "Animal"  
    def __init__(self, name):
        self.name = name 
d1 = Dog("Buddy")
d2 = Dog("Max")

print(d1.species)
print(d2.species)


class Product:
    shipping_cost = 500   # общая доставка

    def __init__(self, name):
        self.name = name
p1 = Product("Phone")
p2 = Product("Laptop")
print(p1.shipping_cost)
print(p2.shipping_cost)


class Dog:
    legs = 4

d1 = Dog()
d2 = Dog()
d1.legs = 3
print(d1.legs)
print(d2.legs)

