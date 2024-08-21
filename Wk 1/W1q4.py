num= int(input("Enter your number: "))
original_num=num
reversed_num=0
while num>0:
    remainder=num%10
    reversed_num=(reversed_num * 10) + remainder
    num=num//10
if(reversed_num == original_num):
    print("Entered num is a palindrome number ")  
else:
    print("Entered num is not a palindrome number: ")       
