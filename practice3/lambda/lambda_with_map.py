numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers=[1, 2, 3, 4, 5]
power=list(map(lambda a:a**2, numbers))
print(power)


strings=["Nazym", "Nazerke", "Balgynbek", "Aigerim", "KasymKHAN"]
lenova=list(map(lambda w:len(w), strings))
print(lenova)

a=[12, 13, 34, 65, 46]
b=[4, 5, 3, 7, 8]
div=list(map(lambda x, y: x//y, a, b))
print (div)


nums = ["10", "20", "30"]
numbers = list(map(lambda s: int(s), nums))
print(numbers)
