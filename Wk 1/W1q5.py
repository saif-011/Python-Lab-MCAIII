num=int(input("Enter the target till which cubes are to be printed: "))
cubes=[]
for i in range(1,num+1):
    cubes.append(i*i*i)
print(cubes)    