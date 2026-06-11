num=int(input("Enter the number: "))

sum=0
for i in range(1,(num//2)+1):
    if(num%i==0):
        sum=sum+i

if(num==sum):
    print("Perfect number.")

else:
    print("Not perfect number.")