lis=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, l in enumerate(lis, start=1):
    print(f"Index:{i} and Number:{l}")
letters=["a", "b", "c"]
ind=[1, 2, 3]
for i, l in zip(letters, ind):
    print(i, l)