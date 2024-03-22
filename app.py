def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total


result = multiply(1, 2, 3, 4)
print(result)
