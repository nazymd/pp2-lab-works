students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[0][0])
print(sorted_students)


people = [
    {"name": "Ali", "age": 25},
    {"name": "Dana", "age": 19},
    {"name": "Omar", "age": 30}
]
print(sorted(people, key=lambda p: p["age"]))


words = ["cat", "banana", "apple", "dog"]
print(sorted(words, key=lambda w: w[-1]))