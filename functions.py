def increment(number, by):
    #return number+by
    return (number, number+by)


print(increment(2, 3))

# def increment(num: int, by: int = 1) -> int:
#     return by+num


# print(increment(3))
def multiply(*list): #python will see the list as a tuple
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

def save_user(**user): #works like a dictionay
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=1,name="shanto")
