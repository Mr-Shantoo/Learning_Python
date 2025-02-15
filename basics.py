import math
# variables
student = 100
rating = 4.90
is_published = False
course_name = "dsa"  # single line_string
course_name = """
 data structures and algorithm
 """  # multiline_string
x, y = 1, 2
x = y = 1

# dynamic language python..determine the type of variable in run time
price = 1000
print(type(price))
price = 10.50
print(price)

# String
course = "python programming"
print(len(course))  # for lenght
print(course[0])  # for first index
print(course[-1])  # it will return values from last
print(course[-2])  # it will return n
print(course[0:3])  # it will return from characters from 0 to end-1
print(course[:3])  # will do the same
print(course[0:])  # it will return from first to last
print(course[:])  # it will also do the same
# escape sequence
msg = "Maine \"uddin shanto"
print(msg)
# \"
# \'
# \\
# \n

# formating_string
first = "maine uddin"
last = "shanto"
full = first+" "+last
print(full)
# better way
full = f"{first} {last}"
print(full)
# string methods of_string
string = "data structures"
print(string.upper())  # for upper case
print(string.lower())  # for lower case
print(string.title())  # first character upper case
print(string.strip())  # for removing space... left right strip do the same
print(string.find("st"))  # for finding something in the_string
# case sensitive
print(string.replace("s", "_"))  # it will replace s with _
print("data" in string)  # it will return true..
print("data" not in string)  # it will return false

# arithmetic operations
x = 10+3  # additon
x = 10-3  # subtraction
x = 10*3  # multipication
x = 10/3  # will return floating values
x = 10//3  # will return int values
x = 10 % 3  # mod
x = 10**3  # 10 to the power 3

# playing with numbers

PI = 3.50
print(round(PI))
print(abs(PI))
print(math.floor(PI))

# conditional statement

age = 21
if age >= 18:
    print("adult")
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

print("All done")  # for empty block use pass syntex


# ternary operator
age = 21
if age >= 18:
    msg = "eligbile"
else:
    msg = "not eligible"
# ternary operation
msg = "Eligbile" if age >= 18 else "Not eligible"
print(msg)
