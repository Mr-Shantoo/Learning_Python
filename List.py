letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
# list of hundred Zero..
zeros = [0]*5
print(zeros)  # using this we can repeat a list of thing how many times we want

# # concate two list using +
combined = letters + zeros
print(combined)
numbers=list (range(20))
print(numbers) # will print up to 19
chars=list("maine uddin shanto")
print(chars)
print(len(chars)) #will print length

# we can access individuals items fom list
letters=['s','h','a','n','t','o']
print(letters[0])
print(letters[-2])
print(letters[0:5])
print(letters[0:])
print(letters[:5])
print(letters[:])

numbers=list(range(20))
print(numbers)
#now i want to print  all the evens of the list
print("all the even nummbers of the list")
print(numbers[::2])
print("reverse order")
print(numbers[::-1])

# unpacking list
num=[1,2,3]
first=num[0]
second=num[1]
third=num[2]
# #we can do this in a better way for aassigning the values
# #for that the variables and list items needs to be equal

first,second,third=num
# if we only want few values from the list
num=[1,2,3,4,5,6]

first,second,*others=num
# #what it will do is first two values of the list will be assigned
# #and others will go to another list called others
# #now let's print
print(first)
print(others)
# what if we only want the first and last
#here how we can do ite
first, *others,last=num
#let's print
print(first)
print(others)
print(last)


# printing the list with the index as a tuples\
name = ['s', 'h', 'a', 'n', 't', 'o']

for index,value in enumerate(name):
    print(index,value)

# add and remove
letters = ["a", "b", "c", "d"]
letters.append("e") #add something in the end of the list
letters.insert(0,"A")
#removing
letters.pop() #it will remove from end
letters.pop(0)# removing first one
letters.remove("b") #first occurance
#for removing every b loop over the list and remove
#by usinng del method we can remove the list in a range
del letters[0:3]
print(letters)
# for removing everything of the list
letters.clear()


#sorting list

num=[5,6,9,2,4,1,10]
num.sort()#ascending order
print(num)
num.sort(reverse=True)#descending order
print(num)

#another way
print(sorted(num))
print(sorted(num,reverse=True))

#for list of tuples..
items=[
    ("product1",15),
    ("product2",11),
    ("product3",13)

]

#for sorting this
def sort_item(item):
    return item[1]

items.sort(key=sort_item) #simply passing the reference
print(items)

#better way of sorting
#lamda function or expression
items.sort(key=lambda item:item[1])
print(items)