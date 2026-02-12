class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Linus", 28)
print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)


class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country
p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)



class Family:
  def __init__(self, father, mother, brother, sister):
    self.father=father
    self.mother=mother
    self.brother=brother
    self.sister=sister
f1=Family("Duisen", "Aigul", "Balgynbek", "Nazerke")
f2=Family("Bolat", "Zaya", "Shyngys", "Zhanerke")
print("First family", "Second family")
print(f1.father, f2.father)
print(f1.mother, f2.mother)
print(f1.brother, f2.brother)
print(f1.sister, f2.sister)
