for x in "python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(5):
    print(x)  # will print from 0-4


for x in range(2, 5):
    print(x)  # we can pass the starting number

for x in range(0, 10, 2):
    print(x)  # it will return even from 0-10

names = ["shanto", "star"]

for name in names:
    if name.startswith("s"):
        print("found")
        break
else:
    print("not found")

    # for else.. if we don't find anything starts with s thn it will break and execute the else
