nums=[1, 2, 3, 4, 5, 6, 7, 8]
odd_nums=list(filter(lambda a:a % 2 == 1, nums))
print(odd_nums)


nums=[1, 2, 3, 4, 5, 6, 7, 8]
even_nums=list(filter(lambda a:a % 2 == 0, nums))
print(even_nums)

from math import sqrt
nums=[1,2,3,4,5,6,7,8,9]
ispower=list(filter(lambda n:sqrt(n) == int(sqrt(n)), nums))
print(ispower)


nums = [5, 12, 7, 20, 3]
big = list(filter(lambda x: x > 10, nums))
print(big)


words = ["cat", "tiger", "lion", "elephant"]
ls = list(filter(lambda w: len(w) > 4, words))
print(ls)
