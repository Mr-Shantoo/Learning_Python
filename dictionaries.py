point={"x":1,"y":2}
#we can also use dict function
point=dict(x=1,y=2)

print(point["x"])
point["x"]=10
print(point["x"])
point["z"]=20 #adding another one

if "a" in point:
    print(point["a"]) #if key a exist in poinnt thn it will print

point.get("a") #if a doesn't exist it will print none.. we can also assign default return  to anything 

##example 
print(point.get("a","not found"))

#for deleting
del point["x"]
print(point)

#ffor loop over dictionary
for key in point:
    print(key,point[key])

##dictionary comprehension

values={x:x*3 for x in range(5)}
print(values)


