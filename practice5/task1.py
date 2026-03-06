import re
s=input()
arr=re.split("\s", s)
for i in arr:
    x=re.findall(".*ab*.*", i)
    print(x)