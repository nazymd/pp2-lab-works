class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass
c = C()
c.method_a()
c.method_b()


class Student:
    def study(self):
        print("Studying")

class Athlete:
    def train(self):
        print("Training")
class StudentAthlete(Student, Athlete):
    pass
sa = StudentAthlete()
sa.study()
sa.train()


class Addition:
    def add(self, a, b):
        print(a + b)

class Multiplication:
    def multiply(self, a, b):
        print(a * b)
class Calculator(Addition, Multiplication):
    pass
c = Calculator()
c.add(3, 4)
c.multiply(3, 4)


class A:
    def __init__(self):
        print("A constructor")

class B:
    def __init__(self):
        print("B constructor")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C constructor")
c = C()


class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")

class C(A, B):
    pass
c = C()
c.hello()
