# handling exception
try:
    with open("Exception.py") as file:
        print("file")
        # now we don't need to close it python will automatically do it
    age = int(input("age:"))
    xfactor = 10/age
# except ValueError:
#     print("you didn't eanter a valid age.")
# except ZeroDivisionError:
#     print("age can not be zero")
# we can do the same two exception using one
except (ValueError, ZeroDivisionError):
    print("you didn't eanter a valid age.")

else:
    # this will only be execute if there is no exception
    print("no exception were thrown")

# finally clause;
# finally:
#     file.close()

# throw and raise exception..


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age can not be zero or less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
