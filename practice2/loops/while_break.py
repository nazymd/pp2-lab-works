#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Exit the loop when n is 9:
nums = [4, 7, 2, 9, 5]
for n in nums:
    if n == 9:
        break
    print(n)


#show first even number
nums = [1, 3, 5, 8, 10]
for n in nums:
    if n % 2 == 0:
        print("first even:", n)
        break


text = "hello world"
for ch in text:
    if ch == "o":
        print("Found o!")
        break


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in nums:
    if n == 9:
        break
    print(n)
