def binary(lis, l, r, ele):   
    while l <= r:   
        mid = l + (r - l)//2
        # mid = (l+r)//2
        if lis[mid] == ele:
            return mid+1
        elif lis[mid] < ele: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1
  
  
lis=sorted([int(x) for x in input("Enter comma seperated integers : ").split(",")])
ele=int(input("Enter element to search : "))
print("Sorted list : ",lis)

result = binary(lis, 0, len(lis)-1, ele) 
  
if result != -1: 
    print ("Element is present at position",result,"in the sorted list")
else: 
    print ("Element is not present in list")