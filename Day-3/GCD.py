num1=int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

GCD=1
for i in range(min(num1,num2),0,-1):
    if(num1%i==0 and num2%i==0):
        GCD=i
        break

print("GCD of two numbers:",GCD)