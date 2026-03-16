f=open('data.txt', "r")
print(f.read())

with open("data.txt") as f:
  print(f.read())