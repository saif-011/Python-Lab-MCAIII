range_num1=int(input("Enter the starting value of your range "))
range_num2=int(input("Enter the ending value of your range "))
list1=[]

def find_prime(a):                   #Function to check prime nummber
    flag=1
    for j in range(2,a):
        if(a%j ==0):
            flag= 0
            break
        else:
            j+=1
    if (flag==0):
        return 0
    else:
        return 1
    

for i in range(range_num1,range_num2+1):       #Loop iteration to check prime numberr between the given range
    num=find_prime(i)
    if num==1:
        list1.append(i)
    elif num==0:
        i+=1    
print("Prime no between the given range are: " ,list1)

    