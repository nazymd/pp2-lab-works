def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
print(my_function(3, 7, 2, 9, 1))


def get_greeting():
  return "Hello from a function"
print(get_greeting())


def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result)


def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)