import re
s=input()
x=re.findall("[a-z]+_[a-z]", s)
print(x)