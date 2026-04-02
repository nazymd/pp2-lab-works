def div(num):
    for i in range(0, num+1):
        if i % 12 == 0:
            yield i

n=int(input())
d=div(n)
for i in d:
    print(i)


def down(num):
    for i in range(num, -1, -1):
        yield i
n=int(input())
d=down(n)
for i in d:
    print(i)


def even(num):
    for i in range(0, num+1):
        if i % 2 == 0:
            yield i

n=int(input())
e=even(n)
cnt=0
for i in e:
    cnt+=1
    if cnt != (n // 2)+1:
        print (i, end=",")
    else:
        print(i, end="")


def square(num):
    for i in  range(1, num + 1):
        yield i*i
n=int(input())
s=square(n)
for i in s:
    print(i)


def square(a, b):
    for i in range (a, b+1):
        yield i * i
n, m=map(int, input().split())
for i in square(n, m):
    print(i)
