name = input("enter your name")

nameLen = len(name)

if nameLen < 6:
    print("the length is only "+str(nameLen)+" characters")
elif nameLen > 4:
    print("name is "+str(nameLen)+ "characters long")
else:
    print("i dont want to tell u :p")