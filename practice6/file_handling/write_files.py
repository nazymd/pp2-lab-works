with open("data.txt", "a") as f:
  f.write("Now the file has more content!")
  f.write("Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.")
with open ("data.txt", 'r') as f:
  print(f.read())

with open("data.txt", "w") as f:
    f.write("Hello")
with open ("data.txt", 'r') as f:
  print(f.read())
