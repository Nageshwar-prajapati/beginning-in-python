num1=int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

GCD=1
for i in range(2,min(num1,num2)):
    if(num1%i==0 and num2%i==0):
        GCD=i
        
LCM=(num1*num2)//GCD
print("LCM of two numbers:",LCM)