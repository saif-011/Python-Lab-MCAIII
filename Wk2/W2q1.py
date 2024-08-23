num=int(input("Enter the number whose digits are need to be extracted:"))
list=[]                                     #we create a list to stored the digits of our number 
while num > 0:
    remainder=num % 10
    list.append(remainder)                  #Here we append our remainder which is our one's digit 
    num=num//10
print("The final output is: ", list)    