import re
s=input()
arr=re.split("\s", s)
for i in arr:
    x=re.findall(r"^ab{2,3}$", i)
    print(x)