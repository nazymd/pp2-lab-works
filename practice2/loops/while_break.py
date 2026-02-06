#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#Exit the loop when n is 9:
nums = [4, 7, 2, 9, 5]
i = 0
while i < len(nums):
    if nums[i] == 9:
        break
    print(nums[i])
    i += 1


#show first even number
nums = [1, 3, 5, 8, 10]
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        print("first even:", nums[i])
        break
    i += 1


text = "hello world"
i = 0
while i < len(text):
    if text[i] == "o":
        print("Found o!")
        break
    i += 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while i < len(nums):
    if nums[i] == 9:
        break
    print(nums[i])
    i += 1


