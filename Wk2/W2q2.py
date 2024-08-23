num=int(input("Enter the number whose total digits are to be calculated: "))
count=0
while num>0:
    count+=1
    num=num//10
print("There are",count,"digits in the number entered!")    