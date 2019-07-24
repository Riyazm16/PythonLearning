tup = ("riyaj",4,50,50,2)
print(tup)
print(tup[0])
print(tup[2:5])
print(tup[2])
print(tup*9)
print(tup.index(50))
print(tup.index("riyaj"))
print(tup.count(50)) #count the occurance

# converting list to tupple

lst= [1,4,5]
tp1= tuple(lst)
print(type(tp1))