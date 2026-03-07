import re
s=input()
arr=re.split("_",s)
ans=arr[0]
for i in range(1, len(arr)):
    ans+=arr[i].capitalize()
print(ans)