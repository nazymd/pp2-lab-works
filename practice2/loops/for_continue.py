fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  #Do not print banana:


  for i in range(1, 8):
    if i == 5:
        continue
    print(i)


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


text = "Hello World"
for ch in text:
    if ch == " ":
        continue
    print(ch)


nums = [3, -1, 7, -5, 2]
for n in nums:
    if n < 0:
        continue
    print(n)

