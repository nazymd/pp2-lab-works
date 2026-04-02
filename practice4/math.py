# /Users/nazym/Documents/PP2/practice5fake/math/area.py
import math
n = int(input('Input number of sides: '))
l = int(input('Input the length of a side: '))
ans=(n*l*l)//(4*math.tan(math.pi/n))
print("The area of the polygon is: ",ans)

# /Users/nazym/Documents/PP2/practice5fake/math/parallelogram.py
import math
b=float(input("Length of base: "))
p=float(input("Height of parallelogram: "))
print("Expected Output:", b*p)

# /Users/nazym/Documents/PP2/practice5fake/math/radian.py
import math
degree=float(input('Input degree: '))
radian=math.radians(degree)
print("Output radian:", f"{radian:.6f}")

# /Users/nazym/Documents/PP2/practice5fake/math/trapezoid.py
import math
h=float(input())
a=float(input())
b=float(input())
print((a+b)/2*h)