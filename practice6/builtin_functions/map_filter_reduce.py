lis=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums=map(lambda x:x,filter(lambda x:x%2==0,lis))
for i in even_nums:
    print(i)
from functools import reduce
print(reduce(lambda x, y: x + y, lis))
