def cal_sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub



num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
print("Sum and subration of the entered numbers are: ", cal_sum_sub(num1,num2))