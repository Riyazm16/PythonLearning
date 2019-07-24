sets = {"riyaj",5,6,7}

sets.update([20,90])
sets = frozenset(sets)

for x in sets:
	print(x)
print(sets)