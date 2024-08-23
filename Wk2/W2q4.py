num=int(input("Enter the number whose factorial needs to be calculated:- "))
factorial=1
while num>0:
    factorial= factorial*num
    num-=1
print("Factorial of  the entered number is : ",factorial)    