import re

file = open('raw.data','r') 
text = file.read()

prices = re.findall(r"\d[\d\s]*,\d{2}$", text)

names = re.findall(r"\d+\.\n(.+)", text)

summa = 0
for i in prices:
    price = i.replace(" ", "").replace(",", ".")
    summa += float(price)

data = re.findall(r"\d{2}\.\d{2}\.\d{4}", text)
time = re.findall(r"\d{2}:\d{2}:\d{2}", text)

payment = re.findall(r"Банковская карта|Наличные", text)

print("Prices")
for i in prices:
    print(i)
print("\n")

print("Names of products")
for i in names:
    print(i)
print("\n")

print("Total summa")
print(summa)
print("\n")

print("Date and time")
print(data, time)
print("\n")

print("Payment method")
print(payment)