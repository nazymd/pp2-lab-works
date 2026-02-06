#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Print only odd numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


#Skip negative numbers
numbers = [3, -1, 5, -7, 2]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1


text = "banana"
i = 0
while i < len(text):
    if text[i] == 'a':
        i += 1
        continue
    print(text[i])
    i += 1


text = "Hello World"
i = 0
while i < len(text):
    if text[i] == " ":
        i += 1
        continue
    print(text[i])
    i += 1

