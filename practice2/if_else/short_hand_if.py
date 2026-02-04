a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#variable = value_if_true if condition else value_if_false

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#One line, three outcomes:


username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
#Setting a default value:

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
#Finding the maximum of two numbers:
