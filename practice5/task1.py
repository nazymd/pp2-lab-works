import re
s=input()
arr=re.split("\s", s)
print(arr)
for i in arr:
    x=re.findall(".*ab*.*", i)
    print(x)