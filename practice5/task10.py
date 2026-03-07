import re
s=input()
ans=""
for i in s:
    if re.match("[A-Z]", i):
        ans+="_"
    ans+=i
print(ans)