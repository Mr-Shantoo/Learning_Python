items=[
    ("product1",10),
    ("product2",9),
    ("product3",12)
]
# for prices of the items
# one way
prices=[]
for item in items:
    prices.append(item[1])
    
print(prices)
#another way whic is map function
x=map(lambda item:item[1],items)
# for printing
for item in x:
    print(item)

#we can also use list object
price=list(map(lambda item:item[1],items))
print(price)


###filter function

x=list(filter(lambda item:item[1]>=10,items))
print(x)

##filter function checks our condition and if it's matches the condition then stores it

#list comprehension
# by using it we can acheive the same thing of map and filter
# it's a better and cleaner approach

#map--->list comprehension
prices=[item[1] for item in items]
print(prices)

##filter--->> list comprehension
prices=[item for item in items if item[1]>=10]
print(prices)

##zip function
list1=[1,2,3]
list2=[4,5,6]
##if we want something like (1,4) (2,5) (3,6)
print(list(zip(list1,list2)))