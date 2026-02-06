#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


for i in range(1, 11):
    if i == 5:
        break
    print(i)


nums = [1, 3, 5, 8, 9, 10]
for n in nums:
    if n % 2 == 0:
        print("First even number:", n)
        break


nums = [5, 8, 3, -2, 7, -1]
for n in nums:
    if n < 0:
        print("Negative number found:", n)
        break
    print(n)
