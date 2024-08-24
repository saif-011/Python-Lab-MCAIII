list1=[2,21,13,9,11,7,10,40,27,91,61]
length=len(list1)
for i in range(0,length-1):
    list1[i]=list1[i]*list1[i]
print("The new list of integers with each element turned into its square is:",list1)    