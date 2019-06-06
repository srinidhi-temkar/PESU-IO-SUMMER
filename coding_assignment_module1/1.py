num = str(input("Enter comma separated integers : "))
l=num.split(",")
lis=[]
for i in l:
    lis.append(int(i))
print ("list: ", lis)
tup = tuple(lis)
print("tuple:",tup)