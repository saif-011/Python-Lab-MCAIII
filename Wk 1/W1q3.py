list1=[]

for i in range(20):
    num=int(input(f"Enter the {i+1}: number of your list"))
    list1.append(num)
list2=[]    
for num in list1:
    if num % 5 == 0:
        list2.append(num)
print("The number of your list which are divisible by 5 are: ", list2)        