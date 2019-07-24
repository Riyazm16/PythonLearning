lst = [1,5,"riyaj",7,4]
print(lst)
print(lst[0])
print(lst[0:3])
print(lst*5)
print(len(lst))

#adding and removing the element

lst.append(9)
del(lst[2])


# testing some more funcions on the list for performing dynamic operartion on the list

lst.append(600)
print(lst)

lst.remove(600)

print(max(lst))
print(min(lst))
lst.insert(3,88)
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# lst.remove("riyaj")
