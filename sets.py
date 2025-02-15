numbers=[1,1,2,3,4]
first=set(numbers)
print(first) #it will give unique values
second={1,2}
# second.add(5)
# second.remove(5)
# len(second)

print(first | second) #union
print( first & second) #intersection
print(first - second) 
print( first ^ second) # only exist in first or exist in second
